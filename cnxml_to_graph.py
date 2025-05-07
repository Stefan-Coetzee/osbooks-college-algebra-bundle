import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
import textwrap
import json # For JSON output
import os # Added for XSLT path
from lxml import etree # Added for XSLT
import re # Added for regex operations
import traceback # For detailed error logging
import copy # For deepcopying elements

# Namespaces
CNXML_NS = "http://cnx.rice.edu/cnxml"
MATHML_NS = "http://www.w3.org/1998/Math/MathML"
MDML_NS = "http://cnx.rice.edu/mdml" # For metadata

# Tags that should be treated primarily as inline text or absorbed into parent's content
ABSORB_INLINE_TAGS = {'term', 'emphasis', 'foreign', 'sub', 'sup', 'code', 'link', 'xref', 'cite', 'preformat'}
# MathML tags that should be stringified, not become nodes (SUBSIDIARY TAGS - m:math itself is handled specially)
MATHML_SUB_TAGS = { # Renamed to avoid confusion
    'mi', 'mn', 'mo', 'ms', 'mspace', 'mtext', 'menclose', 'merror', 'mfenced', 
    'mfrac', 'mglyph', 'mlabeledtr', 'mmultiscripts', 'mover', 'mpadded', 'mphantom', 
    'mroot', 'mrow', 'msqrt', 'mstyle', 'msub', 'msubsup', 'msup', 'mtable', 'mtd', 'mtr', 
    'munder', 'munderover', 'maction', 'annotation', 'annotation-xml', 'semantics'
}

# --- MathML to LaTeX Conversion Utilities ---
_XSLT_BASE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vendor', 'mathml2latex_bowang')
XSLT_FILE_PATH = os.path.join(_XSLT_BASE_PATH, 'mmltex', 'mmltex.xsl')

# Placeholder for unicode_map.py content
# In a real scenario, this would be populated from vendor/mathml2latex_bowang/unicode_map.py
UNICODE_TO_LATEX_MAP = {
    '\u2061': '', # Function Application
    '\u00A0': '~', # No-break space (dummy entry for linter)
    # Example entry: '\\u2212': '\\\\(-\\\\)' # Minus sign
    # This should be filled with the actual map
}

_MATHML_XSLT_TRANSFORM = None

def _initialize_xslt_transform():
    global _MATHML_XSLT_TRANSFORM
    if _MATHML_XSLT_TRANSFORM is None:
        try:
            if not os.path.exists(XSLT_FILE_PATH):
                # Try an alternative path if the script is not in the workspace root
                # This assumes the script is one level down, e.g. in a 'src' folder
                alt_base_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'vendor', 'mathml2latex_bowang')
                alt_xslt_file_path = os.path.join(alt_base_path, 'mmltex', 'mmltex.xsl')
                if os.path.exists(alt_xslt_file_path):
                    actual_xslt_path = alt_xslt_file_path
                else:
                    print(f"XSLT file not found at {XSLT_FILE_PATH} or {alt_xslt_file_path}")
                    return False
            else:
                actual_xslt_path = XSLT_FILE_PATH
            
            xslt_doc = etree.parse(actual_xslt_path)
            _MATHML_XSLT_TRANSFORM = etree.XSLT(xslt_doc)
            print(f"XSLT transform initialized from {actual_xslt_path}")
            return True
        except Exception as e:
            print(f"Failed to initialize XSLT transform: {e}")
            _MATHML_XSLT_TRANSFORM = "error" # Mark as error to avoid retrying
            return False
    elif _MATHML_XSLT_TRANSFORM == "error":
        return False # Already failed, don't retry
    return True # Already initialized

def _convert_mathml_element_to_latex(math_element_node):
    """Converts an xml.etree.ElementTree.Element representing a MathML <math> tag to a LaTeX string."""
    if not _initialize_xslt_transform() or _MATHML_XSLT_TRANSFORM == "error":
        print("XSLT transform not available for MathML conversion.")
        return "[XSLT_ERROR]"
    try:
        # Debug: Print info about the original element including its tail
        # print(f"--- DEBUG: Original MathML Element (type: {type(math_element_node)}) ---")
        # print(f"    Tag: {math_element_node.tag}, XML ID: {math_element_node.get('id')}, Tail: {repr(math_element_node.tail)}")

        # Create a deep copy to safely manipulate (e.g., clear tail)
        node_copy = copy.deepcopy(math_element_node)
        node_copy.tail = None # Explicitly remove tail from the copy
        
        mathml_string_for_lxml = ET.tostring(node_copy, encoding='unicode', method='xml')
        
        # Standard preprocessing from original script
        mathml_string_for_lxml = mathml_string_for_lxml.replace('<<', '&lt;<').replace('>>', '>&gt;')
        
        # Strip whitespace that might be around the core XML string
        mathml_string_for_lxml = mathml_string_for_lxml.strip()

        # --- Debug: Print the exact string being passed to lxml.fromstring --- 
        # print(f"--- DEBUG: Final string for lxml.fromstring (len: {len(mathml_string_for_lxml)}) ---")
        # print(repr(mathml_string_for_lxml)) 
        # print("--- DEBUG: End of final string for lxml.fromstring ---")
        
        lxml_dom = etree.fromstring(mathml_string_for_lxml.encode('utf-8'))
        
        latex_result_tree = _MATHML_XSLT_TRANSFORM(lxml_dom)
        raw_latex_output = str(latex_result_tree)
        # --- Debug: Print raw XSLT output ---
        # print(f"--- DEBUG: Raw LaTeX from XSLT: {raw_latex_output[:300]} ---")
        
        processed_latex = _postprocess_latex_unicode(raw_latex_output)
        # --- Debug: Print processed LaTeX output ---
        # print(f"--- DEBUG: Processed LaTeX: {processed_latex[:300]} ---")
        return processed_latex

    except Exception as e:
        # The error log now prints the string that was *attempted* to be parsed by lxml
        print(f"Error during XSLT processing. Attempted to parse with lxml:\n{repr(mathml_string_for_lxml)}\nError: {e}")
        print(traceback.format_exc())
        return "[CONVERSION_ERROR]"

