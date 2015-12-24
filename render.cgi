#!/bin/bash
echo "Content-Type: text/html"
echo ""

if [ -n "$HOME" ]; then
  md=markdown_py
else
  md="/home/stuff/env1/bin/markdown_py"
fi

cat HEADER.html

cat $1 | $md -x tables  \
                     -x footnotes -x def_list -x toc -x smart_strong  \
                     -x attr_list -x sane_lists  -x  fenced_code  \
                     -x "codehilite(linenums=True)"

