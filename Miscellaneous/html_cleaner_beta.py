"""
A script for testing concepts of programming to be employed
by an eventual html cleaner script.

CURRENT ISSUE(S): filepath strings for the css file is incorrect, while correct for icon.
"""

import re
import os
from tkinter.filedialog import askdirectory

# Global Variables
TOTAL = 0
PARTIAL = 0


# FUNCTIONS

def re_sub(test_string, current_path, working_directory, filename):
    div = re.sub("(<div[^>]+>)", "", test_string)
    span = re.sub("(<span[^>]+>)", "", div)
    pea = re.sub("(<p [^>]+>)", "<p>", span)
    table = re.sub("(<table [^>]+>)", "<table>", pea)
    teedee = re.sub("(<td [^>]+>)", "<td>", table)
    tear = re.sub("(<tr [^>]+>)", "<tr>", teedee)
    meta = re.sub("(<meta [^>]+>)", "", tear)
    style = re.sub("(<style>[^>]+>)", "", meta)
    body = re.sub("(<body [^>]+>)", "", style)
    new_string = body.replace("</div>", "")
    new_string = new_string.replace("</span>", "")
    new_string = new_string.replace("</div>", "")
    new_string = new_string.replace("</style>", "")
    new_string = new_string.replace("</body>", "")
    new_string = new_string.replace("Central%20Hub.htm", "index.html")
    # Adding a stylesheet link
    style_link = os.path.relpath(working_directory, current_path)
    style_link = style_link.replace("\\", "/")
    css_link = f'<head>\n\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n\t<link rel="stylesheet" href="{style_link}/liberation_format.css">'
    new_string = new_string.replace('<head>', css_link)
    # Remove unneeded newlines
    new_string = new_string.replace("\n\n\n", "")

    # Add newlines as needed now.
    new_string = new_string.replace("<title>", "\n<title>", 1)
    new_string = new_string.replace("<link>", "\n<link>", 2)
    new_string = new_string.replace("</head>", "\n<head>", 1)
    new_string = new_string.replace("</head><p>", "</head>\n\n<p>", 1)
    new_string = new_string.replace("<hr", "\n<hr")
    new_string = new_string.replace("align=center>", "align=center>\n")
    #new_string = new_string.replace("\n\n ", "")
    new_string = new_string.replace("<p>&nbsp;</p></html>", "\n</html>")
    new_string = new_string.replace("<p><i>&nbsp;</i></p></html>", "\n</html>")
    new_string = new_string.replace("<p><b>&nbsp;</b></p></html>", "\n</html>")
    new_string = new_string.replace("<p>&nbsp;</p>\n<p>&nbsp;</p>", "<p>&nbsp;</p>")


    # Insure all links are there.
    # new_string = add_gender(new_string, current_path)

    return new_string


