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
import shutil

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
        #print("xslt_result_obj:\n\n",xslt_result_obj)
        final_latex = mml_bowang.unicode2latex(xslt_result_obj)
        #print("final_latex:\n\n",final_latex)
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
# Forward declaration for the main render function, as RENDER handlers might call it.
def render(node, source_file_path: Path | None = None, include_mathml_source: bool = False) -> str:
    pass # Actual definition will be below RENDER handlers

# Global RENDER dictionary
RENDER: dict[str, Any] = {}

def underline(txt: str, ch: str = "=") -> str:
    return f"\n{txt}\n{ch * len(txt)}\n"

# --- NEW/MODIFIED RENDER HANDLERS ---
def r_para_new(el, source_file_path: Path | None = None, include_mathml_source: bool = False):
    parts = []
    if el.text: parts.append(el.text)
    for child in el:
        parts.append(render(child, source_file_path=source_file_path, include_mathml_source=include_mathml_source))
        if child.tail: parts.append(child.tail)
    return "".join(parts).strip() + "\n"

def r_em_new(el, source_file_path: Path | None = None, include_mathml_source: bool = False):
    parts = []
    if el.text: parts.append(el.text)
    for child in el:
        parts.append(render(child, source_file_path=source_file_path, include_mathml_source=include_mathml_source))
        if child.tail: parts.append(child.tail)
    return f'*{"".join(parts).strip()}*'

def r_term_new(el, source_file_path: Path | None = None, include_mathml_source: bool = False):
    parts = []
    if el.text: parts.append(el.text)
    for child in el:
        parts.append(render(child, source_file_path=source_file_path, include_mathml_source=include_mathml_source))
        if child.tail: parts.append(child.tail)
    
    parent = el.getparent()
    parent_tag = parent.tag if parent is not None else ""
    text_content = "".join(parts).strip()
    return "" if parent_tag.endswith("DEFINITION") else f"**{text_content}**"
    
def r_title_new(el, source_file_path: Path | None = None, include_mathml_source: bool = False):
    parts = []
    if el.text: parts.append(el.text)
    for child in el:
        parts.append(render(child, source_file_path=source_file_path, include_mathml_source=include_mathml_source))
        if child.tail: parts.append(child.tail)
    txt = "".join(parts).strip()
    
    parent = el.getparent()
    parent_tag = parent.tag if parent is not None else ""
    # Ensure title text itself doesn't get newlines from underline mixed in if it's short
    title_text = txt.replace("\n", " ") 
    if parent_tag.endswith("SECTION"):
        return f"\n## {title_text}\n"
    else:
        return underline(title_text)

# --- Helper for cleaning alt text (can be made global if used more widely) ---
def clean_alt_text_global(text_content: str | None, default_alt: str = "Image") -> str:
    if text_content is None:
        return default_alt
    cleaned = str(text_content).replace('\\n', ' ').replace('\\r', ' ').strip()
    return cleaned if cleaned else default_alt

# r_fig and r_math are assumed to be mostly compatible as they build their own strings.
# r_fig might need to be updated if it calls the old render or relies on its side effects.
# For now, keep existing r_fig and r_math definitions.