def _postprocess_latex_unicode(latex_text_unicode):
    if not latex_text_unicode or latex_text_unicode in ["[XSLT_ERROR]", "[CONVERSION_ERROR]"]:
        return latex_text_unicode 
    
    for utf_char, latex_code in UNICODE_TO_LATEX_MAP.items():
        latex_text_unicode = latex_text_unicode.replace(str(utf_char), str(latex_code))

    latex_text_unicode = latex_text_unicode.replace('\\\\', '\\') 
    latex_text_unicode = re.sub(r'\\textcolor\[rgb\]\{[0-9.,]+\}', '', latex_text_unicode)
    latex_text_unicode = latex_text_unicode.replace('\\ ~\\ ', ' {\\sim} ') 
    latex_text_unicode = re.sub(r'^\$ ', '$', latex_text_unicode)
    latex_text_unicode = latex_text_unicode.replace('{\\ }', '\\ ')
    latex_text_unicode = re.sub(r' \}', '}', latex_text_unicode)
    # Removed: latex_text_unicode = latex_text_unicode.replace('\\n\\[\\n\\t', '$$').replace('\\n\\]', '$$')
    latex_text_unicode = latex_text_unicode.replace('\n', ' ') 
    latex_text_unicode = re.sub(r'\s+', ' ', latex_text_unicode).strip() 
    return latex_text_unicode

# --- End MathML to LaTeX Conversion Utilities ---

# Helper to create a unique node name
def get_unique_node_name(element, prefix="node"):
    elem_id = element.attrib.get('id', str(id(element)))
    tag_name = element.tag
    if '}' in tag_name:
        tag_name = tag_name.split('}', 1)[1]
    return f"{prefix}_{tag_name}_{elem_id}"

def get_full_text_content(element):
    if element is None:
        return ""
    
    parts = []
    tag_local_name = element.tag.split('}',1)[-1] if '}' in element.tag else element.tag

    # For preformat, we want to keep the whitespace more or less as is.
    if tag_local_name == 'preformat':
        # ET.tostring preserves internal tags, which we might not want if they are MathML.
        # A simpler approach for preformat might be to just get all text content recursively but join with newlines.
        # For now, let's try to get its text directly and avoid further recursion into complex tags from here.
        current_text = element.text if element.text else ""
        for child in element: # Get text from children if preformat contains other simple tags
            current_text += get_full_text_content(child) # Simplified recursion
            if child.tail: current_text += child.tail
        return current_text.strip() # Strip outer whitespace only

    if element.text:
        stripped_text = element.text.strip()
        if stripped_text:
            parts.append(stripped_text)

    for child in element:
        if not isinstance(child.tag, str):
            continue 
        child_tag_full = child.tag
        child_local_name = child_tag_full
        child_ns_uri = ""
        if '}' in child_tag_full:
            child_ns_uri, child_local_name = child_tag_full.split('}', 1)
            child_ns_uri = child_ns_uri[1:]
        
        if child_local_name == 'math' and child_ns_uri == MATHML_NS: # Inline <m:math>
            processed_latex = _convert_mathml_element_to_latex(child)
            if processed_latex and not processed_latex.startswith('['): 
                parts.append(processed_latex) 
            else:
                # print(f"Failed conversion for inline math. Processed LaTeX: {processed_latex} \nOriginal Element: {ET.tostring(child, encoding='unicode')}")
                parts.append("[INLINE_MATH_CONV_ERROR]") 
        elif child_ns_uri == MATHML_NS and child_local_name in MATHML_SUB_TAGS:
            pass # These are handled by the parent <m:math> conversion or skipped if orphaned
        elif child_local_name in ABSORB_INLINE_TAGS or child_local_name == 'para': # Absorb para text too
            parts.append(get_full_text_content(child)) 
        elif child_local_name == 'footnote':
            parts.append(f"[FN:{child.attrib.get('id', '')}]") 
        else:
            # Avoid recursing into elements that will form their own major graph nodes
            if child_local_name not in ["section", "example", "figure", "note", "key-concepts", "glossary", "table", "exercise", "solution", "problem", "list", "equation"]:
                 parts.append(get_full_text_content(child))
        
        if child.tail:
            stripped_tail = child.tail.strip()
            if stripped_tail:
                parts.append(stripped_tail)
                
    full_text = " ".join(filter(None, parts))
    return ' '.join(full_text.split())


