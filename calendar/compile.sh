#!/bin/bash
python calendar/compile.py | pandoc -s -o calendar.html --from=markdown --template=sources/template.html -M "pagetitle=Calendar" --css pandoc.css --css calendar.css
