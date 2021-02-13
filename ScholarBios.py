import requests
import markdown
from bs4 import BeautifulSoup

output = ""

url = "https://www.schwarzmanscholars.org/scholars/"

payload={}
headers = {
  'User-Agent': 'PostmanRuntime/7.26.10'
}

response = requests.request("GET", url, headers=headers, data=payload)
content = response.text

soup = (BeautifulSoup(content, "html.parser").find_all('button', {"class":"action-launch-bio-modal", "data-bio-modal-subtitle":"Class of 2022"}))
print(soup)

for item in soup:
    output += '<img src="{0}" alt="{1}" width="200"/>\n'.format(item["data-bio-modal-image"], item["data-bio-modal-name"])
    output += "# {0}\n".format(item["data-bio-modal-name"])
    output += "## {0}\n".format(item["data-bio-modal-subtitle"])
    output += "{0}\n\n\n".format(item["data-bio-modal-text"])

with open('output.md', mode='w', encoding='utf-8') as o:
    o.write(output)

with open('output.html', mode='w', encoding='utf-8') as o:
    o.write(
        """
        <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Schwarzman Scholars</title>
        <style>
</style>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.min.css" integrity="sha384-yFRtMMDnQtDRO8rLpMIKrtPCD5jdktao2TV19YiZYWMDkUR5GQZR/NOVTdquEx1j" crossorigin="anonymous">
<link href="https://cdn.jsdelivr.net/npm/katex-copytex@latest/dist/katex-copytex.min.css" rel="stylesheet" type="text/css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/markdown.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/highlight.css">
<style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe WPC', 'Segoe UI', system-ui, 'Ubuntu', 'Droid Sans', sans-serif;
                font-size: 14px;
                line-height: 1.6;
            }
        </style>
        <style>
.task-list-item { list-style-type: none; } .task-list-item-checkbox { margin-left: -20px; vertical-align: middle; }
</style>
        
        <script src="https://cdn.jsdelivr.net/npm/katex-copytex@latest/dist/katex-copytex.min.js"></script>
        
    </head>
    <body class="vscode-body vscode-light">
        """
    )
    o.write(markdown.markdown(output))
    o.write("</body></html>")    