def add_nodes_edges(graph, element, parent_name=None, parent_tag=None):
    if element is None or not isinstance(element.tag, str):
        return

    full_tag = element.tag
    local_name = full_tag.split('}', 1)[-1] if '}' in full_tag else full_tag
    ns_uri = full_tag.split('}',1)[0][1:] if '}' in full_tag else ""

    # Skip MathML sub-tags here. Top-level <m:math> is handled by get_full_text_content.
    # <equation> tags will handle their own <m:math> children.
    if (ns_uri == MATHML_NS and local_name in MATHML_SUB_TAGS) or \
       (local_name in ABSORB_INLINE_TAGS and parent_tag not in ["metadata", "glossary", "definition"]) or \
       (local_name == 'footnote'):
        return

    element_xml_id = element.attrib.get('id')
    unique_element_name = get_unique_node_name(element, prefix=local_name)

    node_attrs = {'label': local_name, 'tag': local_name, 'graph_node_id': unique_element_name}
    if element_xml_id: node_attrs['id'] = element_xml_id
    # Label is further refined below based on type

    if graph.has_node(unique_element_name):
        if parent_name and not graph.has_edge(parent_name, unique_element_name):
            graph.add_edge(parent_name, unique_element_name)
        return

    # --- Handlers for Major Structural Elements (including equation) ---
    if local_name == "document":
        node_attrs['label'] = "Document"
        graph.add_node(unique_element_name, **node_attrs)
        for child in element: add_nodes_edges(graph, child, unique_element_name, local_name)

    elif local_name == "metadata":
        doc_title_elem = element.find(f'{{{MDML_NS}}}title')
        abstract_elem = element.find(f'{{{MDML_NS}}}abstract')
        node_attrs['label'] = "Metadata"
        if doc_title_elem is not None and doc_title_elem.text:
            node_attrs['document_title'] = doc_title_elem.text.strip()
            node_attrs['label'] += f"\nTitle: {textwrap.shorten(doc_title_elem.text.strip(),25)}"
        if abstract_elem is not None: node_attrs['abstract_text'] = get_full_text_content(abstract_elem)
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)

    elif local_name == "content":
        node_attrs['label'] = "Content"
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)
        for child in element: add_nodes_edges(graph, child, unique_element_name, local_name)

    elif local_name == "section":
        section_class = element.get('class', '')
        node_attrs['section_class'] = section_class
        title_elem = element.find(f'{{{CNXML_NS}}}title')
        section_title = get_full_text_content(title_elem) if title_elem is not None else ""
        
        if not section_title and section_class:
            # Attempt to make a title from class name
            section_title = section_class.replace('-', ' ').title()
        elif not section_title:
            section_title = "Untitled Section"
        
        node_attrs['title'] = section_title
        node_attrs['label'] = f"Section ({section_class or 'default'})\n{textwrap.shorten(section_title, 25)}"
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)

        if section_class == "learning-objectives":
            list_elem = element.find(f'{{{CNXML_NS}}}list')
            if list_elem is not None:
                objectives = [get_full_text_content(item) for item in list_elem.findall(f'{{{CNXML_NS}}}item')]
                graph.nodes[unique_element_name]['objectives_list'] = objectives
            # Children like title already handled or absorbed. No further distinct node recursion for list/item here.
        elif section_class == "practice-perfect":
            for child_exercise in element.findall(f'.//{{{CNXML_NS}}}exercise'): # Find all exercise descendants
                # Create specialized exercise node under this section
                ex_xml_id = child_exercise.attrib.get('id')
                ex_unique_name = get_unique_node_name(child_exercise, prefix="PracticeExercise")
                ex_attrs = {'tag': 'PracticeExerciseItem', 'label': f"Practice Ex.\n({ex_xml_id or id(child_exercise)})", 'graph_node_id': ex_unique_name}
                if ex_xml_id: ex_attrs['id'] = ex_xml_id
                prob = child_exercise.find(f'{{{CNXML_NS}}}problem')
                sol = child_exercise.find(f'{{{CNXML_NS}}}solution')
                if prob is not None: ex_attrs['problem_text'] = get_full_text_content(prob)
                if sol is not None: ex_attrs['solution_text'] = get_full_text_content(sol)
                graph.add_node(ex_unique_name, **ex_attrs)
                graph.add_edge(unique_element_name, ex_unique_name)
            # Process other major children like figures if any, but not paras or absorbed exercises
            for child in element:
                if not isinstance(child.tag, str): continue
                child_ln = child.tag.split('}',1)[-1] if '}' in child.tag else child.tag
                if child_ln == 'figure': add_nodes_edges(graph, child, unique_element_name, local_name)
        else: # Default section processing (includes coreq-skills, or no class)
            for child in element:
                if not isinstance(child.tag, str): continue
                child_local_name_iter = child.tag.split('}', 1)[-1] if '}' in child.tag else child.tag
                if child_local_name_iter != 'title': # title already processed
                    add_nodes_edges(graph, child, unique_element_name, local_name)
    
    elif local_name == "example":
        title_elem = element.find(f'{{{CNXML_NS}}}title') or element.find(f'.//{{{CNXML_NS}}}problem/{{{CNXML_NS}}}title')
        example_title = get_full_text_content(title_elem) if title_elem is not None else f"Example {element_xml_id or id(element)}"
        node_attrs['title'] = example_title
        node_attrs['label'] = f"Example\n{textwrap.shorten(example_title, 25)}"
        problem_elem = element.find(f'.//{{{CNXML_NS}}}problem')
        if problem_elem is not None: node_attrs['problem_text'] = get_full_text_content(problem_elem)
        solution_elem = element.find(f'.//{{{CNXML_NS}}}solution')
        if solution_elem is not None: node_attrs['solution_text'] = get_full_text_content(solution_elem)
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)
        for child in element:
            child_local_name_iter = child.tag.split('}', 1)[-1] if '}' in child.tag else child.tag
            if child_local_name_iter in ["figure", "note"] :
                add_nodes_edges(graph, child, unique_element_name, local_name)

    elif local_name == "note":
        note_class = element.get("class", "")
        title_elem = element.find(f'{{{CNXML_NS}}}title')
        note_title = get_full_text_content(title_elem) if title_elem is not None else ""
        node_attrs['title'] = note_title
        node_attrs['note_class'] = note_class
        label_prefix = "Note"
        if "qa" in note_class: 
            label_prefix = "Q&A"
            paras = [p for p in element if isinstance(p.tag, str) and (p.tag.split('}', 1)[-1] if '}' in p.tag else p.tag) == 'para']
            if paras and len(paras) >=1 :
                 node_attrs['question'] = get_full_text_content(paras[0])
                 if len(paras) > 1: node_attrs['answer'] = " ".join([get_full_text_content(p) for p in paras[1:]])
        elif "try" in note_class:
            label_prefix = "Try It"
            ex_elem = element.find(f'{{{CNXML_NS}}}exercise') 
            if ex_elem is not None:
                prob_elem = ex_elem.find(f'{{{CNXML_NS}}}problem')
                sol_elem = ex_elem.find(f'{{{CNXML_NS}}}solution')
                if prob_elem is not None: node_attrs['problem_text'] = get_full_text_content(prob_elem)
                if sol_elem is not None: node_attrs['solution_text'] = get_full_text_content(sol_elem)
            else: 
                 node_attrs['content'] = get_full_text_content(element)
        elif "how-to" in note_class: 
            label_prefix = "How To"
            node_attrs['content'] = get_full_text_content(element)
        elif title_elem is not None and note_title: 
            label_prefix = f"DefNote: {textwrap.shorten(note_title, 15)}"
            node_attrs['content'] = get_full_text_content(element)
        else: 
            node_attrs['content'] = get_full_text_content(element)
        node_attrs['label'] = f"{label_prefix} ({note_class})\n{textwrap.shorten(note_title if note_title else (element_xml_id or 'NoID'), 20)}"
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)
        for child in element:
            if not isinstance(child.tag, str): continue
            if (child.tag.split('}', 1)[-1] if '}' in child.tag else child.tag) == "figure": 
                add_nodes_edges(graph, child, unique_element_name, local_name)
        if "how-to" in note_class:
            for list_child in element.findall(f'{{{CNXML_NS}}}list'):
                add_nodes_edges(graph, list_child, unique_element_name, local_name)

    elif local_name == "figure":
        node_attrs['label'] = f"Figure\n(ID: {element_xml_id if element_xml_id else 'NoID'})"
        caption_elem = element.find(f'{{{CNXML_NS}}}caption')
        if caption_elem is not None: node_attrs['caption_text'] = get_full_text_content(caption_elem)
        media_elem = element.find(f'{{{CNXML_NS}}}media')
        if media_elem is not None:
            node_attrs['media_xml_content'] = ET.tostring(media_elem, encoding='unicode').strip()
            image_elem = media_elem.find(f'{{{CNXML_NS}}}image')
            if image_elem is not None and 'src' in image_elem.attrib:
                node_attrs['image_src'] = image_elem.attrib['src']
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)

    elif local_name == "key-concepts":
        node_attrs['label'] = "Key Concepts"
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)
        list_elem = element.find(f'{{{CNXML_NS}}}list')
        if list_elem is not None:
            for i, item_elem in enumerate(list_elem.findall(f'{{{CNXML_NS}}}item')):
                item_text = get_full_text_content(item_elem)
                item_xml_id = item_elem.attrib.get('id')
                item_node_name = get_unique_node_name(item_elem, prefix=f"KC_item{i}")
                kc_item_attrs = {'tag': 'KeyConceptItem', 'label':f"KC: {textwrap.shorten(item_text, 25)}", 'text_content':item_text, 'graph_node_id': item_node_name}
                if item_xml_id: kc_item_attrs['id'] = item_xml_id
                graph.add_node(item_node_name, **kc_item_attrs)
                graph.add_edge(unique_element_name, item_node_name)

    elif local_name == "glossary":
        node_attrs['label'] = "Glossary"
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)
        for def_elem in element.findall(f'{{{CNXML_NS}}}definition'):
            term_elem = def_elem.find(f'{{{CNXML_NS}}}term')
            meaning_elem = def_elem.find(f'{{{CNXML_NS}}}meaning')
            if term_elem is not None and meaning_elem is not None:
                term_text = get_full_text_content(term_elem)
                meaning_text = get_full_text_content(meaning_elem)
                def_xml_id = def_elem.attrib.get('id')
                def_node_name = get_unique_node_name(def_elem, prefix="GlossDef")
                gloss_attrs = {'tag':'GlossaryDefinition', 'label':f"Term: {textwrap.shorten(term_text, 20)}", 'term_text':term_text, 'meaning_text':meaning_text, 'graph_node_id': def_node_name}
                if def_xml_id: gloss_attrs['id'] = def_xml_id
                graph.add_node(def_node_name, **gloss_attrs)
                graph.add_edge(unique_element_name, def_node_name)
    
    elif local_name == "section-exercises" or (local_name == "section" and parent_tag == "section-exercises"):
        if local_name == "section-exercises":
            node_attrs['label'] = "Section Exercises Group"
        else: 
            title_elem = element.find(f'{{{CNXML_NS}}}title')
            sub_ex_title = get_full_text_content(title_elem) if title_elem is not None else local_name.title()
            node_attrs['title'] = sub_ex_title
            node_attrs['label'] = f"ExGroup: {sub_ex_title}"

        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)
        for child in element: 
            if not isinstance(child.tag, str): continue
            child_ln_iter = child.tag.split('}',1)[-1] if '}' in child.tag else child.tag
            if child_ln_iter == 'exercise' or child_ln_iter == 'section': 
                add_nodes_edges(graph, child, unique_element_name, local_name) 
            elif child_ln_iter == 'title' and local_name == "section": 
                pass 
            elif child_ln_iter == 'para' : 
                 add_nodes_edges(graph, child, unique_element_name, local_name)

    elif local_name == "exercise" and (parent_tag == "section-exercises" or \
                                        (parent_tag == "section" and graph.nodes[parent_name].get('tag') == "section-exercises") or \
                                        (parent_tag == "section" and graph.nodes[parent_name].get('section_class','').endswith("-exercises")) or 
                                        (parent_tag == "section" and graph.nodes[parent_name].get('section_class') == "practice-perfect")):
        ex_label_prefix = "Exercise Item"
        ex_tag = "ExerciseItem"
        if parent_tag == "section" and graph.nodes[parent_name].get('section_class') == "practice-perfect":
            ex_label_prefix = "Practice Ex."
            ex_tag = "PracticeExerciseItem"

        node_attrs['label'] = f"{ex_label_prefix}\n(ID: {element_xml_id or id(element)})"
        node_attrs['tag'] = ex_tag 
        problem_elem = element.find(f'{{{CNXML_NS}}}problem')
        if problem_elem is not None: node_attrs['problem_text'] = get_full_text_content(problem_elem)
        solution_elem = element.find(f'{{{CNXML_NS}}}solution')
        if solution_elem is not None: node_attrs['solution_text'] = get_full_text_content(solution_elem)
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)
        for fig_child in element.findall(f'.//{{{CNXML_NS}}}figure'): 
            add_nodes_edges(graph, fig_child, unique_element_name, local_name)

    elif local_name == "equation":
        node_attrs['tag'] = "equation" 
        node_attrs['label'] = f"Equation\n(ID: {element_xml_id or id(element)})"
        # Find m:math or math (unprefixed, though less common in strict CNXML)
        math_elem = element.find(f'{{{MATHML_NS}}}math') 
        if math_elem is None: 
            math_elem = element.find('math')

        if math_elem is not None:
            processed_latex = _convert_mathml_element_to_latex(math_elem)
            if processed_latex and not processed_latex.startswith('['): 
                node_attrs['latex_content'] = processed_latex 
            else:
                # print(f"Failed conversion for block equation. Processed LaTeX: {processed_latex} \nOriginal Element: {ET.tostring(math_elem, encoding='unicode')}")
                node_attrs['latex_content'] = "[BLOCK_MATH_CONV_ERROR]"
                node_attrs['original_mathml'] = ET.tostring(math_elem, encoding='unicode', method='xml')
        else:
            node_attrs['latex_content'] = "[MATH_CONTENT_NOT_FOUND_IN_EQUATION]"

        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)
        for child in element:
            if not isinstance(child.tag, str): continue
            child_ln_iter = child.tag.split('}',1)[-1] if '}' in child.tag else child.tag
            is_mathml_math_tag = (child.tag.startswith(f'{{{MATHML_NS}}}') and child_ln_iter == 'math') or \
                                 (child_ln_iter == 'math' and not child.tag.startswith('{'))
            if not is_mathml_math_tag:
                 add_nodes_edges(graph, child, unique_element_name, local_name)

    elif local_name in ["para", "title", "abstract", "definition", "problem", "solution", "caption", "item"]:
        text_content = get_full_text_content(element)
        # Default label construction, including ID
        base_label = f"{local_name}\n(ID: {element_xml_id or id(element)})"
        if text_content: 
            node_attrs['text_content'] = text_content
            # For Matplotlib labels, escape $ if we don't want mathtext interpretation here
            safe_text_for_label = text_content.replace('$', '\\$')
            node_attrs['label'] = f"{local_name}\n({textwrap.shorten(safe_text_for_label, 20)})"
        else:
            node_attrs['label'] = base_label # Use if no text_content
        
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)
        for child in element:
            if not isinstance(child.tag, str): continue
            child_local_name_iter = child.tag.split('}', 1)[-1] if '}' in child.tag else child.tag
            if child_local_name_iter in ["figure", "example", "note", "list", "table", "equation"]:
                add_nodes_edges(graph, child, unique_element_name, local_name)
    
    elif local_name == "list":
        text_content = get_full_text_content(element) 
        node_attrs['text_content'] = text_content 
        safe_text_for_label = text_content.replace('$', '\\$') if text_content else ""
        node_attrs['label'] = f"List ({element.attrib.get('list-type', 'bulleted')})\n({textwrap.shorten(safe_text_for_label, 15)} ID: {element_xml_id or id(element)})"
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)
        for item_child in element.findall(f'{{{CNXML_NS}}}item'): 
            add_nodes_edges(graph, item_child, unique_element_name, local_name)
        for other_child in element:
            if not isinstance(other_child.tag, str): continue
            child_ln = other_child.tag.split('}',1)[-1] if '}' in other_child.tag else other_child.tag
            if child_ln != 'item' and child_ln in ["figure", "note", "equation"]:
                 add_nodes_edges(graph, other_child, unique_element_name, local_name)

    elif local_name == "table":
        node_attrs['label'] = f"Table\n(ID: {element_xml_id or 'NoID'})"
        node_attrs['xml_content'] = ET.tostring(element, encoding='unicode').strip()
        graph.add_node(unique_element_name, **node_attrs)
        if parent_name: graph.add_edge(parent_name, unique_element_name)

    else: 
        if not graph.has_node(unique_element_name):
            text_content = get_full_text_content(element) 
            safe_text_for_label = text_content.replace('$', '\\$') if text_content else ""
            label_detail = textwrap.shorten(safe_text_for_label if safe_text_for_label else (element_xml_id or '?'), 20)
            node_attrs['label'] = f"{local_name}\n({label_detail})"
            if text_content: 
                node_attrs['text_content'] = text_content
            graph.add_node(unique_element_name, **node_attrs)
            if parent_name: graph.add_edge(parent_name, unique_element_name)
            for child in element:
                add_nodes_edges(graph, child, unique_element_name, local_name)

