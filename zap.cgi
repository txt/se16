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
rm -rf .htaccess *
git clone https://github.com/txt/se16.git .

date >> logs.del

cat<<EOF
</pre>
</body>
</html>
EOF
