REVERSE := tac
posts = $(patsubst sources/%.tex,docs/%.html,$(wildcard sources/*.tex))
snippets = $(patsubst sources/%.tex,sources/base/%.html,$(wildcard sources/*.tex))
auto : docs/index.html calendar
	python sources/compile.py $$(tail -n1 sources/order.txt | sed 's/\(.*\).tex:.*/\1.html/g') | bash
	python sources/compile.py $$(tail -n2 sources/order.txt | head -n1 | sed 's/\(.*\).tex:.*/\1.html/g') | bash
all : $(posts) $(snippets) docs/index.html docs/calendar.html docs/calendar_base.html
calendar: docs/calendar.html docs/calendar_base.html
docs/calendar.html : calendar/order.txt calendar/calendar.md
	calendar/compile.sh
docs/calendar_base.html : calendar/order.txt calendar/calendar.md
	calendar/compile_base.sh
docs/index.html : $(snippets)
	python sources/fix_order.py
	pandoc -s -o index.html $$(${REVERSE} sources/order.txt | sed 's/\(.*\).tex:.*/sources\/base\/\1.html/g') -M pagetitle=Home --template=sources/template.html --css pandoc.css

sources/base/%.html : sources/%.tex
	pandoc -o $@ $<

docs/%.html : sources/%.tex sources/template.html sources/order.txt
	python sources/compile.py $@ | bash