def get_node_by_xml_id(graph, xml_id):
    for node, data in graph.nodes(data=True):
        if data.get('id') == xml_id:
            return node
    return None

def get_structured_content(graph, start_node_id):
    if not graph.has_node(start_node_id):
        return {"error": "Start node not found in graph"}

    start_node_data = graph.nodes[start_node_id]
    content_piece = {
        "graph_node_id": start_node_id,
        "type": start_node_data.get('tag'),
        "id_attribute": start_node_data.get('id'),
        "title": start_node_data.get('title')
    }
    if 'section_class' in start_node_data:
        content_piece['section_class'] = start_node_data['section_class']
    if 'objectives_list' in start_node_data:
        content_piece['objectives_list'] = start_node_data['objectives_list']

    direct_attrs = [
        'text_content', 'problem_text', 'solution_text', 'caption_text', 
        'image_src', 'media_xml_content', 'question', 'answer', 
        'note_class', 'term_text', 'meaning_text', 'document_title', 'abstract_text',
        'xml_content', 'latex_content', 'original_mathml' 
    ]
    for attr in direct_attrs:
        if attr in start_node_data:
            content_piece[attr] = start_node_data[attr]
    
    child_collection_map = {
        'para': 'direct_text_blocks',
        'example': 'examples',
        'figure': 'figures',
        'note': 'notes',
        'KeyConceptItem': 'key_concept_items',
        'GlossaryDefinition': 'glossary_definitions',
        'ExerciseItem': 'exercise_items',
        'PracticeExerciseItem': 'practice_exercises',
        'table': 'tables',
        'list': 'lists',
        'section': 'sub_sections',
        'item': 'items', 
        'equation': 'equations' 
    }
    for key in child_collection_map.values():
        if key not in content_piece: 
            content_piece[key] = []

    if start_node_id in graph:
        for child_node_id in graph.successors(start_node_id):
            if not graph.has_node(child_node_id): continue 
            child_data = graph.nodes[child_node_id]
            child_tag = child_data.get('tag')

            processed_as_specific_child = False
            for specific_tag, list_key in child_collection_map.items():
                if child_tag == specific_tag:
                    if list_key == 'direct_text_blocks': 
                        content_piece[list_key].append({
                            "type": "paragraph",
                            "graph_node_id": child_node_id,
                            "id_attribute": child_data.get('id'),
                            "text": child_data.get('text_content', '')
                        })
                    elif list_key == 'equations':
                        equation_data = {
                            "graph_node_id": child_node_id,
                            "type": "equation",
                            "id_attribute": child_data.get('id'),
                            "latex_content": child_data.get('latex_content'),
                            "original_mathml": child_data.get('original_mathml')
                        }
                        content_piece[list_key].append(equation_data)
                    else:
                        structured_child = get_structured_content(graph, child_node_id)
                        content_piece[list_key].append(structured_child)
                    processed_as_specific_child = True
                    break
            
            if not processed_as_specific_child:
                if 'generic_children_content' not in content_piece:
                    content_piece['generic_children_content'] = []
                child_simple_struct = {
                    "graph_node_id": child_node_id,
                    "type": child_tag,
                    "id_attribute": child_data.get('id'),
                    "label": child_data.get('label'),
                    "text_content": child_data.get('text_content') 
                }
                if child_tag == 'equation' and 'latex_content' in child_data:
                    child_simple_struct['latex_content'] = child_data['latex_content']

                content_piece['generic_children_content'].append(child_simple_struct)
                
    return content_piece