def r_fig(el, source_file_path: Path | None = None, include_mathml_source: bool = False):
    NSMAP = {'cnxml': 'http://cnx.rice.edu/cnxml'}
    subs = el.findall(".//cnxml:subfigure", namespaces=NSMAP)
    out: list[str] = []

    if subs:
        for sf in subs:
            alt_node = sf.find(".//cnxml:media", namespaces=NSMAP)
            raw_alt = alt_node.get("alt", "Image") if alt_node is not None else "Image"
            alt = clean_alt_text_global(raw_alt)
            
            src_node = sf.find(".//cnxml:image", namespaces=NSMAP)
            xml_img_src = src_node.get("src") if src_node is not None else None
            md_img_src = "MISSING_SRC" 
            if xml_img_src:
                image_filename = Path(xml_img_src).name
                md_img_src = f"../../media/{image_filename}" 
            out.append(f"![{alt}]({md_img_src})")

        cap_node = el.find(".//cnxml:caption", namespaces=NSMAP)
        if cap_node is not None:
            caption_display_text = render(cap_node, source_file_path=source_file_path, include_mathml_source=False).strip()
            if caption_display_text:
                 out.append(f"\\n\\n*{caption_display_text}*\\n\\n")
    else:
        cap_node = el.find(".//cnxml:caption", namespaces=NSMAP)
        rendered_caption_content = ""
        if cap_node is not None:
            rendered_caption_content = render(cap_node, source_file_path=source_file_path, include_mathml_source=False).strip()
        alt_from_caption = clean_alt_text_global(rendered_caption_content, default_alt="")

        src_node = el.find(".//cnxml:image", namespaces=NSMAP)
        xml_img_src = src_node.get("src") if src_node is not None else None
        md_img_src = "MISSING_SRC"
        if xml_img_src:
            image_filename = Path(xml_img_src).name
            md_img_src = f"../../media/{image_filename}"

        raw_alt_from_media = el.findtext('.//cnxml:media[@alt]', namespaces=NSMAP, default=None)
        alt_from_media = clean_alt_text_global(raw_alt_from_media, default_alt="")

        alt_text_for_image_tag = "Image"
        if alt_from_media:
            alt_text_for_image_tag = alt_from_media
        elif alt_from_caption:
            alt_text_for_image_tag = alt_from_caption
        
        out.append(f"\\n\\n![{alt_text_for_image_tag}]({md_img_src})\\n\\n")

        if rendered_caption_content and (alt_from_media or alt_text_for_image_tag != alt_from_caption):
            out.append(f"\\n\\n*{rendered_caption_content}*\\n\\n")
        elif rendered_caption_content and not alt_from_media and alt_text_for_image_tag == alt_from_caption:
            pass

    return "\\n".join(out)


