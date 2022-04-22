REVERSE := tail -r
TEX_FILES := $(shell sed -e 's/[.]tex:.*$$/.tex/g' -e 's-^.-sources/&-' sources/order.txt)
DOCS := $(patsubst sources/%.tex,docs/%.html,$(TEX_FILES))
SNIPPETS := $(patsubst sources/%.tex,sources/base/%.html,$(TEX_FILES))

all : $(DOCS) $(SNIPPETS) docs/index.html calendar
	python3 sources/compile.py $$(tail -n1 sources/order.txt)
	python3 sources/compile.py $$(tail -n2 sources/order.txt | head -n1)
calendar: docs/calendar.html docs/calendar_base.html

docs/calendar.html : calendar/order.txt calendar/calendar.md
	python3 calendar/compile.py\
		| pandoc -s -o docs/calendar.html --from=markdown --template=sources/template.html -M "pagetitle=Calendar" --css calendar.css --css pandoc.css

docs/calendar_base.html : calendar/order.txt calendar/calendar.md
	python3 calendar/compile.py\
		| pandoc -s -o docs/calendar_base.html --from=markdown -M "pagetitle=Calendar" --css calendar.css --css pandoc_min.css

docs/index.html : $(SNIPPETS) make_index.py
	python3 make_index.py && cp docs/index0.html docs/index.html

sources/base/%.html : sources/%.tex
	pandoc -o $@ $<

docs/%.html : sources/%.tex sources/template.html
	python3 sources/compile.py $@

.PHONY: calendar all