def print_content_schema():
    schema_explanation = """
    Conceptual Schema for Queried Content (JSON Output):

    The output is a single JSON object representing the queried content piece.

    Common fields for all content pieces:
    - graph_node_id: (string) Unique identifier of the node in the NetworkX graph.
    - type: (string) The CNXML tag name or a derived type (e.g., 'section', 'Example', 'KeyConceptItem').
    - id_attribute: (string|null) The original 'id' attribute from the CNXML, if present.
    - title: (string|null) The title of the element, if applicable.

    Type-specific fields and nested structures (examples):

    If 'type' is 'document':
    - metadata: (object) Content of the <metadata> node.
    - content: (object) Structured content of the <content> node.
    - glossary: (object) Structured content of a top-level <glossary> if present.

    If 'type' is 'section':
    - section_class: (string|null) The 'class' attribute of the section.
    - objectives_list: (array of strings) For 'learning-objectives' sections.
    - direct_text_blocks: (array of objects) {"type":"paragraph", "text":"...", ...}. (Paragraph text may now contain $inline_latex$)
    - examples: (array of example objects)
    - figures: (array of figure objects)
    - notes: (array of note objects)
    - equations: (array of equation objects) <--- NEW
    - key_concept_items: (array of key_concept_item objects)
    - glossary_definitions: (array of glossary_definition objects)
    - exercise_items: (array of ExerciseItem objects)
    - practice_exercises: (array of PracticeExerciseItem objects)
    - tables: (array of table objects)
    - lists: (array of list objects)
    - sub_sections: (array of section objects) For nested sections.
    - generic_children_content: (array) For other direct children.

    If 'type' is 'equation': <--- NEW
    - latex_content: (string) The block LaTeX representation (e.g., $$...$$ or \\[...\\] from XSLT).
    - original_mathml: (string|null) The original MathML if conversion failed.

    If 'type' is 'example': (Problem/Solution text may now contain $inline_latex$)
    - problem_text: (string)
    - solution_text: (string)
    - figures: (array of figure objects)
    - notes: (array of note objects)
    - equations: (array of equation objects)

    If 'type' is 'note': (Content/question/answer may now contain $inline_latex$)
    - note_class: (string)
    - question: (string) For 'qa' notes.
    - answer: (string) For 'qa' notes.
    - problem_text: (string) For 'try' notes.
    - content: (string) For general notes or as fallback.
    - figures: (array of figure objects)
    - lists: (array of list objects)
    - equations: (array of equation objects)

    If 'type' is 'KeyConceptItem', 'GlossaryDefinition', 'ExerciseItem', 'PracticeExerciseItem', 'table', 'item':
    - Relevant text fields (like 'text_content', 'term_text', etc.) may now contain $inline_latex$.
    - For 'table', 'xml_content' remains raw XML.

    If 'type' is 'list':
    - text_content: (string|null) Direct text which may contain $inline_latex$.
    - items: (array of item objects, whose text_content may contain $inline_latex$)

    This schema is representative. The exact fields depend on the queried element and its children.
    """
    print(schema_explanation)