def r_math(el, source_file_path: Path | None = None, include_mathml_source: bool = False):
    tex_from_lib = mathml_to_tex(el, source_file_path=source_file_path)
    display_attr = el.get("display")

    # --- Debug Print --- 
    # Print only if the debug flag for MathML source is also on, to avoid flooding console otherwise
    if include_mathml_source: 
        # Using repr() for tex_from_lib to make whitespace visible
        pass
        #print(f"[r_math DEBUG] display_attr: '{display_attr}', tex_from_lib (raw): {repr(tex_from_lib[:200])}{'...' if len(tex_from_lib)>200 else ''}")
    # --- End Debug Print ---

    original_mathml_block = ""
    if include_mathml_source:
        try:
            original_mathml = etree.tostring(el, encoding='unicode', pretty_print=True).strip()
        except Exception:
            original_mathml = "Error serializing original MathML"
        original_mathml_block = f'''

<details>
<summary>Original MathML Source</summary>

```xml
{original_mathml}
```

</details>
'''

    latex_part = ""

    # Case 1: Library returned no TeX or only whitespace
    if not tex_from_lib or not tex_from_lib.strip():
        fallback_text = etree.tostring(el, method="text", encoding="unicode").strip()
        if fallback_text:
             latex_part = f"*[MathML fallback (no TeX from lib): {fallback_text}]*" 
        else: 
             latex_part = "*[MathML conversion failed (no TeX from lib)]*"
        # No actual TeX, so just return this part with the optional source block
        output = f'{latex_part}{original_mathml_block}'
        return output.strip()

    # Case 2: Library returned TeX, now process it
    cleaned_tex_for_processing = tex_from_lib.strip()
    processed_tex_content = "" # This will hold the TeX *between* delimiters
    is_block_render_style = False # Flag to indicate if final style is block

    # Determine processing based on display_attr or heuristic
    if display_attr == "inline":
        is_block_render_style = False
        temp_tex = cleaned_tex_for_processing
        if temp_tex.startswith("$$") and temp_tex.endswith("$$"):
            temp_tex = temp_tex[2:-2].strip()
        elif temp_tex.startswith("\\[") and temp_tex.endswith("\\]"):
            temp_tex = temp_tex[2:-2].strip()
        if temp_tex.startswith("$") and temp_tex.endswith("$") and len(temp_tex) > 1:
            temp_tex = temp_tex[1:-1].strip()
        processed_tex_content = temp_tex

    elif display_attr == "block":
        is_block_render_style = True
        temp_tex = cleaned_tex_for_processing
        if temp_tex.startswith("\\begin"): # LaTeX environments like align, gather
            pass 
        elif temp_tex.startswith("$$") and temp_tex.endswith("$$"):
            temp_tex = temp_tex[2:-2].strip()
        elif temp_tex.startswith("\\[") and temp_tex.endswith("\\]"):
            temp_tex = temp_tex[2:-2].strip()
        processed_tex_content = temp_tex
    
    else: # Fallback to heuristic based on library output
        temp_tex = cleaned_tex_for_processing
        if temp_tex.startswith("\\begin") or temp_tex.startswith("\\[") or temp_tex.startswith("$$"):
            is_block_render_style = True
            if temp_tex.startswith("$$") and temp_tex.endswith("$$"):
                temp_tex = temp_tex[2:-2].strip()
            elif temp_tex.startswith("\\[") and temp_tex.endswith("\\]"):
                temp_tex = temp_tex[2:-2].strip()
            # If \begin{...}, it's already good for content
            processed_tex_content = temp_tex
        else: # Heuristic implies inline
            is_block_render_style = False
            # For inline heuristic, also strip single $ if present
            if temp_tex.startswith("$") and temp_tex.endswith("$") and len(temp_tex) > 1:
                temp_tex = temp_tex[1:-1].strip()
            processed_tex_content = temp_tex

    # Now, form the latex_part based on processed_tex_content and render style
    # and apply the "empty after processing" diagnostic
    
    if not processed_tex_content.strip(): # Content inside delimiters is empty/whitespace
        # If tex_from_lib was originally non-empty, but processed_tex_content is empty, it's a diagnostic case.
        # This helps catch cases like library returning "$ $" which becomes empty.
        # We use repr(tex_from_lib) to make sure spaces or minimal content is visible.
        latex_part = f"*[MathML processed to empty TeX. Original from lib: {repr(tex_from_lib)}]*"
    else:
        if is_block_render_style:
            latex_part = f"\n\n$$\n{processed_tex_content}\n$$\n\n"
        else:
            latex_part = f"${processed_tex_content}$"

    output = f'{latex_part}{original_mathml_block}'
    return output.strip()


# --- NEW MAIN RENDER FUNCTION ---
def render(node, source_file_path: Path | None = None, include_mathml_source: bool = False) -> str:
    if isinstance(node, etree._ElementUnicodeResult):
        return str(node) 
    
    if not isinstance(node.tag, str): # Comments, PIs, etc.
        return ""

    tag_name_ns = node.tag
    local_tag_name = tag_name_ns.split("}")[-1] if '}' in tag_name_ns else tag_name_ns
    
    renderer_func = RENDER.get(local_tag_name) or RENDER.get(tag_name_ns)

    output_parts = []
    if renderer_func:
        # ALWAYS pass the include_mathml_source flag to the specific renderer.
        # The renderer itself will decide if/how to use it or pass it further.
        # This requires renderers (like r_para_new, etc.) to accept this param.
        # r_math, r_fig will also receive it.
        try:
            output_parts.append(renderer_func(node, source_file_path=source_file_path, include_mathml_source=include_mathml_source))
        except TypeError as e:
            # Handle cases where a renderer in RENDER might not yet accept include_mathml_source
            if "unexpected keyword argument 'include_mathml_source'" in str(e):
                # Call without the flag as a fallback for non-updated renderers
                # log(f"⚠︎ Renderer for {local_tag_name} does not accept 'include_mathml_source'. Calling without it.")
                output_parts.append(renderer_func(node, source_file_path=source_file_path))
            else:
                raise # Re-raise other TypeErrors
    else:
        # Generic handling: process node.text + children + child.tail
        if node.text:
            output_parts.append(node.text)
        
        for child in node:
            output_parts.append(render(child, source_file_path=source_file_path, include_mathml_source=include_mathml_source)) # Pass flag recursively
            if child.tail:
                output_parts.append(child.tail)
                
    return "".join(output_parts)

