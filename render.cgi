#!/bin/bash
echo "Content-Type: text/html"
echo ""

css="pygment_pastie.css"
if [ -n "$HOME" ]; then
  md=markdown_py
else
  md="/home/tumm/env/bin/markdown_py"
fi

echo '<html><head>'
echo '<link rel="stylesheet" type="text/css" href="'$css'">'

echo '</head><body>'

cat _tmp/test.md | $md -x tables  \
                     -x footnotes -x def_list -x toc -x smart_strong  \
                     -x attr_list -x sane_lists  -x  fenced_code  \
                     -x "codehilite(linenums=True)"

echo '</body></html>'
