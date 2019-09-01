REVERSE := tail -r
posts = $(patsubst sources/%.tex,docs/%.html,$(wildcard sources/*.tex))
snippets = $(patsubst sources/%.tex,sources/base/%.html,$(wildcard sources/*.tex))
auto : docs/index.html calendar
	python sources/compile.py $$(tail -n1 sources/order.txt | sed 's/\(.*\).tex:.*/docs\/\1.html/g') | bash
	python sources/compile.py $$(tail -n2 sources/order.txt | head -n1 | sed 's/\(.*\).tex:.*/docs\/\1.html/g') | bash
all : $(posts) $(snippets) docs/index.html docs/calendar.html docs/calendar_base.html
calendar: docs/calendar.html docs/calendar_base.html
docs/calendar.html : calendar/order.txt calendar/calendar.md
	calendar/compile.sh
docs/calendar_base.html : calendar/order.txt calendar/calendar.md
	calendar/compile_base.sh
docs/index.html : $(snippets)
	python sources/fix_order.py
	${REVERSE} sources/order.txt | sed 's-\(.*\).tex:.*-sources/base/\1.html-g' | python make_index.py
	rm docs/index.html
	ln -s docs/index0.html docs/index.html

sources/base/%.html : sources/%.tex
	pandoc -o $@ $<

docs/%.html : sources/%.tex sources/template.html sources/order.txt
	python sources/compile.py $@ | bash
