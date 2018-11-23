htmls = $(patsubst sources/%.tex,%.html,$(wildcard sources/*.tex))
snippets = $(patsubst sources/%.tex,sources/base/%.html,$(wildcard sources/*.tex))
make : $(htmls) $(snippets) index.html
calendar.html : calendar/order.txt calendar/calendar.md
	calendar/compile.sh
index.html : sources/base/*
	python sources/fix_order.py
	pandoc -s -o index.html $$(tail -r sources/order.txt | sed 's/\(.*\).tex:.*/sources\/base\/\1.html/g') -M pagetitle=Home --template=sources/template.html --css pandoc.css

sources/base/%.html : sources/%.tex
	pandoc -o $@ $<

%.html : sources/%.tex sources/template.html sources/order.txt
	 python sources/compile.py $@ | bash
