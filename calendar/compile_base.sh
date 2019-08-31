#!/bin/bash
python calendar/compile.py | pandoc -s -o docs/calendar_base.html --from=markdown -M "pagetitle=Calendar" --css calendar.css --css pandoc_min.css
