import os
import sys
import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import json
from cnxml_to_graph import add_nodes_edges, get_unique_node_name

# Define namespaces
CNXML_NS = "http://cnx.rice.edu/cnxml"
COLLXML_NS = "http://cnx.rice.edu/collxml"
MDML_NS = "http://cnx.rice.edu/mdml"

def parse_collection(collection_path):
    """
    Parse the collection XML file to extract the course structure.
    Returns a dictionary representing the hierarchy and a flat list of all module IDs.
    """
    try:
        # Register namespaces
        ET.register_namespace('', COLLXML_NS)
        ET.register_namespace('md', MDML_NS)
        ET.register_namespace('col', COLLXML_NS)
        
        # Parse the collection XML
        tree = ET.parse(collection_path)
        root = tree.getroot()
        
        # Extract course metadata
        metadata = root.find(f'.//{{{MDML_NS}}}title')
        course_title = metadata.text if metadata is not None else "Untitled Course"
        
        # Get course UUID
        uuid_elem = root.find(f'.//{{{MDML_NS}}}uuid')
        course_uuid = uuid_elem.text if uuid_elem is not None else "no-uuid"
        
        # Initialize hierarchy and module list
        course_hierarchy = {
            'title': course_title,
            'uuid': course_uuid,
            'chapters': [],
            'module_order': []  # To preserve sequence
        }
        all_modules = []
        
        # Process content (chapters and modules)
        content = root.find(f'.//{{{COLLXML_NS}}}content')
        if content is not None:
            # Process direct module children of content (not in chapters)
            for module in content.findall(f'.//{{{COLLXML_NS}}}module'):
                module_id = module.get('document')
                course_hierarchy['module_order'].append(module_id)
                all_modules.append(module_id)
            
            # Process chapters (subcollections)
            for subcol_idx, subcollection in enumerate(content.findall(f'.//{{{COLLXML_NS}}}subcollection')):
                chapter = {
                    'index': subcol_idx,
                    'modules': [],
                    'module_order': []
                }
                
                # Get chapter title
                chapter_title = subcollection.find(f'.//{{{MDML_NS}}}title')
                chapter['title'] = chapter_title.text if chapter_title is not None else f"Chapter {subcol_idx+1}"
                
                # Get modules in this chapter
                subcol_content = subcollection.find(f'.//{{{COLLXML_NS}}}content')
                if subcol_content is not None:
                    for module in subcol_content.findall(f'.//{{{COLLXML_NS}}}module'):
                        module_id = module.get('document')
                        chapter['modules'].append(module_id)
                        chapter['module_order'].append(module_id)
                        all_modules.append(module_id)
                
                course_hierarchy['chapters'].append(chapter)
        
        return course_hierarchy, all_modules
    
    except Exception as e:
        print(f"Error parsing collection XML: {e}")
        return None, []

def build_module_graph(module_id, modules_dir="modules"):
    """
    Build a graph for a single module using the existing cnxml_to_graph functionality.
    Returns the graph and unique ID for the module's document node.
    """
    module_path = os.path.join(modules_dir, module_id, "index.cnxml")
    if not os.path.exists(module_path):
        print(f"Module file not found: {module_path}")
        return None, None
    
    try:
        # Register namespaces
        ET.register_namespace('', CNXML_NS)
        
        # Parse the module XML
        tree = ET.parse(module_path)
        root = tree.getroot()
        
        # Create a new graph for this module
        G = nx.DiGraph()
        
        # Use the existing function from cnxml_to_graph to build the module graph
        add_nodes_edges(G, root)
        
        # Find the document node (root of the module)
        document_node_id = None
        for node, data in G.nodes(data=True):
            if data.get('tag') == 'document':
                document_node_id = node
                break
        
        return G, document_node_id
    
    except Exception as e:
        print(f"Error building graph for module {module_id}: {e}")
        return None, None