# --- NEW MEDIA RENDERER ---
def r_media(el, source_file_path: Path | None = None, include_mathml_source: bool = False):
    NSMAP = {'cnxml': 'http://cnx.rice.edu/cnxml'} 
    
    # Get alt from the <media> tag itself
    alt_text = clean_alt_text_global(el.get("alt"))
    
    # Find the <image> child, or handle if el is <image>
    image_element = None
    if el.tag.endswith("image"): # If this renderer is called for an <image> tag directly
        image_element = el
    else: # Assume el is <media> and find child <image>
        image_element = el.find(".//cnxml:image", namespaces=NSMAP) 

    if image_element is None:
        # log(f"⚠︎ No <image> tag found within element: {etree.tostring(el, pretty_print=True)}")
        return "" # Or some placeholder like *[Missing Image Element]*

    xml_img_src = image_element.get("src")
    md_img_src = "MISSING_SRC_IN_MEDIA_HANDLER" 
    if xml_img_src:
        image_filename = Path(xml_img_src).name
        # Path relative from out_root/modules/mID/index.md to out_root/media/filename.jpg
        # This assumes the standard output structure.
        md_img_src = f"../../media/{image_filename}" 
    else:
        # log(f"⚠︎ Image tag found but 'src' attribute is missing: {etree.tostring(image_element, pretty_print=True)}")
        pass # md_img_src remains MISSING_SRC_IN_MEDIA_HANDLER
    
    # Ensure there are surrounding newlines for block display
    return f"\n\n![{alt_text}]({md_img_src})\n\n"

# --- POPULATE RENDER DICTIONARY ---
# This should be after all r_... and new_r_... functions are defined.
RENDER.update({
    "para": r_para_new,
    "emphasis": r_em_new,
    "term": r_term_new,
    "title": r_title_new,
    "figure": r_fig,
    "math": r_math,
    "media": r_media, # <-- Added media renderer
    # "image": r_media, # Optionally, if <image> can be directly under <para>
    # Add other CNXML tags and their handlers here. For example:
    # "section": r_section_new, (if you define r_section_new)
    # "list": r_list_new,
    # "item": r_item_new,
    # "link": r_link_new, # Example, definition needed
    # If a tag is not here, it gets generic text aggregation.
})
# Ensure MathML specific tag is also covered if namespace is primary
RENDER["{http://www.w3.org/1998/Math/MathML}math"] = r_math


def convert_cnxml(cnxml: Path, include_mathml_source: bool = False) -> str:
    log(f"   • parse {cnxml}")
    parser = etree.XMLParser(recover=True, no_network=True)
    try:
        doc = etree.parse(str(cnxml), parser)
    except etree.XMLSyntaxError as e:
        log(f"⚠︎ XML Syntax Error parsing {cnxml}: {e}")
        return f"Error parsing {cnxml.name}: XML Syntax Error.\\n"
    except Exception as e:
        log(f"⚠︎ Error parsing {cnxml}: {type(e).__name__}: {e}")
        return f"Error parsing {cnxml.name}: {type(e).__name__}.\n"

    # NEW: Call the new render function to get the complete string output
    txt = render(doc.getroot(), source_file_path=cnxml, include_mathml_source=include_mathml_source)
    
    # Cleanup: Collapse multiple newlines (3+ -> 2, 2 stays 2), then strip.
    # Allow max 2 consecutive newlines (one blank line).
    txt = re.sub(r"\n{3,}", "\n\n", txt) 
    txt = txt.strip() # Remove leading/trailing whitespace including newlines

    return txt + "\n" # Ensure single newline at the end of the file.


