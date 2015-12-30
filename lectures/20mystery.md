<img align=right width=400
     src="http://www.bookcountry.com/uploadedImages/Book_Country/Read_and_Review/Books/Genre_Map/Young_Adult/YA_Mystery_Thriller/YA_Mystery_Thriller.png?n=4014">

# The Great Mystery

It seems so unlikely that software ever works.

I'm not saying that software never crashes, cause it surely does:

+ [http://en.wikipedia.org/wiki/List_of_software_bugs](http://en.wikipedia.org/wiki/List_of_software_bugs)
+ [http://catless.ncl.ac.uk/Risks/](http://catless.ncl.ac.uk/Risks/)

And some of those crashes can be  spectacular and disasterous

+ A bug in the code controlling the Therac-25 radiation therapy machine was directly responsible for at least five patient deaths in the 1980s when it administered excessive quantities of X-rays.
+ The Vancouver Stock Exchange index had large errors due to repeated rounding. In January 1982 the index was initialized at 1000 and subsequently updated and truncated to three decimal places on each trade. This was done about 3000 times a day. The accumulated truncations led to an erroneous loss of around 25 points per month. Over the weekend of November 25-28, 1983, the error was corrected, raising the value of the index from its Friday closing figure of 524.811 to 1098.892.
+ A bug in floating point handling of the Ariane 5 rocket (which was worth, with its cargo,
$500 million) meant that...

<center>
<iframe width="700" height="5255" src="https://www.youtube.com/embed/gp_D8r-2hwk" frameborder="0" allowfullscreen></iframe>
</center>

By why doesn't software crash more often? How does it even work in the first place?

+ Consider software with 300 booleans.
+ Internal state space = _2<sup>300</sup>_ which is a number larger than
  _10<sup>23</sup>_, which is the number of stars in the known universe.
+ Think about that: that software is more complex than all the stars in the sky.

So the wonder is not that software fails (which it does, sometimes
at the worse possible time) but that _it ever works at all_. 

Some more maths:

+ A software system with _N_ modules has _N<sup>2</sup>_ possible intraconnections...
  each of must be designed and built and tested and maintained.
+ So theoretically, software effort increases _dramatically_ as software size increases.

But it does not:

+ Barry Boehm, data from 161 Southern Californian companies, 1990 to 2000.
+ Effort = a*LinesOfCode<sup>b</sup>
+ <em>b= 0.91 + 0.01*sum(5 factors)</em>
+ _Factors_ include risk manangement, team cohesion, etc. Range in
  value from 3.04 (median) to 7.8 (max)
+ So _sum(5 factors)_ is usually <em>5*3,04=15.2</em> and at most _5 * 7.8 = 39_ 
+ And _b = 1.062_ (usually) and, worse case, _b=1.3_.
+ Which means that, usually, effort grows very slowly on LOC.

<img width=400 src="/_img/effortVSLoc.png">

Q: Why is it so easy to build larger and larger software systems?

## Theory1: Humans are Brilliant?

Yeah, not so much...

+ [Voltaire](http://en.wikipedia.org/wiki/Voltaire):
  _It is a necessary consequence of our humanity. We are all fallible, and prone to error; let us then pardon each other's follies. This is the first principle of natural right._
+ Will Rogers: _It isn't what we don't know that gives us trouble, it's what we know that ain't so._
+ Wikipedia, long, long [list of cognitive biases](http://en.wikipedia.org/wiki/List_of_cognitive_biases). e.g.
[inattentional blindness](https://www.youtube.com/watch?v=vJG698U2Mvo)&nbsp;[^simo99].

[^simo99]: _SIMO99

## Theory2: Architecture

Theory. Coming soon.

## Theory3: What do you think?

Class exercise: what are the factors that make SE so successful?
