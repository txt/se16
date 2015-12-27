from __future__ import print_function

import re,sys
d=dict(

_GIRLBOT="""
<img size=300 align=right   src="/_img/girlbot.jpg">
""",

_UNDER400="""
<center><img size=400 src="https://www.lahc.edu/pageunderconstruction.png"></center>
""",


_FERU10="""
David Ferrucci, Eric Brown, Jennifer Chu-Carroll, 
James Fan, David Gondek, Aditya A. Kalyanpur, Adam Lally, 
J. William Murdock, Eric Nyberg, John Prager, Nico Schlaefer, 
and Chris Welty, 
[THE AI BEHIND WATSON](http://www.aaai.org/Magazine/Watson/watson.php).
AI Magazine, 
Fall, 2010
""",

_LINA15="""
Mario Linares-Vasquez, Gabriele Bavota,
Carlos Eduardo Bernal Cardenas, Rocco Oliveto, 
Massimiliano Di Penta, Denys Poshyvanyk,
[Optimizing energy consumption of guis in android apps: 
A multi-objective approach](http://www.cs.wm.edu/~denys/pubs/FSE15-GEMMA-CRC.pdf).
Proceedings of the 2015 10th Joint Meeting on 
Foundations of Software Engineering,
page 143-154, 2015
""",

_MURP06 ="""
Gail Murphy, Mik Kersten, 
[How are java software developers using the eclipse 
IDE](https://github.com/txt/se16/blob/master/todo/howDevelopersUseEclipseIDE.pdf)
IEEE Software, 
July 2006.
""",

_RACH14="""
Andy Rachleff,
[What You Need To Know About Vesting 
Stock](https://blog.wealthfront.com/vesting-stock-options/). 
Wealthfront blog, May 19, 2014.
""",

_SINO11="""
Steven Sinofsky, 
[Improvements in Windows 
Explorer](https://blogs.msdn.microsoft.com/b8/2011/08/29/improvements-in-windows-explorer).
Microsoft Developer Blog, August 29, 2011.
"""

)

print(re.compile(r'\b(' + '|'.join(d.keys()) + r')\b')
      .sub(lambda x: d[x.group()], sys.stdin.read()))
