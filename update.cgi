#!/bin/bash
cat<<EOF
Content-Type: text/html

<html>
<head>
<title>Updating</title>
</head>
<body>
<pre>
EOF

date
git pull origin master

ls -lsa

cat<<EOF
</pre>
</body>
</html>
EOF