# ---------------------------------------- locate modules from *.collection.xml -
def modules_from_collection(coll: Path) -> list[Path]:
    tree = etree.parse(str(coll))
    root = tree.getroot()
    ns = {'c': root.nsmap.get(None) or "http://cnx.rice.edu/collxml"}

    modules: list[Path] = []
    # Try more specific XPath first for OpenStax CNXML structure
    # Accounts for <col:module /> and <module /> under <col:content />
    xpath_expr = "//*[local-name()='content']/*[local-name()='module'][@document]"
    module_elements = tree.xpath(xpath_expr)

    if not module_elements: # Fallback to less specific search if above yields nothing
        xpath_expr_fallback = "//*[local-name()='module'][@document]"
        module_elements = tree.xpath(xpath_expr_fallback)

    for mod_el in module_elements:
        uuid = mod_el.get("document")
        if uuid:
            # Assuming standard OS-bundle structure: collection.xml -> modules/uuid/index.cnxml
            module_path = coll.parent.parent / "modules" / uuid / "index.cnxml"
            modules.append(module_path)
            
    # Legacy search if pathing is different (e.g. modules dir next to collection.xml parent)
    if not modules:
        for mod_el in tree.xpath("//*[local-name()='module'][@document]"): # Broader search
            uuid = mod_el.get("document")
            if uuid:
                # This was the original logic: coll.parent.parent / "modules"
                # This implies collection.xml is inside a book-specific folder, e.g. book-slug/collection.xml
                # And modules are in book-slug/modules/
                # Let's test this path if the primary one (coll.parent / "modules") fails.
                # This structure seems less common for typical OS bundles where collection is at root.
                # For now, stick to `coll.parent / "modules"` as primary.
                # Example: current_bundle/collection.xml -> current_bundle/modules/
                pass # Keeping original logic commented out for reference if needed.
                # module_path = coll.parent.parent / "modules" / uuid / "index.cnxml"
                # modules.append(module_path)
    return modules


