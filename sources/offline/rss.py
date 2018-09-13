#!/bin/python
import sys

title = sys.argv[2]
filename = sys.argv[3]
date = sys.argv[1]
description = sys.argv[4]
with open("sources/item_template.xml") as file:
  source = file.read().format(title=title, filename=filename, date=date, description=description)

with open("rss.xml", "r") as file:
  lines = file.readlines()

with open("rss.xml", "w") as file:
  file.write("".join(lines[0:7]))
  file.write(source)
  file.write("".join(lines[7:]))