def extract_cross_references(G, module_id):
    """
    Extract cross-references from a module graph.
    Returns a list of (source_node, target_module_id) tuples.
    """
    cross_refs = []
    
    # Look for xref elements
    for node, data in G.nodes(data=True):
        if data.get('tag') == 'xref':
            # Check if this is a reference to another module
            document = data.get('document')
            if document and document != module_id:
                cross_refs.append((node, document))
    
    return cross_refs

def sanitize_graph_attributes(graph):
    """
    Sanitize graph attributes to make them GEXF-compatible.
    """
    sanitized_graph = nx.DiGraph()
    
    # Process nodes
    for node, attrs in graph.nodes(data=True):
        # Create a sanitized copy of the attributes
        sanitized_attrs = {}
        for key, value in attrs.items():
            # Handle various problematic attribute types
            if isinstance(value, (list, tuple)):
                # Convert lists to strings
                sanitized_attrs[key] = str(value)
            elif isinstance(value, dict):
                # Convert dicts to strings
                sanitized_attrs[key] = str(value)
            elif value is None:
                # Skip None values
                continue
            else:
                # Keep simple types as is
                sanitized_attrs[key] = value
        
        # Add the node with sanitized attributes
        sanitized_graph.add_node(node, **sanitized_attrs)
    
    # Process edges
    for u, v, attrs in graph.edges(data=True):
        # Create a sanitized copy of the attributes
        sanitized_attrs = {}
        for key, value in attrs.items():
            # Handle various problematic attribute types
            if isinstance(value, (list, tuple)):
                # Convert lists to strings
                sanitized_attrs[key] = str(value)
            elif isinstance(value, dict):
                # Convert dicts to strings
                sanitized_attrs[key] = str(value)
            elif value is None:
                # Skip None values
                continue
            else:
                # Keep simple types as is
                sanitized_attrs[key] = value
        
        # Add the edge with sanitized attributes
        sanitized_graph.add_edge(u, v, **sanitized_attrs)
    
    return sanitized_graph

