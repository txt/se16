#!/bin/env python

import sys,markdown2,cgi
from markdown2 import markdown as marked

marked = markdown2.markdown
#reload(sys)  

#sys.setdefaultencoding('utf8')

Extras=["metadata",
        "fenced-code-blocks",
        "footnotes",
        "toc"]

sys,readlibs(sys.agv[1])
for k,v in html.metadata.items()  :
  the[k] = Template(v).safe_substitute(the)
for k,v in config.metadata.items():
  the[k] = Template(v).safe_substitute(the)

template = slurp(the.themes + the.theme)

the['TOC'] = html.toc_html
the['PAGE'] = html

page= Template(template).safe_substitute(the)

print  "Content-type: text/html\n\n"
print page
  
