from sys import argv
	# pandoc -s -o $@ $< -M "pagetitle=$$(grep '$(<F)' sources/order.txt | sed 's/.*://')" --template=sources/template.html

filename = argv[1].replace(".html", "")
with open("sources/order.txt", "r") as order:
  lines = order.readlines()

for i, line in enumerate(lines):
  if line.find(filename) != -1:
    index = i
    break

def get_index(lines, index):
  if(index < 0):
    return ['', '']
  try:
    return lines[index].split(":")
  except:
    return ['', '']

source = "sources/{}.tex".format(filename)
dest = "{}.html".format(filename)
name = lines[index].split(":")[1]
prevurl, prev = get_index(lines, index-1)
nexturl, next = get_index(lines, index+1)
nexturl = nexturl.replace(".tex", ".html")
prevurl = prevurl.replace(".tex", ".html")

options = {"next": next, "prev": prev, "nexturl": nexturl, "prevurl": prevurl, "pagetitle": name}
options_string = filter(lambda x: options[x] != "", options.keys())
options_string = map(lambda x: '-M "{}={}"'.format(x.strip(), options[x].strip()), options_string)
options_string = " ".join(list(options_string))

print('pandoc -s -o {} {} --template=sources/template.html {} --css pandoc.css'.format(dest, source, options_string))
