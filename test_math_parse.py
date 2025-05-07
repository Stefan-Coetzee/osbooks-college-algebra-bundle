from bs4 import BeautifulSoup
from mathml2latex.mathml import process_mathml # Direct import

# >>> PASTE THE ACTUAL FAILING MATHML SNIPPET (the one you copied in Step 1.4) 
# >>> AS A MULTILINE STRING BELOW:
failing_mathml_string = """
    <m:math xmlns:m="http://www.w3.org/1998/Math/MathML" xmlns="http://cnx.rice.edu/cnxml">
    <m:mrow>
    <m:mi>f</m:mi><m:mo stretchy="false">(</m:mo><m:mi>x</m:mi><m:mo stretchy="false">)</m:mo><m:mo>=</m:mo><m:mo>−</m:mo><m:mfrac>
    <m:mn>1</m:mn>
    <m:mn>3</m:mn>
    </m:mfrac>
    <m:msup>
    <m:mi>e</m:mi>
    <m:mi>x</m:mi>
    </m:msup>
    <m:mo>−</m:mo><m:mn>2</m:mn><m:mo>;</m:mo>
    </m:mrow>
    </m:math>
    """
# Make sure the above string is replaced with your *actual* failing snippet.

print("--- Input MathML ---")
print(failing_mathml_string)
print("--------------------")

try:
    soup = BeautifulSoup(failing_mathml_string, "xml")
    
    # This logic is closer to what's in your main.py's mathml_to_tex
    math_tag_in_soup = soup.find(lambda tag: tag.name == 'math' or tag.name.endswith(':math'))
    if not math_tag_in_soup: # Fallback if xml_string was just <math>...</math> (less likely for a full snippet)
            math_tag_in_soup = soup 

    # Further refinement if the above didn't quite get the actual math element
    if not hasattr(math_tag_in_soup, 'name') or not math_tag_in_soup.name or math_tag_in_soup.name not in ['math', 'm:math']:
            # This can happen if soup.find returns the document root or something unexpected
            # if the initial find was too broad or if the structure is nested differently.
            # Try to find the first actual 'math' tag element more directly if the above was not specific enough.
            first_child_math = None
            if soup.contents and hasattr(soup.contents[0], 'name') and (soup.contents[0].name == 'math' or soup.contents[0].name.endswith(':math')):
                first_child_math = soup.contents[0]
            
            if first_child_math:
                math_tag_in_soup = first_child_math
            elif not (hasattr(math_tag_in_soup, 'name') and (math_tag_in_soup.name == 'math' or math_tag_in_soup.name.endswith(':math'))):
                # If it's still not a math tag, this is problematic.
                print(f"!!!DEBUG: math_tag_in_soup is '{math_tag_in_soup.name if hasattr(math_tag_in_soup, 'name') else 'Not a tag'}' after find. Trying children.")
                # This part is tricky; process_mathml expects the <math> tag.
                # If the soup object itself is the document and the <math> tag is its first child:
                if soup.contents and len(soup.contents) > 0 and hasattr(soup.contents[0], 'name'):
                     if soup.contents[0].name == 'math' or soup.contents[0].name.endswith(':math'):
                          math_tag_in_soup = soup.contents[0]
                     else:
                          print(f"!!! First child is {soup.contents[0].name}, not math.")
                else:
                     print(f"!!! No clear math tag found as first child of soup.")


    if not (hasattr(math_tag_in_soup, 'name') and (math_tag_in_soup.name == 'math' or math_tag_in_soup.name.endswith(':math'))):
        print(f"!!! CRITICAL: Could not pass a proper <math> element to process_mathml. Object is: {type(math_tag_in_soup)}")
        # For safety, skip calling process_mathml if we don't have a math tag.
        latex_output = "Error: Could not find math tag in test script."
    else:
        print(f"--- Passing to process_mathml: Element <{math_tag_in_soup.name if hasattr(math_tag_in_soup, 'name') else 'Object without name attribute'}> ---")
        latex_output = process_mathml(math_tag_in_soup) 

    print("\n--- LaTeX Output (from process_mathml) ---")
    print(latex_output) 
    print("------------------------------------------")

except Exception as e:
    print(f"\n--- ERROR during conversion in test_math_parse.py ---")
    import traceback
    traceback.print_exc() 
    print("----------------------------------------------------------")
