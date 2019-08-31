#!/bin/python
import sys

title = raw_input("Title: ")
filename = raw_input("Filename (don't include the html extension): ")
date = sys.argv[1]
description = raw_input("Description: ")
with open("sources/item_template.xml") as file:
  source = file.read().format(title=title, filename=filename, date=date, description=description)

with open("docs/rss.xml", "r") as file:
  lines = file.readlines()

with open("docs/rss.xml", "w") as file:
  file.write("".join(lines[0:7]))
  file.write(source)
  file.write("".join(lines[7:]))
