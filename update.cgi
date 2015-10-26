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
$(git pull origin master)
</pre>
</body>
</html>
