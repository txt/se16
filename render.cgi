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

what=$QUERY_STRING

[ -z "$what" ] && what="$1"

if [ ! -f "$1.md" ];
   then cat $root/.worksite/404.html
else    
    Title=$(cat $1.md | awk 'sub(/^# /,"") { print $0; exit}')
    

    cat HEADER.html | sed "s/__TITLE__/${Title}/g"
    
    cat $what.md |
    python _etc/xpand.py |
    $md -x tables  \
      -x footnotes -x def_list -x toc -x smart_strong  \
      -x attr_list -x sane_lists  -x  fenced_code  \
      -x "codehilite(linenums=True)"
fi
