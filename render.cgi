#!/bin/bash


if [ -n "$HOME" ]; then
  root="./"
  md=markdown_py
else
  root=/home/stuff/se16.unbox.org
  md=/home/stuff/env1/bin/markdown_py
fi

what=$QUERY_STRING

[ -z "$what" ] && what="$1"

what=$(echo $what  | sed 's/[^\&\/=A-Za-z0-9._-]/_/g')

if [ ! -f "$1.md" ];
   then cat $root/.worksite/404.html
else    
    Title=$(cat $1.md | awk 'sub(/^# /,"") { print $0; exit}')
    
    if [  -z "$2" ]; then
	 echo "Content-Type: text/html"
	 echo ""
	 cat HEADER.html |
	 sed "s/__TITLE__/${Title}/g" |
	 sed 's/: __TITLE__//'    
    fi
    
    cat $what.md |
    python _etc/xpand.py |
    $md -x tables  \
      -x footnotes -x def_list -x toc -x smart_strong  \
      -x attr_list -x sane_lists  -x  fenced_code  \
      -x "codehilite(linenums=True)" |
    sed "s?<li>.*${Title}.*\$??" 
fi
