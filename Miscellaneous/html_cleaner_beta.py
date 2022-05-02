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

def re_sub(test_string, current_path, working_directory):
    div = re.sub("(<div[^>]+>)", "", test_string)
    span = re.sub("(<span[^>]+>)", "", div)
    pea = re.sub("(<p [^>]+>)", "<p>", span)
    teedee = re.sub("(<td [^>]+>)", "<td>", pea)
    tear = re.sub("(<tr [^>]+>)", "<tr>", teedee)
    meta = re.sub("(<meta [^>]+>)", "", tear)
    style = re.sub("(<style>[^>]+>)", "", meta)
    body = re.sub("(<body [^>]+>)", "", style)
    #ula = re.sub('(·&nbsp;[^\n]+\n)', '<ul class="a">')
    new_string = body.replace("</div>", "")
    new_string = new_string.replace("</span>", "")
    new_string = new_string.replace("</div>", "")
    new_string = new_string.replace("</style>", "")
    new_string = new_string.replace("</body>", "")
    new_string = new_string.replace("Central%20Hub.htm", "index.html")
    # Adding a stylesheet link
    style_link = os.path.relpath(working_directory, current_path)
    style_link = style_link.replace("\\", "/")
    css_link = f'<head>\n\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n\t<link rel="stylesheet" href="{style_link}/liberation_format.css">' # Must use / for Mac/Linux and website(?)
    new_string = new_string.replace('<head>', css_link)
    print(style_link)

    return new_string

def add_bullet(old_string):
    pre_ula = "<ul>"
    post_ula = "</ul>"
    # Adding bullets
    ula = re.sub("(·[^<]+)", "<ul>", old_string)  # Use loop with index starting here to locate where to place </ul>

# Acquire directory path
directory = askdirectory()

# Get Current Working Directory (CWD)
working_directory = os.getcwd()

# Calculate total number of files
for root, dirs, files in os.walk(directory):
    for file in files:
        if file[-4:] == ".htm":  # MAKE SURE TO TEST THIS!
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
            new_string = re_sub(old_string, root2, working_directory)

            # Input edited information back into file
            fixed_file = open(root2 + "/" + filename, "w", encoding="utf-8")
            fixed_file.write(new_string)
            fixed_file.close()
            # add to the number of files completed
            PARTIAL += 1
            print(str(PARTIAL) + "/" + str(TOTAL) + " completed!")
        else:
            next
