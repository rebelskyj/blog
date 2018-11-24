#!/bin/bash
python calendar/compile.py | pandoc -s -o calendar_base.html --from=markdown -M "pagetitle=Calendar" --css calendar.css --css pandoc_min.css
