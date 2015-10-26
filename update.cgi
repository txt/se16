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

$(chmod 755 *.cgi)

</pre>
</body>
</html>
EOF


