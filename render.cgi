#!/bin/bash
echo "Content-Type: text/html"
echo ""

if [ -n "$HOME" ]; then
  md=markdown_py
else
  md="/home/stuff/env1/bin/markdown_py"
fi

cat _tmp/test.md | $md
