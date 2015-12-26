#!/bin/bash
echo "Content-Type: text/html"
echo ""

if [ -n "$HOME" ]; then
  root="./"
  md=markdown_py
else
  root=/home/stuff/se16.unbox.org
  md=/home/stuff/env1/bin/markdown_py
fi

cat HEADER.html

cat $QUERY_STRING.md |
$md -x tables  \
    -x footnotes -x def_list -x toc -x smart_strong  \
    -x attr_list -x sane_lists  -x  fenced_code  \
    -x "codehilite(linenums=True)"

