# coding: utf-8

# Place this file in any directory and run it
# A HTML, CSS, Javascript, and Python file will be genrated in the directory
# Double click the html file to launch it in a browser.
# That's it

WRITE= 'w'
READ= 'r'
APPEND = 'a'
READWRITE = 'w+'

html_file = 'index.html'
css_file = 'style.css'
javascript_file = 'script.js'
python_file = 'code.py'
ruby_file = 'ruby.py'
package_file = 'package.json'

html_code = """<!DOCTYPE html>
<html lang='en'>
<head>
	<meta charset='UTF-8'>
	<link href='style.css' rel='stylesheet'>
	<script src='script.js' type='text/javascript'></script>
</head>
<body>
	<p>Text Here: </p>
</body>
</html>"""

css_code = "p{color:red}"

javascript_code = "document.write('Javascript working')"

python_code = """html_file = "index.html"
with open(html_file,"a") as infile:
    infile.write("Python Working ")
    infile.write("<script>document.write('Yasss!')</script>")
"""
package_code = """{
    "main": "index.html",
    "name": "Gmg",
    "window": {
      "toolbar":false,
      "resizable:":true,
      "fullscreen":false,
      "width":850,
      "height":600
    }
}

"""

ruby_code = """print('Hello') """


with open(html_file,mode=WRITE) as outfile:
	outfile.write(html_code)
	
with open(css_file,mode=WRITE) as outfile:
	outfile.write(css_code)

with open(javascript_file,mode=WRITE) as outfile:
	outfile.write(javascript_code)

with open(python_file,mode=WRITE) as outfile:
    outfile.write(python_code)

with open(python_file,mode=WRITE) as outfile:
    outfile.write(ruby_code)

with open(package_file,mode=WRITE) as outfile:
    outfile.write(package_code)
execfile(python_file)


# CUSTOMIZE: (Add your cool functions and stuff here)
import os,webbrowser

def locationOf(filename="index.html"):
    return os.getcwd() + "/" + filename

webbrowser.open(locationOf(html_file))