# ----------------------------------------------------------- CLI entry point --
def main() -> None:
    p = argparse.ArgumentParser(description="Convert OpenStax CNXML to Markdown with LaTeX math (using vendored bowang/mathml2latex).")
    p.add_argument("collection", help="path to *.collection.xml")
    p.add_argument("--out", default="md-out", help="output directory")
    p.add_argument("--include-mathml-source", action="store_true", help="Include original MathML source in output Markdown files.")
    args = p.parse_args()

    coll_path = Path(args.collection).resolve()
    if not coll_path.is_file():
        sys.exit(f"❌ Collection file not found: {coll_path}")

    log(f"Reading {coll_path}")
    modules = modules_from_collection(coll_path)
    if not modules:
        # Check if modules exist relative to collection file's PARENT directory
        # e.g. some_book/some_collection.collection.xml and some_book/modules/
        log(f"No modules found relative to collection dir. Trying relative to collection parent...")
        modules_alt_path = list((coll_path.parent / "modules").glob("*/index.cnxml"))
        if modules_alt_path:
             # This is not robust enough, modules_from_collection should ideally find them based on XML content.
             # Forcing a file system search here if XML parsing fails to find module paths.
             # This part needs review of how module paths are derived if modules_from_collection is insufficient.
             log(f"Found {len(modules_alt_path)} modules via filesystem glob in parent. This is a fallback.")
             # This is just an example, modules_from_collection should be fixed if it fails.
        else:
            sys.exit("❌ 0 module entries found in collection and fallback search failed. Check XML structure, namespaces, or pathing.")


    log(f"Found {len(modules)} modules to process.")
    out_root = Path(args.out).resolve()
    out_root.mkdir(parents=True, exist_ok=True)
    
    # Determine bundle_root more robustly. Usually, it's where 'modules' and 'media' directories sit.
    # If collection.xml is at bundle_root/collection.xml, then bundle_root = coll_path.parent
    # If collection.xml is at bundle_root/subfolder/collection.xml, need to go up.
    # Assuming 'modules' is a sibling to where 'collection.xml' resides or one level up if collection is in a subfolder.
    
    bundle_root_candidate1 = coll_path.parent # e.g., my-book/collection.xml -> my-book/ is bundle root
    bundle_root_candidate2 = coll_path.parent.parent # e.g., my-book/ops/collection.xml -> my-book/ is bundle root

    if (bundle_root_candidate1 / "modules").is_dir() and (bundle_root_candidate1 / "media").is_dir():
        bundle_root = bundle_root_candidate1
    elif (bundle_root_candidate2 / "modules").is_dir() and (bundle_root_candidate2 / "media").is_dir():
        bundle_root = bundle_root_candidate2
    elif (bundle_root_candidate1 / "modules").is_dir(): # Fallback if media isn't where modules is
        bundle_root = bundle_root_candidate1
        log(f"⚠︎ Found 'modules' at {bundle_root}, but 'media' directory not found alongside it. Images may not be copied.")
    elif (bundle_root_candidate2 / "modules").is_dir(): # Fallback if media isn't where modules is
        bundle_root = bundle_root_candidate2
        log(f"⚠︎ Found 'modules' at {bundle_root}, but 'media' directory not found alongside it. Images may not be copied.")
    else:
        bundle_root = coll_path.parent 
        log(f"⚠︎ Could not reliably determine bundle_root based on 'modules' or 'media' dir. Using {bundle_root}. Paths may be incorrect.")

    # Copy media directory
    source_media_dir = bundle_root / "media"
    dest_media_dir = out_root / "media"
    if source_media_dir.is_dir():
        log(f"Copying media from {source_media_dir} to {dest_media_dir}")
        if dest_media_dir.exists():
            shutil.rmtree(dest_media_dir) # Remove existing to avoid merge issues if script is rerun
        try:
            shutil.copytree(source_media_dir, dest_media_dir)
            log(f"✔︎ Media copied successfully.")
        except Exception as e:
            log(f"❌ Error copying media directory: {e}")
    else:
        log(f"⚠︎ Source media directory not found: {source_media_dir}. Images will likely be broken.")


    for m_path in modules:
        if not m_path.is_file(): 
            log(f"⚠︎ Module CNXML file missing or not a file: {m_path.relative_to(bundle_root) if m_path.is_relative_to(bundle_root) else m_path}")
            continue
        
        log(f"Processing module: {m_path.relative_to(bundle_root) if m_path.is_relative_to(bundle_root) else m_path}")
        md_text = convert_cnxml(m_path, include_mathml_source=args.include_mathml_source)
        
        try:
            # Path for md output should be relative to the 'modules' dir found within bundle_root
            # e.g. modules/m12345/index.cnxml -> modules/m12345/index.md
            rel_path_from_bundle_modules = m_path.relative_to(bundle_root / "modules")
            dest = out_root / "modules" / rel_path_from_bundle_modules.with_suffix(".md")
        except ValueError:
            log(f"⚠︎ Could not determine relative path for {m_path} from {bundle_root / 'modules'}. Using fallback naming.")
            # Fallback: use module's parent dir name + original filename
            dest_name = m_path.parent.name + "_" + m_path.name.replace(".cnxml",".md")
            # Put it in a generic 'others' folder if structure is unexpected
            dest_parent_folder = out_root / "others"
            dest = dest_parent_folder / dest_name


        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            dest.write_text(md_text, encoding="utf-8")
            log(f"✔︎ wrote {dest.relative_to(out_root)} ({len(md_text)} bytes)")
        except Exception as e:
            log(f"❌ Error writing file {dest}: {e}")

if __name__ == "__main__":
    main()
