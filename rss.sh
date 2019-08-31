#!/bin/bash
python sources/rss.py "$(date -R)"
git add docs/rss.xml
git commit -m "Updated rss feed"
git push
