#!/bin/bash
cat<<EOF
Content-Type: text/html

<html>
<head>
<title>Updating</title>
</head>
<body>
<p>
EOF

date
git pull origin master

date >> logs

cat<<EOF
<pre>
</pre>
</body>
</html>
EOF