def create_course_graph(collection_path, modules_dir="modules", output_dir="."):
    """
    Build a comprehensive graph of the entire course.
    """
    # Parse the collection to get course structure
    course_hierarchy, all_modules = parse_collection(collection_path)
    if not course_hierarchy:
        print("Failed to parse collection XML. Exiting.")
        return None
    
    # Deduplicate module list (some modules might appear in multiple places)
    all_modules = list(dict.fromkeys(all_modules))
    print(f"Processing {len(all_modules)} unique modules...")
    
    # Create the course-level graph
    course_graph = nx.DiGraph()
    
    # Add course root node
    course_id = f"course_{course_hierarchy['uuid']}"
    course_graph.add_node(course_id, 
                         label=course_hierarchy['title'],
                         title=course_hierarchy['title'],
                         type='course',
                         tag='course',
                         uuid=course_hierarchy['uuid'])
    
    # Add chapter nodes and connect to course
    chapter_nodes = {}
    for chapter in course_hierarchy['chapters']:
        chapter_id = f"chapter_{chapter['index']}"
        chapter_nodes[chapter_id] = {
            'title': chapter['title'],
            'modules': chapter['modules'],
            'module_order': chapter['module_order']
        }
        
        course_graph.add_node(chapter_id,
                             label=chapter['title'],
                             title=chapter['title'], 
                             type='chapter',
                             tag='chapter',
                             index=chapter['index'])
        
        # Connect chapter to course
        course_graph.add_edge(course_id, chapter_id, relation='contains')
    
    # Process each module, build its graph, and integrate
    module_graphs = {}
    module_doc_nodes = {}
    cross_references = []
    
    for module_id in all_modules:
        print(f"Building graph for module {module_id}...")
        
        # Build the module's graph
        module_graph, doc_node_id = build_module_graph(module_id, modules_dir)
        
        if module_graph and doc_node_id:
            # Store the module graph and document node
            module_graphs[module_id] = module_graph
            module_doc_nodes[module_id] = doc_node_id
            
            # Extract metadata
            module_title = "Untitled Module"
            for node, data in module_graph.nodes(data=True):
                if data.get('tag') == 'metadata':
                    title_elem = module_graph.nodes[node].get('document_title')
                    if title_elem:
                        module_title = title_elem
                        break
            
            # Create a module node in the course graph
            module_node_id = f"module_{module_id}"
            course_graph.add_node(module_node_id,
                                 label=module_title,
                                 title=module_title,
                                 type='module',
                                 tag='module',
                                 module_id=module_id,
                                 document_node=doc_node_id)
            
            # Connect module to appropriate chapter
            for chapter_id, chapter_data in chapter_nodes.items():
                if module_id in chapter_data['modules']:
                    course_graph.add_edge(chapter_id, module_node_id, relation='contains')
                    break
            
            # Extract cross-references
            module_xrefs = extract_cross_references(module_graph, module_id)
            for source, target in module_xrefs:
                cross_references.append((module_id, source, target))
    
    # Add cross-reference edges
    for source_module, source_node, target_module in cross_references:
        if source_module in module_doc_nodes and target_module in module_doc_nodes:
            source_module_node = f"module_{source_module}"
            target_module_node = f"module_{target_module}"
            course_graph.add_edge(source_module_node, target_module_node, 
                                  relation='references',
                                  source_xref_node=source_node)
    
    # Now integrate the detailed module graphs with the course graph
    integrated_graph = nx.DiGraph()
    
    # Copy course structure first
    for node, data in course_graph.nodes(data=True):
        integrated_graph.add_node(node, **data)
    
    for u, v, data in course_graph.edges(data=True):
        integrated_graph.add_edge(u, v, **data)
    
    # Add module details
    for module_id, module_graph in module_graphs.items():
        module_node_id = f"module_{module_id}"
        
        # Add all nodes from module graph
        prefix = f"{module_id}_"
        for node, data in module_graph.nodes(data=True):
            # Create a unique ID for this node in the integrated graph
            integrated_node_id = f"{prefix}{node}"
            
            # Copy all attributes (sanitized version)
            sanitized_data = {}
            for key, value in data.items():
                if isinstance(value, (str, int, float, bool)) or value is None:
                    sanitized_data[key] = value
                else:
                    # Convert complex types to string
                    sanitized_data[key] = str(value)
            
            integrated_graph.add_node(integrated_node_id, **sanitized_data)
            
            # Add additional attributes
            integrated_graph.nodes[integrated_node_id]['module_id'] = module_id
            
            # If this is the document node, connect it to the module node
            if node == module_doc_nodes[module_id]:
                integrated_graph.add_edge(module_node_id, integrated_node_id, relation='contains')
        
        # Add all edges from module graph
        for u, v, data in module_graph.edges(data=True):
            integrated_u = f"{prefix}{u}"
            integrated_v = f"{prefix}{v}"
            # Sanitize edge attributes
            sanitized_data = {}
            for key, value in data.items():
                if isinstance(value, (str, int, float, bool)) or value is None:
                    sanitized_data[key] = value
                else:
                    # Convert complex types to string
                    sanitized_data[key] = str(value)
            integrated_graph.add_edge(integrated_u, integrated_v, **sanitized_data)
    
    # Sanitize the graph to ensure it can be saved to GEXF
    print("Sanitizing graph attributes for GEXF export...")
    sanitized_graph = sanitize_graph_attributes(integrated_graph)
    
    # Save the integrated graph to GEXF
    output_gexf = os.path.join(output_dir, "course_graph.gexf")
    print(f"Saving graph to {output_gexf}...")
    nx.write_gexf(sanitized_graph, output_gexf)
    print(f"Course graph saved to {output_gexf}")
    
    # Create PyVis interactive visualization
    output_html = os.path.join(output_dir, "course_graph_interactive.html")
    print("Creating interactive visualization...")
    create_interactive_visualization(sanitized_graph, output_html)
    print(f"Interactive visualization saved to {output_html}")
    
    # Output graph statistics
    print("\nCourse Graph Statistics:")
    print(f"Nodes: {sanitized_graph.number_of_nodes()}")
    print(f"Edges: {sanitized_graph.number_of_edges()}")
    print(f"Modules processed: {len(module_graphs)}")
    print(f"Chapters: {len(course_hierarchy['chapters'])}")
    
    return sanitized_graph

