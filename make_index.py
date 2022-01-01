import sys
from math import ceil

with open("index_base.html", "r") as f:
    template = f.read()

def write_file(sources, num, next, prev):
    content = []
    nav_links = ""
    for i, source in enumerate(sources):
        with open(source, "r") as f:
            raw = f.read()
            content.append(raw.replace(
                'href="#fn', 'href="#fn0{}'.format(i)
            ).replace(
                'id="fn', 'id="fn0{}'.format(i)
            ))
    if(prev):
        nav_links += '<a class="nav-previous" href="index{}.html">Newer</a>\n'.format(num - 1)
    if(next):
        nav_links += '<a class="nav-next" href="index{}.html">Older</a>\n'.format(num + 1)
    with open("docs/index{num}.html".format(num = num), "w") as output:
        output.write(template.replace("{content}", "\n".join(content)).replace("{nav-links}", nav_links))
        
lines = []
content = sys.stdin.readlines()


for i, line in enumerate(content):
    lines.append(line.rstrip())
    if((i + 1) % 10 == 0):
        args = {}
        num = i//10
        write_file(sources = lines, num = num, prev = num != 0, next = i != len(content))
        lines = []

if(len(lines) > 0):
    num = int(ceil(i/10))
    write_file(sources = lines, num = num, prev = True, next = False)
