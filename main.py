#!/usr/bin/env python3
"""
Convert a single OpenStax book (given its *.collection.xml) to
GitHub‑flavoured Markdown with LaTeX maths – **without needing Pandoc**.

Dependencies
------------
    pip install lxml 
    (mathml2latex is now vendored)
Usage
-----
    python main.py collections/college-algebra-corequisite-support-2e.collection.xml \
                       --out md_algebra
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any
import copy

from lxml import etree

# --- Add vendored library to path ---
# This makes Python look for modules in our vendor/mathml2latex_bowang directory
_MAIN_PY_DIR = Path(__file__).parent.resolve()
VENDOR_DIR_BOWANG = _MAIN_PY_DIR / "vendor" / "mathml2latex_bowang"

if not VENDOR_DIR_BOWANG.is_dir():
    sys.exit(
        f"❌ Vendored library directory not found: {VENDOR_DIR_BOWANG}\n"
        "    Please clone it: git clone https://github.com/bowang/mathml2latex.git vendor/mathml2latex_bowang"
    )
# Ensure the vendor directory itself is in the path so 'import mathml2latex' finds the .py file
if str(VENDOR_DIR_BOWANG) not in sys.path:
    sys.path.insert(0, str(VENDOR_DIR_BOWANG))
# Also ensure the parent vendor dir is in path if unicode_map needs relative import, although direct import should work
# VENDOR_PARENT_DIR = VENDOR_DIR_BOWANG.parent
# if str(VENDOR_PARENT_DIR) not in sys.path:
#     sys.path.insert(0, str(VENDOR_PARENT_DIR))


# ------------------------------------------------------------------ 3rd‑party -
try:
    # Import the script file directly as a module
    import mathml2latex as mml_bowang 
except ImportError as e:
    sys.exit(
        f"❌ Failed to import from vendored mathml2latex_bowang library. Error: {e}\n"
        f"    Ensure it's correctly placed in {VENDOR_DIR_BOWANG} and the directory is in sys.path."
    )
except Exception as e: # Catch any other unexpected import errors
    sys.exit(f"❌ An unexpected error occurred during mathml2latex_bowang import: {e}")


# ------------------------------------------------------------------- helpers ---
def log(msg: str) -> None:
    print("[cnxml2md]", msg)


def mathml_to_tex(math_el: etree.Element, source_file_path: Path | None = None) -> str:
    """Convert a single <math> element to LaTeX, using the vendored bowang/mathml2latex library."""
    
    # --- Debug Flag for specific file ---
    DEBUG_THIS_FILE = source_file_path is not None and "m51239" in source_file_path.name
    # ---

    try:
        math_el_copy = copy.deepcopy(math_el)
    except Exception as e: 
        log(f"⚠︎ Error deepcopying MathML element: {e}")
        return etree.tostring(math_el, method="text", encoding="unicode").strip() 
        
    math_el_copy.tail = None 

    xml_string = etree.tostring(math_el_copy, encoding="unicode")

    if not xml_string.strip():
        return ""

    final_latex = "" # Initialize to empty
    try:
        xslt_result_obj = mml_bowang.mathml2latex(xml_string) 
        final_latex = mml_bowang.unicode2latex(xslt_result_obj)

        # --- Debug Print for specific file ---
        if DEBUG_THIS_FILE:
            print(f"\n--- DEBUG m51239 ---")
            print(f"Input MathML:\n{xml_string}")
            print(f"Output LaTeX:\n'{final_latex}'") 
            print(f"--------------------\n")
        # ---

        return final_latex.strip()
        
    except Exception as exc:  
        log(f"⚠︎ MathML→TeX conversion error (bowang library) ({type(exc).__name__}: {exc}) for input: {xml_string[:200]}...")
        # import traceback # Uncomment for full traceback during debugging
        # traceback.print_exc() # Uncomment for full traceback during debugging
        return etree.tostring(math_el, method="text", encoding="unicode").strip()


# ----------------------------------------------------------- element renderers -
def underline(txt: str, ch: str = "=") -> str:
    return f"\n{txt}\n{ch * len(txt)}\n"


def r_para(el):   return etree.tostring(el, method='text', encoding='unicode').strip() + "\n"
def r_em(el):     return f"*{etree.tostring(el, method='text', encoding='unicode').strip()}*"
def r_term(el):   
    # Check parent exists before accessing tag
    parent = el.getparent()
    parent_tag = parent.tag if parent is not None else ""
    return "" if parent_tag.endswith("DEFINITION") else f"**{etree.tostring(el, method='text', encoding='unicode').strip()}**"
def r_title(el):
    txt = etree.tostring(el, method='text', encoding='unicode').strip()
    parent = el.getparent()
    parent_tag = parent.tag if parent is not None else ""
    return f"\n## {txt}\n" if parent_tag.endswith("SECTION") else underline(txt)


def r_fig(el):
    subs = el.findall(".//subfigure")
    out: list[str] = []
    if subs:
        for sf in subs:
            alt_node = sf.find(".//media")
            alt = alt_node.get("alt", "") if alt_node is not None else ""
            src_node = sf.find(".//image")
            src = src_node.get("src") if src_node is not None else "MISSING_SRC"
            out.append(f"![{alt}]({src})")
        cap_node = el.find(".//caption")
        if cap_node is not None and cap_node.text is not None:
            out.append(f"\n*{cap_node.text.strip()}*\n")
    else:
        cap_node = el.find(".//caption")
        cap = (cap_node.text.strip() or "") if cap_node is not None and cap_node.text is not None else ""
        src_node = el.find(".//image")
        src = src_node.get("src") if src_node is not None else "MISSING_SRC"
        out.append(f"\n\n![{cap}]({src})\n\n")
    return "\n\n".join(out)


def r_math(el, source_file_path: Path | None = None):
    # Get the LaTeX conversion attempt (could be fallback text or empty)
    tex = mathml_to_tex(el, source_file_path=source_file_path)
    
    # Get the original MathML source for debugging
    try:
        original_mathml = etree.tostring(el, encoding='unicode', pretty_print=True).strip()
    except Exception:
        original_mathml = "Error serializing original MathML"

    # Determine the LaTeX output part (inline, block, or placeholder)
    latex_part = ""
    if tex and tex.strip():
        # Heuristic: block maths usually start with \begin{...} or \[ or $$
        if tex.startswith("\\begin") or tex.startswith("\\[") or tex.startswith("$$"):
            clean_tex = tex.strip()
            if clean_tex.startswith("$$") and clean_tex.endswith("$$"):
                 clean_tex = clean_tex[2:-2].strip()
            elif clean_tex.startswith("\\[") and clean_tex.endswith("\\]"):
                 clean_tex = clean_tex[2:-2].strip()
            latex_part = f"\n\n$$\n{clean_tex}\n$$\n\n"
        else: # Inline math
            latex_part = f"${tex}$"
    else:
        # Use fallback text if conversion failed and produced nothing
        fallback_text = etree.tostring(el, method="text", encoding="unicode").strip()
        if fallback_text:
             latex_part = f"*[MathML fallback: {fallback_text}]*" # Italicize fallback
        else: 
             latex_part = "*[MathML conversion failed]*" # Placeholder if empty

    # Construct the final Markdown output with the <details> block
    output = f'''{latex_part}

<details>
<summary>Original MathML Source</summary>

```xml
{original_mathml}
```

</details>

'''
    
    return output


RENDER: dict[str, Any] = {} # Define RENDER before r_math uses it

def render(node, source_file_path: Path | None = None):
    if isinstance(node, etree._ElementUnicodeResult):
        return str(node)

    if not isinstance(node.tag, str):
        return ""

    for child in list(node):
        rep = render(child, source_file_path=source_file_path)
        if rep:
            # Escape potential markdown/HTML comment sequences within the rendered text
            safe = rep.replace("--", "—").replace("<!", "&lt;!").replace("-->", "—&gt;") 
            if safe.endswith("-"):
                safe += " "
            
            parent = child.getparent()
            if parent is not None:
                 # Use lxml Comment factory
                 parent.replace(child, etree.Comment(safe)) 

    tag_name = node.tag
    # Special handling for MATH tags to pass the path
    if tag_name == "MATH" or tag_name == "{http://www.w3.org/1998/Math/MathML}math":
        fn = RENDER.get(tag_name)
        return fn(node, source_file_path=source_file_path) if fn else ""
    else:
        # Regular lookup for other tags
        fn = RENDER.get(tag_name)
        if not fn and '}' in tag_name:
            fn = RENDER.get(tag_name.split("}")[-1])
        # Call other renderers without the path argument if they don't need it
        return fn(node) if fn else ""


def convert_cnxml(cnxml: Path) -> str:
    log(f"   • parse {cnxml}")
    parser = etree.XMLParser(recover=True, no_network=True) # Add no_network=True for security
    try:
        doc = etree.parse(str(cnxml), parser)
    except etree.XMLSyntaxError as e:
        log(f"⚠︎ XML Syntax Error parsing {cnxml}: {e}")
        return f"Error parsing {cnxml.name}: XML Syntax Error.\n"
    except Exception as e: # Catch other parsing errors
        log(f"⚠︎ Error parsing {cnxml}: {type(e).__name__}: {e}")
        return f"Error parsing {cnxml.name}: {type(e).__name__}.\n"

    # Pass the path to render
    render(doc.getroot(), source_file_path=cnxml)
    # Method 'text' preserves whitespace better, consider 'html' if structure is needed?
    # For Markdown, 'text' is likely correct.
    try:
        txt = etree.tostring(doc, method="text", encoding="unicode")
    except Exception as e:
        log(f"⚠︎ Error serializing text from processed tree for {cnxml}: {e}")
        return f"Error serializing text for {cnxml.name}.\\n"
        
    # Collapse 2 or more newlines into just 2, then strip leading/trailing whitespace
    txt = re.sub(r"\n{2,}", "\n\n", txt).strip() 
    return txt + "\n"


# ---------------------------------------- locate modules from *.collection.xml -
def modules_from_collection(coll: Path) -> list[Path]:
    tree = etree.parse(str(coll))
    root = tree.getroot()
    ns = {'c': root.nsmap.get(None) or "http://cnx.rice.edu/collxml"}

    modules: list[Path] = []
    for mod_el in tree.xpath("//*[local-name()='module'][@document]"):
        uuid = mod_el.get("document")
        if uuid:
            module_path = coll.parent.parent / "modules" / uuid / "index.cnxml"
            modules.append(module_path)
    if not modules:
        for mod_el in tree.findall(".//module[@document]"):
            uuid = mod_el.get("document")
            if uuid:
                 module_path = coll.parent.parent / "modules" / uuid / "index.cnxml"
                 modules.append(module_path)
    return modules


# ----------------------------------------------------------- CLI entry point --
def main() -> None:
    p = argparse.ArgumentParser(description="Convert OpenStax CNXML to Markdown with LaTeX math (using vendored bowang/mathml2latex).")
    p.add_argument("collection", help="path to *.collection.xml")
    p.add_argument("--out", default="md-out", help="output directory")
    args = p.parse_args()

    coll_path = Path(args.collection).resolve()
    if not coll_path.is_file():
        sys.exit(f"❌ Collection file not found: {coll_path}")

    log(f"Reading {coll_path}")
    modules = modules_from_collection(coll_path)
    if not modules:
        sys.exit("❌ 0 module entries found in collection. Check XML structure, namespaces, or pathing.")

    log(f"Found {len(modules)} modules to process.")
    out_root = Path(args.out).resolve()
    out_root.mkdir(parents=True, exist_ok=True)
    bundle_root = coll_path.parent.parent 

    for m_path in modules:
        if not m_path.exists():
            log(f"⚠︎ Module CNXML file missing: {m_path.relative_to(bundle_root)}")
            continue
        
        log(f"Processing module: {m_path.relative_to(bundle_root)}")
        md_text = convert_cnxml(m_path)
        
        try:
            rel_path_for_md = m_path.relative_to(bundle_root / "modules")
            dest = out_root / "modules" / rel_path_for_md.with_suffix(".md")
        except ValueError:
            log(f"⚠︎ Could not determine relative path for {m_path}. Using fallback naming.")
            dest = out_root / (m_path.parent.name + "_" + m_path.name).replace(".cnxml",".md")

        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            dest.write_text(md_text, encoding="utf-8")
            log(f"✔︎ wrote {dest.relative_to(out_root)} ({len(md_text)} bytes)")
        except Exception as e:
            log(f"❌ Error writing file {dest}: {e}")


if __name__ == "__main__":
    main()