def create_interactive_visualization(graph, output_path, height="800px", width="100%"):
    """
    Create an interactive HTML visualization of the graph.
    """
    # Create PyVis network
    net = Network(height=height, width=width, notebook=False, directed=True)
    
    # Configure options for better visualization
    net.set_options("""
    var options = {
      "nodes": {
        "font": { "size": 12 },
        "size": 25
      },
      "edges": {
        "color": { "inherit": true },
        "smooth": false
      },
      "physics": {
        "hierarchicalRepulsion": {
          "centralGravity": 0.0,
          "springLength": 100,
          "springConstant": 0.01,
          "nodeDistance": 120
        },
        "solver": "hierarchicalRepulsion"
      },
      "layout": {
        "hierarchical": {
          "enabled": true,
          "direction": "UD",
          "sortMethod": "directed",
          "levelSeparation": 150
        }
      }
    }
    """)
    
    # Add nodes with attributes
    for node_id, node_attrs in graph.nodes(data=True):
        # Get node type and determine color
        node_type = node_attrs.get('type', node_attrs.get('tag', 'unknown'))
        
        # Set color based on node type
        color = "#66ccff"  # Default blue
        size = 15  # Default size
        
        if node_type == 'course':
            color = "#ff0000"  # Red
            size = 40
        elif node_type == 'chapter':
            color = "#ff9900"  # Orange
            size = 30
        elif node_type == 'module':
            color = "#0099ff"  # Blue
            size = 25
        elif node_type == 'section':
            color = "#9966ff"  # Purple
            size = 20
        elif node_type == 'example':
            color = "#66ff66"  # Green
        elif node_type == 'figure':
            color = "#ff6666"  # Light red
        elif node_type == 'equation':
            color = "#cc99ff"  # Light purple
        
        # Create label and title
        label = node_attrs.get('label', node_id)
        if isinstance(label, str) and '\n' in label:
            label = label.split('\n')[0]  # Take only the first line for label
        
        title = f"Type: {node_type}"
        for key, value in node_attrs.items():
            if key not in ['label', 'tag', 'type', 'graph_node_id'] and isinstance(value, (str, int, float, bool)):
                # Truncate long values
                if isinstance(value, str) and len(value) > 200:
                    value = value[:200] + "..."
                title += f"<br>{key}: {value}"
        
        # Add node with attributes
        net.add_node(node_id, label=label, title=title, color=color, size=size)
    
    # Add edges
    for source, target, edge_attrs in graph.edges(data=True):
        # Get relationship type and set properties accordingly
        relation = edge_attrs.get('relation', '')
        title = relation
        
        if relation == 'contains':
            width = 3
        elif relation == 'references':
            width = 2
            color = "#ff0000"  # Red for cross-references
        else:
            width = 1
            
        net.add_edge(source, target, title=title, width=width)
    
    # Save the interactive visualization
    net.save_graph(output_path)
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python course_to_graph.py <collection_xml_path> [modules_dir] [output_dir]")
        return
    
    collection_path = sys.argv[1]
    modules_dir = sys.argv[2] if len(sys.argv) > 2 else "modules"
    output_dir = sys.argv[3] if len(sys.argv) > 3 else "."
    
    create_course_graph(collection_path, modules_dir, output_dir)

if __name__ == "__main__":
    main() 