def add_gender(old_string: str, current_path):
    """Adds a hyperlink to the gender specification if there is no gender"""

    working_directory = "../Grammar/Noun Grammar"
    # Making directory path for noun gender and type hyperlinks
    style_link = os.path.relpath(working_directory, current_path)
    style_link = style_link.replace("\\", "/")
    # Final Links
    gen_link = f'<a href="{style_link}/Gender.htm">'
    weak_link = f'<a href="{style_link}/Weak%20Nouns.htm">'
    strong_link = f'<a href="{style_link}/Strong%20Nouns.htm">'

    # Making Sure all keywords are formatted correctly
    old_string = old_string.replace("neuter", "Neuter", 1)
    old_string = old_string.replace("common", "Common", 1)
    old_string = old_string.replace("masculine", "Masculine", 1)
    old_string = old_string.replace("feminine", "Feminine", 1)
    old_string = old_string.replace("Gendered Feminine", "Gendered-Feminine", 1)
    old_string = old_string.replace("Gendered Masculine", "Gendered-Masculine", 1)
    old_string = old_string.replace("Gendered Common", "Gendered-Common", 1)

    old_string = old_string.replace("Strong I", "Strong-I")
    old_string = old_string.replace("Strong II", "Strong-II")
    old_string = old_string.replace("Weak I", "Weak-I")
    old_string.replace("Weak II", "Weak-II")

    new_string = old_string

    # Search for keywords, replace them with keyword + hyperlink if hyperlink is missing.
    if "Neuter" in old_string:
        if "Neuter</a>" not in old_string:
            new_string = old_string.replace("Neuter", gen_link + "Neuter" + "</a>", 1)
            print("Successful fix for Gender hyperlink!")
    elif "Feminine" in old_string:
        if "Feminine</a>" not in old_string:
            new_string = old_string.replace("Feminine", gen_link + "Feminine" + "</a>", 1)
            print("Successful fix for Gender hyperlink!")
    elif "Masculine" in old_string:
        if "Masculine</a>" not in old_string:
            new_string = old_string.replace("Masculine", gen_link + "Masculine" + "</a>", 1)
            print("Successful fix for Gender hyperlink!")
    elif "Common" in old_string:
        if "Common</a>" not in old_string:
            new_string = old_string.replace("Common", gen_link + "Common" + "</a>", 1)
            print("Successful fix for Gender hyperlink!")
    elif "Gendered-Masculine" in old_string:
        if "Gendered-Masculine</a>" not in old_string:
            new_string = old_string.replace("Gendered-Masculine", gen_link + "Gendered-Masculine" + "</a>", 1)
            print("Successful fix for Gender hyperlink!")
    elif "Gendered-Feminine" in old_string:
        if "Gendered-Feminine</a>" not in old_string:
            new_string = old_string.replace("Gendered-Feminine", gen_link + "Gendered-Feminine" + "</a>", 1)
            print("Successful fix for Gender hyperlink!")
    elif "Gendered-Common" in old_string:
        if "Gendered-Common</a>" not in old_string:
            new_string = old_string.replace("Gendered-Common", gen_link + "Gendered-Common" + "</a>", 1)
            print("Successful fix for Gender hyperlink!")

    
    # Now check and fix noun type links
    if "Strong-II" in new_string:
        if "Strong-II</a>" not in new_string:
            new_string = new_string.replace("Strong-II", strong_link + "Strong-II" + "</a>", 1)
            print("Successful fix for Noun Type hyperlink!")
    elif "Strong-I" in new_string:
        if "Strong-I</a>" not in new_string and "Strong-II</a>" not in new_string:
            new_string = new_string.replace("Strong-I", strong_link + "Strong-I" + "</a>", 1)
            print("Successful fix for Noun Type hyperlink!")
    elif "Weak-II" in new_string:
        if "Weak-II</a>" not in new_string:
            new_string = new_string.replace("Weak-II", strong_link + "Weak-II" + "</a>", 1)
            print("Successful fix for Noun Type hyperlink!")
    elif "Weak-I" in new_string:
        if "Weak-I</a>" not in new_string and "Weak-II</a>" not in new_string:
            new_string = new_string.replace("Weak-I", strong_link + "Weak-I" + "</a>", 1)
            print("Successful fix for Noun Type hyperlink!")
    
    print()

    return new_string


def add_title(old_string: str, filename):
    """If there is no title in the file."""
    if "<title>" not in old_string:
        index_point = old_string.index("css\">")
        new_string = old_string[:index_point] + f"\n<title>Neo-Adûnaic : {filename}</title>" + old_string[index_point:]
    return new_string


def add_bullet(old_string):
    # Find nearest aspect of string that has <p>...·&nbsp; in it, then replace it with <ul>.  
    re.sub('(<p>·&nbsp;[^<]+<)', '<ul>\n<p><li><', new_string)
    # Once done, take everything between <ul> and </ul> and loop through it until all the bullets are added.
    pre_ula = "<ul>"
    end_tag = "</ul>"
    # Adding bullets
    ula = re.sub("(·[^<]+)", "<li>", old_string)  # Use loop with index starting here to locate where to place </ul>
    # Figuring out where to add </ul>
    if re.findall("(<li>[^</li>])</p>") == True: # Obviously that regex needs polishing, just a placeholder atm.
        asdf = ""
    else:
        new_string = re.sub("</li></p>", "</li></p>\n</ul>") # Now how to get this to only do it to the last one only...


# Acquire directory path
directory = askdirectory()

# Get Current Working Directory (CWD)
working_directory = os.getcwd()

# Calculate total number of files
for root, dirs, files in os.walk(directory):
    for file in files:
        if file[-4:] == ".htm":
            TOTAL += 1

# Walk and clean chosen directory
for root, dirs, files in os.walk(directory):
    for filename in files:

        root2 = root.replace("\\", "/")
        if filename[-4:] == ".htm":
            filename2 = filename[:-4]
            
            # Get information from file
            file_path = root2 + "/" + filename
            old_file = open(file_path, "r", encoding="windows-1252")
            old_string = old_file.read()
            old_file.close()
            os.remove(file_path)

            # Clean File
            new_string = re_sub(old_string, root2, working_directory, filename2)

            # Input edited information back into file
            fixed_file = open(root2 + "/" + filename, "w", encoding="utf-8")
            fixed_file.write(new_string)
            fixed_file.close()
            # add to the number of files completed
            PARTIAL += 1
            print(str(PARTIAL) + "/" + str(TOTAL) + " completed!")
        else:
            next

print()
input("Hit enter to continue...")