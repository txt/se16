#!/bin/bash
echo "Content-Type: text/html"
echo ""

echo "<p>"
date
echo "</p><pre>"
git pull origin master
echo "</pre>"