def visualize_cnxml_as_graph(filepath, query_start_id=None, output_json_path="queried_content.json", output_gexf_path="graph_output.gexf"):
    """
    Parses a CNXML file, visualizes its structure, and optionally queries a part of it.
    Also saves the graph to a GEXF file.
    """
    if not _initialize_xslt_transform():
        print("Halting due to XSLT initialization failure.")
        return
        
    try:
        ET.register_namespace('', CNXML_NS)
        ET.register_namespace('m', MATHML_NS)
        ET.register_namespace('md', MDML_NS)
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
        return
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return

    G = nx.DiGraph()
    add_nodes_edges(G, root)

    if not G.nodes():
        print("Graph is empty. No nodes were created.")
        return

    for node_id, data in G.nodes(data=True):
        if 'objectives_list' in data and isinstance(data['objectives_list'], list):
            data['objectives_list'] = json.dumps(data['objectives_list'])

    try:
        nx.write_gexf(G, output_gexf_path)
        print(f"Graph saved to GEXF format at {output_gexf_path}")
    except Exception as e_gexf:
        print(f"Error writing GEXF file: {e_gexf}")

    queried_node_graph_id = None
    if query_start_id:
        queried_node_graph_id = get_node_by_xml_id(G, query_start_id)
        if not queried_node_graph_id:
            print(f"Could not find a node with XML ID: {query_start_id}. Trying to find document root for query.")
    
    if not queried_node_graph_id: 
        for node, data in G.nodes(data=True):
            if data.get('tag') == 'document':
                queried_node_graph_id = node
                query_start_id = data.get('id', 'document_root') 
                print(f"Querying from document root (Graph node: {queried_node_graph_id}).")
                break
    
    if queried_node_graph_id:
        print(f"\nAttempting to query content starting from: {query_start_id} (Graph node: {queried_node_graph_id})")
        structured_data = get_structured_content(G, queried_node_graph_id)
        try:
            with open(output_json_path, 'w', encoding='utf-8') as f:
                json.dump(structured_data, f, ensure_ascii=False, indent=2)
            print(f"Structured content for '{query_start_id}' saved to {output_json_path}")
        except Exception as e_json:
            print(f"Error writing JSON file: {e_json}")
    else:
        print("Could not find a starting node for query (specific ID or document root).")

    plt.figure(figsize=(40, 40)) 
    
    try:
        pos = nx.nx_agraph.graphviz_layout(G, prog="dot", args="-Grankdir=TB -Gnodesep=0.75 -Grandsep=2.0") 
    except ImportError:
        print("Graphviz layout (prog='dot') not available. Install pygraphviz or pydot.")
        print("Falling back to spring_layout, which might not show hierarchy well.")
        pos = nx.spring_layout(G, k=1.5/((len(G.nodes())**0.5) or 1), iterations=30, seed=123) 
    except Exception as e_layout: 
        print(f"Graphviz layout error ({e_layout}). Falling back to spring_layout.")
        pos = nx.spring_layout(G, k=1.5/((len(G.nodes())**0.5) or 1), iterations=30, seed=123)

    node_labels = {node: data.get('label', node.split('_')[0]) for node, data in G.nodes(data=True)}
    node_sizes = [2000 + G.degree(node) * 75 for node in G.nodes()] 
    
    nx.draw(G, pos, labels=node_labels, with_labels=True, node_size=node_sizes, node_color="skyblue", 
            font_size=7, font_weight="normal", arrows=True, arrowstyle='-|>', arrowsize=10,
            width=1.0, edge_color='#777777')

    plt.title(f"CNXML Structure Graph: {filepath}", size=20)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        cnxml_file_path = sys.argv[1]
        query_id = None 
        json_path = "queried_content.json" 
        gexf_path = "graph_output.gexf"    

        if len(sys.argv) > 2:
            query_id = sys.argv[2]
            print(f"Received query_id for content extraction: {query_id}")
        else:
            print("No specific XML ID provided for query, will attempt to query from document root.")
        
        if len(sys.argv) > 3:
            json_path = sys.argv[3]
            print(f"Using custom JSON output path: {json_path}")

        if len(sys.argv) > 4:
            gexf_path = sys.argv[4]
            print(f"Using custom GEXF output path: {gexf_path}")

        visualize_cnxml_as_graph(cnxml_file_path, query_start_id=query_id, output_json_path=json_path, output_gexf_path=gexf_path)
    else:
        print("Please provide the path to the CNXML file as a command-line argument.")
        print("Optionally, provide an XML ID of a section/element to query as a second argument.")
        print("Optionally, provide a custom JSON output path as a third argument.")
        print("Optionally, provide a custom GEXF output path as a fourth argument.")
        print("Example: python cnxml_to_graph.py modules/m49304/index.cnxml")
        print("Example query: python cnxml_to_graph.py modules/m49304/index.cnxml fs-id1165135193832")
        print("Example with custom paths: python cnxml_to_graph.py modules/m49304/index.cnxml fs-id1165135193832 output/my_content.json output/my_graph.gexf") 