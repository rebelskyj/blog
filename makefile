htmls = $(patsubst sources/%.tex,%.html,$(wildcard sources/*.tex))
make : $(htmls) index.html

index.html : sources/*
	pandoc -s -o index.html $$(tail -r sources/order.txt | sed 's/\(.*\):.*/sources\/\1/g') -M pagetitle=Home --template=sources/template.html --css pandoc.css

%.html : sources/%.tex sources/template.html sources/order.txt
	 python3 sources/compile.py $@ | bash
