#!/bin/bash
echo "Content-Type: text/html"
echo ""

echo "<pre>"
git pull origin master
echo "</pre>"
