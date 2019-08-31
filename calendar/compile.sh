#!/bin/bash
python calendar/compile.py | pandoc -s -o docs/calendar.html --from=markdown --template=sources/template.html -M "pagetitle=Calendar" --css calendar.css --css pandoc.css
