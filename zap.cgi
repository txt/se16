#!/bin/bash
cat<<EOF
Content-Type: text/html

<html>
<head>
<title>Updating</title>
</head>
<body>
<p>$(date)
<pre>
$(rm -rf .htaccess *; git clone https://github.com/txt/se16.git .)
</pre>
</body>
</html>
