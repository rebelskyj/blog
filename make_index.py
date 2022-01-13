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
        
def main():
    sources = []
    with open("sources/order.txt") as f:
        for line in f:
            line = line.rstrip()
            if not line:
                continue
            filename, _ = line.split(":")
            filename = "sources/base/" + filename.replace(".tex", ".html")
            sources.append(filename)

    sources.reverse() # newest first
    lines = []
    for i, line in enumerate(sources):
        lines.append(line)
        if (i + 1) % 10 == 0:
            num = i // 10
            write_file(sources=lines, num=num, prev=num != 0, next=(i + 1 != len(sources)))
            lines = []

    if lines:
        num = i//10 + 1
        write_file(sources=lines, num=num, prev=True, next=False)

if __name__ == "__main__":
    main()
