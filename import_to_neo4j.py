#!/usr/bin/env python
"""
Import a GEXF file into Neo4j for visualization and analysis.
"""

import networkx as nx
from neo4j import GraphDatabase
import os
import sys
import json

# Neo4j credentials and connection settings
NEO4J_URI = "neo4j://localhost:7687"  # This matches the Bolt port in the screenshot
NEO4J_USER = "neo4j"  # Default username
NEO4J_PASSWORD = "12345678"  # Password from 1 to 8 as mentioned by the user

def import_gexf_to_neo4j(gexf_file, uri=NEO4J_URI, user=NEO4J_USER, password=NEO4J_PASSWORD, clear_db=True):
    """
    Import a GEXF file into Neo4j.
    
    Args:
        gexf_file (str): Path to the GEXF file.
        uri (str): Neo4j URI.
        user (str): Neo4j username.
        password (str): Neo4j password.
        clear_db (bool): Whether to clear the database before importing.
    """
    print(f"Reading GEXF file: {gexf_file}")
    G = nx.read_gexf(gexf_file)
    print(f"Graph loaded with {len(G.nodes())} nodes and {len(G.edges())} edges")
    
    # Connect to Neo4j
    print(f"Connecting to Neo4j at {uri}")
    driver = GraphDatabase.driver(uri, auth=(user, password))
    
    with driver.session() as session:
        if clear_db:
            print("Clearing existing graph data...")
            session.run("MATCH (n) DETACH DELETE n")
        
        # Create node property constraints and indexes for faster lookups
        try:
            session.run("CREATE CONSTRAINT node_id IF NOT EXISTS FOR (n:Node) REQUIRE n.id IS UNIQUE")
        except Exception as e:
            print(f"Note: Could not create constraint: {e}")
            # Fall back to index for older Neo4j versions
            try:
                session.run("CREATE INDEX node_id_index IF NOT EXISTS FOR (n:Node) ON (n.id)")
            except Exception as e2:
                print(f"Note: Could not create index either: {e2}")
        
        # Create nodes
        print("Creating nodes...")
        for i, (node_id, node_data) in enumerate(G.nodes(data=True)):
            # Process node attributes
            props = {}
            for key, value in node_data.items():
                # Skip complex objects that Neo4j can't store
                if isinstance(value, (str, int, float, bool)):
                    # Truncate very long strings
                    if isinstance(value, str) and len(value) > 500:
                        value = value[:500] + "..."
                    props[key] = value
            
            # Ensure we have at least a label attribute
            if 'label' not in props and 'tag' in props:
                props['label'] = props['tag']
            elif 'label' not in props:
                props['label'] = node_id
            
            # Determine node label (Neo4j type) based on tag
            node_type = props.get('tag', 'Node').capitalize()
            
            # Create Cypher parameters
            cypher_params = {
                'node_id': node_id,
                'props': props,
                'node_type': node_type,
            }
            
            # Create the node with a label for its type and a generic Node label
            query = """
            CREATE (n:Node:`%s` {id: $node_id})
            SET n += $props
            """ % node_type
            
            session.run(query, **cypher_params)
            
            # Progress update for large graphs
            if (i + 1) % 100 == 0 or (i + 1) == len(G.nodes()):
                print(f"Created {i + 1}/{len(G.nodes())} nodes")
        
        # Create relationships
        print("Creating relationships...")
        for i, (source, target) in enumerate(G.edges()):
            query = """
            MATCH (a:Node {id: $source}), (b:Node {id: $target})
            CREATE (a)-[r:CONNECTS_TO]->(b)
            """
            session.run(query, source=source, target=target)
            
            # Progress update for large graphs
            if (i + 1) % 500 == 0 or (i + 1) == len(G.edges()):
                print(f"Created {i + 1}/{len(G.edges())} relationships")
    
    # Close the driver
    driver.close()
    print("Import complete!")
    print("\nTo visualize in Neo4j Browser:")
    print("1. Open Neo4j Desktop")
    print("2. Start your database")
    print("3. Click 'Open' to launch Neo4j Browser")
    print("4. Run these Cypher queries:")
    print("   - See all nodes: MATCH (n) RETURN n LIMIT 100")
    print("   - View by type: MATCH (n:`Section`) RETURN n LIMIT 25")
    print("   - Explore document structure: MATCH p=(n)-[r:CONNECTS_TO*1..2]->(m) WHERE n.tag='document' RETURN p")
    print("   - Find specific content: MATCH (n) WHERE n.text_content CONTAINS 'algebra' RETURN n LIMIT 10")

if __name__ == "__main__":
    # Check for custom Neo4j credentials from environment variables
    uri = os.environ.get("NEO4J_URI", NEO4J_URI)
    user = os.environ.get("NEO4J_USER", NEO4J_USER)
    password = os.environ.get("NEO4J_PASSWORD", NEO4J_PASSWORD)
    
    if len(sys.argv) < 2:
        print("Usage: python import_to_neo4j.py <gexf_file> [--no-clear]")
        print("Using default: graph_output.gexf")
        gexf_file = "graph_output.gexf"
        if not os.path.exists(gexf_file):
            print(f"Error: Default file {gexf_file} not found.")
            sys.exit(1)
    else:
        gexf_file = sys.argv[1]
    
    # Check if we should preserve existing data
    clear_db = True
    if "--no-clear" in sys.argv:
        clear_db = False
        print("Note: Preserving existing database data")
    
    print("\nBEFORE RUNNING THIS SCRIPT:")
    print("1. Make sure Neo4j Desktop is open and your database is started")
    print("2. If this is your first time connecting, click 'Open' to open Neo4j Browser")
    print("3. In Neo4j Browser, you'll be prompted to change your password from 'neo4j'")
    print("4. After changing your password, update NEO4J_PASSWORD in this script")
    print("5. Or provide your password via command line: NEO4J_PASSWORD=yourpassword python import_to_neo4j.py\n")
    
    proceed = input("Do you want to proceed with the import? (yes/no): ")
    if proceed.lower() not in ["y", "yes"]:
        print("Import cancelled.")
        sys.exit(0)
    
    try:
        import_gexf_to_neo4j(gexf_file, uri, user, password, clear_db)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1) 