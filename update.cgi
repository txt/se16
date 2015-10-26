#!/bin/bash
echo "Content-Type: text/html"
echo ""

echo "<p>$(date)</p><pre>"
git pull origin master
echo "</pre>"
