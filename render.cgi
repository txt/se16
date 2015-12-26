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

what="$QUERY_STRING"

[ -z "$what" ] && what="$1"

apply_shell_expansion() {
    declare file="$1"
    declare data=$(< "$file")
    declare delimiter="__apply_shell_expansion_delimiter__"
    declare command="cat <<$delimiter"$'\n'"$data"$'\n'"$delimiter"
    eval "$command"
}

. _etc/references.bib

cat HEADER.html

apply_shell_expansion $what.md |
$md -x tables  \
    -x footnotes -x def_list -x toc -x smart_strong  \
    -x attr_list -x sane_lists  -x  fenced_code  \
    -x "codehilite(linenums=True)"

