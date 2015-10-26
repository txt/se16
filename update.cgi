#!/bin/bash
cat<<EOF
Content-Type: text/html

<html>
<head>
<title>Updating</title>
</head>
<body>
<pre>

$(date;git pull origin master)

$(ls -lsa)

</pre>
</body>
</html>
EOF

chmod 755 *.cgi
