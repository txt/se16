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

date >> logs

cat<<EOF
</pre>
</body>
</html>
EOF
