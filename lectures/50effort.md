# Effort Estimation

[TOC]

How much effort does it take to build software? Is
this an important question? Is this an answerable question?

According to the extensive systematic review by
Jorgensen and Shepperd[^Js07], developing new
estimation models is the biggest research topic in
SEE since 1980s.


[^Js07]: M. Jorgensen and M. Shepperd, "A Systematic
Review of Software Development Cost Estimation
Studies," IEEE Trans. Software Eng., vol. 33, no. 1,
pp. 33-53, Jan. 2007.

Over or underestimation of software development
effort can lead to undesirable results:
Underestimation results in schedule and budget
overruns, which may cause project cancellation.
Overestimation hinders the acceptance of promising
ideas, thus threatening organizational
competitiveness.

When projects start running out of budget, bad things happen.
The first thing to go is all pretense of quality assurance
Finally, the whole project can get canceled.

e.g. Software to control shuttle refurbishment "To
gain control over its finances, NASA last week
scuttled a new checkout and launch control system
(CLCS) for the space shuttle.  A recent assessment
of the CLCS, which the space agency originally
estimated would cost $206 million to field,
estimated that costs would swell to between $488
million and $533 million by the time the project was
completed.  – June 11 2003, Computer News

![clsc](/_img/clsc.png)


____

## The Problem

### Problem1: Uncertainty

We don't know how hard it will be to build software,
until we build it.

![boehmEstimation](/_img/boehmEstimation.png)

Early lifecycle estimates can be wrong, by a large factor:

- plus or minus a factor of four.
- e.g The  ballooning software costs of JPL's Mission Science Laboratory
recently forced a two-year launch delay.


So, what to do?

Note that it is hard to separate the _estimation problem_
from the _project management_ problem since:

- Once I tell you it will cost $X;
- Your next question is always "but can you do it any cheaper?".

So the following lecture on _estimation_ is also about _management_.

### Problem2: Better,Faster,Cheaper (pick any two)

Estimation is a multi-goal optimization problem. Project
_effort_ is connected to project delivery _date_ to
project _quality_.

So, better, faster, cheaper, pick any two:

- Deliver faster, spend less money? Prepare for more defects.
- Deliver faster with fewer defects? Stand by to spend lots more
  (e.g. on hyper-quality programmers).
- Fewer defects, spend less money? You'll need to reign in
scope.

### Problem #3: Relucatance to Learn from Experience

Passos et al.:

+ many commercial software
  engineers generalize from their first few projects
  to all future projects [^Pb13].

Jorgensen & Gruschke:

+ commercial estimation
  “gurus” rarely use lessons from past projects
  to improve their future estimates [^Jg09].

When engineers fail to revise their beliefs, this
  leads to poor estimates (see examples
  in [^Jg09]).

[^Pb13]: Carol Passos, Ana Paula Braun, Daniela
S. Cruzes, and Manoel Mendonca. Analyzing the impact
of beliefs in software project practices. In
ESEM’11, 2011.
[^Jg09]: M. Jørgensen and
T.M. Gruschke. The impact of lessons learned
sessions on effort estimation and uncertainty
assessments. Software Engineering, IEEE Transactions
on, 35(3):368 –383, May-June 2009


## Solutions

For details on all the following, see below.

Strategies

- _Feature maturity_ :
  don't estimate software, reward delivery.
- _Big bang_         :
  estimate at the start to allocate resources
- _Spiral_ : project plan includes "stop!
    its not working!" points
- _Many bangs_       :
   continuous small estimation (e.g. local stories,
   active learning)
- _Lie_ : invent some nonsense number to make your
  manager happy
- _Don't estimate_ : the #noestiamtion camp.
  But really they do estimate (but more with _many bangs_
  and not just  _Big Bang_).

Tactics (so many; here's a sample):

- _Parametric_ : fit to an pre-guest distribution;
                 e.g. COCOMO
- _Case-Based Reasoning_ : new estimates are variations of old
              (but similar examples)
- _Planning poker_ : Don't estimate, just rank
work most to least expensive
- _Ensemble_ : Multiple estimates, combined (e.g.
   top-down, bottom-up, bagging, boosting)
- _Stability studies_ : Do the sample "_N_" times
  using small variations in the assumptions.   

Methods

- _Delphi/Expert methods_ :  use human expertise
(possibly augmented with process guidelines, checklists, and data) to
generate predictions [^jorh09a]
      - good for producing one estimate, not a range of estimates)'
- _Algorithmic/Model-based methods_ : build models via data mining or
		via expert intuition then make use those models to make predictions about new
		projects e.g. data mining
      - good for finding the uncertainty in an estimate).		
- _Combo_ : both the above.

[^jorh09a]: Jørgensen, Magne, and Stein
Grimstad. "Software development effort estimation:
Demystifying and improving expert estimation."
Simula Research Laboratory-by thinking constantly
about it (2009): 381-404.

____

## Strategies

### Feature Maturity

- Large organizations with an existing product and cash flow
  work as follows.
- Productivity via social engineering
- Developers compete to get their new feature mature enough
  to add into existing platform.
- The "wining"
  developers are rewarded (financially at annual review time,
  with promotions) if their features make it in.
- Note: bad idea unless all new features are rigorously screened
        - i.e. the organization has a
          strong "culture of testing".
- e.g. Microsoft.

### Big Bang

- Traditional method for large government projects
      - estimate at the start to allocate resources.
      - e.g. NASA needed $3.2 Billion to build the
	    [Cassini Saturn probe](http://saturn.jpl.nasa.gov/faq/FAQMission/)
	    (percentage cost of the software is unknown)
- Needed when development part of very large resource
  allocations (e.g. CLCS)
- Standard practice is to build two estimates:
     - The one you show the client  (so you can
       get the estimate)
     - The real one (so if you get the work you know how
	   much trouble you are in if you get the work).
- Standard U.S. Government practice is to demand that
  estimates are audited via some  model (e.g. COCOMO, see below).
     - Note that Delphi-based methods would not satisfy the
       this government requirement.
- Major weakness:
     - If the scope or technology changes during the period
       of the project, then the big bang's estimates will
	   be wildly inaccurate.

### Spiral

In 1986 [^spiral] Barry Boehm proposed a
modification to the Waterfall model called the
[spiral model](https://www.dimap.ufrn.br/~jair/ES/artigos/SpiralModelBoehm.pdf).

[^spiral]: Boehm B, "A Spiral Model of Software Development and Enhancement", IEEE Computer, IEEE, 21(5):61-72, May 1988

Three important features:

1. These "prototypes" are MUCH bigger than agile SRUMS.
   Weeks to months to years of work.
2. After a few rounds of the spiral, project becomes
   a standard waterfall.
3. There is a "commit partition" (shown left hand side).
   Projects are canned if we get to the commit point, and
   some critical functionality is still not working.
   
![spiral](/_img/spiral.gif)

Note that Spiral assumes developers want to "spiral"
which in turn means that projects can be canceled without
developers losing income. E.g. more projects that coders
and if this one goes, they can jump to that one

+ Hard to go Spiral if you work for an external software
consultants who are struggling for jobs
+ Since any cancellation may be fatal to their plans.

### Many bangs


+  Make Starting Amount of Money Small; Deliver
   Working Software Often
      + J.B. Rainsberger, the author of jUnit Recipes,
          points out that his first solo software project was
          just like this. Rainsberger made no promises up
          front, offering instead to show working software
          every two weeks — and also allowing the client to
          fire him with as little as two weeks' notice.
+  Fund a Pilot That Delivers Working Software; Then Use Modeling to Forecast Schedule
      + If the effort involved for each piece of work
         averages within some reasonable deviation, the team
          can count the pieces of work accomplished per week
        and predict, in a sense, when the project will be
         done.
+  Move From Contract Negotiation to Partnership
      + Establish scope at the outset of a project, but it lets the customer adjust and plan specifics each week. Lets the  customer could steer to a place very different that the original
	   goal. The customer gets what it needs in the moment— not what it thought it needed six months ago.

### Don't estimate
  
Just work on projects until they don't
make sense, then change gears.

+ Makes
long-term predictions challenging;
+ But if you look
back over your team's last five-year plan, how
accurate was it, anyway?

A tempting for products that charge a
per-user, per-month fee that are already cash-flow positive.

+ I.e. If your organization makes enough money to run
          itself, and if you view time spent estimating as time not developing, then you might abandon
		  estimates and just write code. T

Not recommended when:

+ In a budget conscious environment
      + E.g. civil servants as managers mindful they are spending the public's money (not their own)
+ In a cost-cutting environment
	  + e.g. the bubble has burst and everyone is working on how to get on to the life rafts
+ In a CYA environment
	  + E.g. your organization out-sources to India and you are required, each year, to select next year's
      developers based on productivity rates seen this year.
	  + And if you get it wrong, everyone will know who made that decision.
+ When you are required to audit your cost decisions:
      + Some government procurement cycles require such an audit
      + And if you are being sued, then you really want
        evidence of a defensible estimate back at start of
        project.
             + A decision that turns out to be wrong, with the benefit of hindsight, can still
		       be defensible, if it can be shown that 
      + Hard to audit or understand an estimate when it does not exist or when it was made using
	    Delphi-based methods
	  

____

## Tactics

### Planning Poker

From Wikipedia:

![poker](https://upload.wikimedia.org/wikipedia/commons/e/eb/CrispPlanningPokerDeck.jpg)

+ Planning poker, also called Scrum poker, is a
  consensus-based, gamified technique for
  estimating,
+ Does not estimate, but it ranks 
      + members of the group make estimates by playing numbered cards face-down to the table,
        instead of speaking them aloud.
	  + cards were numbered by larger and larger numbers
		   e.g. 0, ½, 1, 2, 3, 5, 8, 13, 20, 40, 100, and optionally a
	  + The cards are revealed, and the estimates are then discussed.
	  +  By hiding the figures in this way, the group can avoid the cognitive bias of anchoring, where the first number spoken aloud sets a precedent for subsequent estimates.

Poorly studied. Only a handful of studies. Rare exception:

+ A study by
  Moløkken-Østvold and Haugen[^agile] found that
  [the] set of control tasks in the same project,
  estimated by individual experts, achieved similar
  estimation accuracy as the planning poker
  tasks. However, for both planning poker and the
  control group, measures of the median estimation
  bias indicated that both groups had unbiased
  estimates, as the typical estimated task was
  perfectly on target.


[^agile]: K Moløkken-Østvold, NC Haugen (10–13 April 2007). "Combining Estimates with Planning Poker—An Empirical Study". 18th Australian Software Engineering Conference (IEEE): 349–58. doi:10.1109/ASWEC.2007.15.
[^others]: Google scholar search of "software effort estimation", since 2012](https://goo.gl/kyjxVH)



### Parametric Analysis

#### How to do it

Collect data on some pre-defined set of values, map it into
a pre-defined parametric form.

Sounds crazy? Then maybe you want to use case-based
reasoning (see below).

#### The  COCOMO Parametric Form

The COCOMO [^cocomo] assumptions:

+ Effort exponentially proportional to lines of code.
+ "_a_" and "_b_" are tuning parameters for linear and exponential
  effects (respectively).
+ "_C_" is the sum of five scale factors 
+ "_D"_ is the product of 17 effort multipliers. For
nominal projects, these are all "1"

The COCOMO parametric form:

_Effort = a * KLOC<sup>(b + C/100)</sup> * D_


To understand this:

+ _Time_ counts calendar months from start to
  finish. Boehm states that one month of work is 152
  hours (and this includes development and management
  tasks).
+ _Effort_ is the total number of person hours on
  that task; e.g.  12 developers working for 1,000
  hours of elapsed _time_ require 12,000 hours of
  _effort_.

Note one curious feature in COCOMO

- Development costs do not include hardware costs.
- In 2016, this is a reasonable
assumption, give the low cost of modern computers.
- In decades past, not so much.

#### The COCOMO Pre-Define Values

E.g. here are the COCOMO set. Do not treat them
as gospel, just illustrative of the range of factors
that might influence a software project

[^cocomo]: Boehm, Barry W., Ray Madachy, and Bert
Steece. Software cost estimation with Cocomo II with
Cdrom. Prentice Hall PTR, 2000.

+ Scale Drivers
      + Precedentedness	 (have we done this before)
      + Development Flexibility	
      + Architecture/Risk Resolution
	    (anyone looked at module interfaces)
      + Team Cohesion	
+ Process Maturity
      + Product Attributes
      + Required Reliability	
      + Database Size	
      + Product Complexity	
      + Required Reuse	
      + Documentation	
+ Platform Attributes
      + Execution Time Constraint	
      + Main Storage Constraint	
      + Platform Volatility	
      + Personnel Attributes
+ Analyst Capability	
      + Programmer Capability
      + Personnel Continuity 
      + Applications Experience
      + Platform Experience	 
      + Language and Toolset Experience	
+ Project Attributes
      + Use of Software Tools	 
      + Multisite Development	 
      + Required Development Schedule

More details:

![cocomoParems](/_img/cocomoParams.png)

_____

Usual values:


```python
_  = None;  Coc2tunings = [[
#              vlow  low   nom   high  vhigh  xhigh   
# scale factors:
'Flex',        5.07, 4.05, 3.04, 2.03, 1.01,     _],[
'Pmat',        7.80, 6.24, 4.68, 3.12, 1.56,     _],[
'Prec',        6.20, 4.96, 3.72, 2.48, 1.24,     _],[
'Resl',        7.07, 5.65, 4.24, 2.83, 1.41,     _],[
'Team',        5.48, 4.38, 3.29, 2.19, 1.01,     _],[

# negative effort multipliers (more means faster)        
'acap',        1.42, 1.19, 1.00, 0.85, 0.71,    _],[
'aexp',        1.22, 1.10, 1.00, 0.88, 0.81,    _],[
'ltex',        1.20, 1.09, 1.00, 0.91, 0.84,    _],[
'pcap',        1.34, 1.15, 1.00, 0.88, 0.76,    _],[ 
'pcon',        1.29, 1.12, 1.00, 0.90, 0.81,    _],[
'plex',        1.19, 1.09, 1.00, 0.91, 0.85,    _],[
'sced',        1.43, 1.14, 1.00, 1.00, 1.00,    _],[ 
'site',        1.22, 1.09, 1.00, 0.93, 0.86, 0.80],[
'tool',        1.17, 1.09, 1.00, 0.90, 0.78,    _],[

# positive effort multipliers (more means slower)
'cplx',        0.73, 0.87, 1.00, 1.17, 1.34, 1.74],[
'data',           _, 0.90, 1.00, 1.14, 1.28,    _],[
'docu',        0.81, 0.91, 1.00, 1.11, 1.23,    _],[
'pvol',           _, 0.87, 1.00, 1.15, 1.30,    _],[
'rely',        0.82, 0.92, 1.00, 1.10, 1.26,    _],[
'ruse',           _, 0.95, 1.00, 1.07, 1.15, 1.24],[ 
'stor',           _,    _, 1.00, 1.05, 1.17, 1.46],[
'time',           _,    _, 1.00, 1.11, 1.29, 1.63]]
```

____



Code:

```python
def COCOMO2(project,  a = 2.94, b = 0.91,  # defaults
                      tunes= Coc2tunings): # defaults 
  sfs ems, kloc  = 0,1,22          
  scaleFactors, effortMultipliers = 5, 17
  
  for i in range(scaleFactors):
    sfs += tunes[i][project[i]]
  
  for i in range(effortMultipliers):
    j = i + scaleFactors
    ems *= tunes[j][project[j]]
	
  return a * ems * project[kloc] ** (b + 0.01*sfs)
```	

Many ways to tune _a_ and _b_: e.g. stochastic  chop:

1. Pick middle-range values for _a_,_b_
    - e.g. a=10
    - e.g. b=1
2. Pick large mutation values:
    - e.g. aDelta = 10
    - e.g. bDelta = 0.5
3. Pick an intial "restraining value"
    - e.g. restrain = 1
4. Set loop counter to 10
5. Decrement loop by 1. If now zero, exit
6. 20 times
    - Mutate them by plus/minus some mutation* a random number.
    - Estimate using equation on some hold out set
	- Set _a,b_ to the best (_a,b_) values (those
	that lead to least estimation error)
7. Restrain the mutation
    size by (say) 66%
	8. Go to 5

```python
def COCONUT(training,          # list of projects
            a=10, b=1,         # initial  (a,b) guess
            deltaA    = 10,    # range of "a" guesses 
            deltaB    = 0.5,   # range of "b" guesses
            depth     = 10     # max recursive calls
            constricting=0.66):# next time,guess less
  if depth > 0:
    useful,a1,b1= GUESSES(training,a,b,deltaA,deltaB)
    if useful: # only continue if something useful
      return COCONUT(training, 
                     a1, b1,  # our new next guess
                     deltaA * constricting,
                     deltaB * constricting,
                     depth - 1)
  return a,b

def GUESSES(training, a,b, deltaA, deltaB,
           repeats=20): # number of guesses
  useful, a1,b1,least,n = False, a,b, 10**32, 0
  while n < repeats:
    n += 1
    aGuess = a1 - deltaA + 2 * deltaA * rand()
    bGuess = b1 - deltaB + 2 * deltaB * rand()
    error  = ASSESS(training, aGuess, bGuess)
    if error < least: # found a new best guess
      useful,a1,b1,least = True,aGuess,bGuess,error
  return useful,a1,b1

def ASSESS(training, aGuess, bGuess):
   error = 0.0
   for project in training: # find error on training
     predicted = COCOMO2(project, aGuess, bGuess)
     actual    = effort(project)
     error    += abs(predicted - actual) / actual
   return error / len(training) # mean training error
```
	
### Case-Based Reasoning

#### How to do it

Is the above too ridiculous for you? Think there are too
many assumptions? Then you want reasoning by case-based reasoning.

(Which, incidently, lets us talk some about data mining.)

CBR seeks to emulate human recollection and adaptation
of past experiences in order to find solutions to current
problems. 

CBR was first motivated by appeals to human
cognition. According to Kolodner [^kol] and Shank
[^shank77], humans do not base their decisions on
complex reductive analysis, but on an instantaneous
survey of past experiences.  To say that another
way, according to CBR,

+ _humans  don't think,  they remember._

[^kol]: Janet Kolodner. 1993. Case-Based
Reasoning. Morgan Kaufmann Publishers Inc., San
Francisco, CA, USA.

[^shank77]: Schank, Roger C., and Robert
P. Abelson. Scripts, plans, goals, and
understanding: An inquiry into human knowledge
structures. Psychology Press, 2013.

CBR has several advantages.  Firstly, when the cache
of past cases is updated and appended with
additional cases, then a CBR system is instantly
updated to the latest findings.

Secondly, the output of a CBR is made on a
``case-by-case'' basis.  That is, CBR does not offer
some trite generalization over multiple
examples. Rather, the advice it gives is specialized
to the particular case being considered at the
current time.

CBR looks complicated


![cbr](http://image.slidesharecdn.com/cbrpemilihankegiatanorganisasiarifrohmadi372322-151207050336-lva1-app6892/95/casebased-reasoning-untuk-pemilihan-kegiatan-organisasi-mahasiswa-4-638.jpg?cb=1449464785)

But actually it very simple.

#### Example Effort Data

The is the very famous Albrecht[^albrecht] data set.

[^albrecht]: A. Albrecht and J. Gaffney, "Software
Function, Source Lines of Code, and Development
Effort Prediction: A Software Science Validation",
IEEE Transactions on Software Engineering
9(6):639-648.


The right hand column is the _dependent variable_
that shows many 1000s of hours it took to build
software.

Left-hand-side columns are the _independent variables_.
This data relates to the _function points_
of software systems written in the late 1970s, usually in COBOL or PL/1.
A function point is a unit of business functionality in
an information system. For example, the first project in
the following data uses:

- 25 inputs to the software from other projects;
- 28 outputs to external software;
- And passes or shares 15 master files to other projects.

Function points are useful in size estimation
for business applications (but we caution that their
value in scientific, real-time, and similar
algorithm-based applications is debatable).  On
completion, that first project was 15,000 lines of
code and took 3,600 hours to complete.  This
includes analysis, design, coding, testing, and
documentation.


```
 $Inputs, $Outputs, $Files, $Queries, $KLOC, $fpoints, $!Khours
      25,       28,     22,        4,    15,      500,      3.6
      70,       27,     12,        ?,    20,      428,     11.1
      69,      112,     39,       21,   110,     1572,     61.2
      61,       68,     11,        ?,    24,      694,     11.8
      28,       38,      9,       24,    96,      512,     15.8
      28,       41,     11,       16,    24,      417,      7.5
      41,       27,      5,       29,    57,      512,     10.8
      13,       19,     23,        ?,    28,      283,       10
      48,       66,     50,       13,    94,     1235,     38.1
      42,       57,      5,       12,    40,      606,     18.3
      34,       14,      5,        ?,    35,      205,        8
      25,      150,     60,       75,   130,     1750,    102.4
       7,       12,      8,       13,    40,      209,      4.1
      15,       15,      3,        6,     3,      199,      0.5
     193,       98,     36,       70,   318,     1902,    105.2
      40,       60,     12,       20,    54,      759,     21.1
      33,       17,      5,        8,    22,      224,      2.9
      45,       64,     16,       14,    48,      680,     12.9
      27,       20,      6,       24,    52,      400,      8.9
      17,       17,      5,       15,    30,      289,      4.9
      40,       60,     15,       20,    93,      794,       19
      10,       69,      9,        1,    62,      431,     28.8
      12,       15,     15,        ?,    29,      260,      6.1
      43,       40,     35,       20,    42,      682,       12
```

Our goal is to learn what independent variables predict for
what value of the dependent variable. That is:

- Given the above rows, and a new row (without an _khours_ measure),
how would we guess the development time?

To do this, using a distance function, we report the average
development times of the the "_k_" nearest things in the table.

+  k=1,3,5 are normal values
+ We will use k=1

This assumes that projects that are similar with
respect to the independent variables will be similar
with respect to their depdendent variables.

(Aside, do you buy that assumption?)

The standard distance function comes from David Aha, 1991[^aha]
and it uses a Euclidean measure. Given to rows X and Y
then the distance between the "_N_"  _independent variables_ is

     d(x,y) = sqrt(sum( (x<sub>i - y<sub>i)<sup>2</sup )) / sqrt(N)

[^aha]: D.Aha, D. Kibler, and M. Albert, 1991,
"Instance-Based Learning Algorithm", Machine
Learning} 6:37-66.

(Aside: why only do distance on the _independent variables_?)

Standard practice is to normalize all the values in each
column 0..1, min..max. For example, in _Inputs_, the min,max values
are 7, 192. So the first's column last value (43) gets normalized
to

    norm(43) = (43 - 7) / (192 - 17 + 0.0001 ) = 0.206

(We add 0.0001 to the demoninator to handle the weird case where min==max.).

Once the data is normalized, then _d(x,y)_ always
returns a number 0..1.  Such normalizing lets us
compute the distance between different scaled
numeric features. To see this problem, consider a
database which lists rocket speeds and astronaut
shoe sizes.  Even if an astronaut shoe size
increases by 50% from 8 to 12. That difference would
be lost when compared to rocket speeds (that can
range from zero to 41*10<sup>6</sup> meters per second). If
we normalize all numerics zero to one, then a 100%
change in shoe size (that can range from zero to 20)
will not be lost amongst any changes to the rocket
speed.

#### Results

The following shows _k=1_ results for nearest neighbor on Albrecht
data. This is a leave-one-out (LOO) experiment; i.e.

- For all rows,
- Test = the ith row
- Train = all other rows
- Reflect over the Train set to guesstimate a value for the Test

Errors are expressed in terms on the magnitude of relative error


     mre = 100 * abs(predicted - actual) / actual

The LOO experiment generates 24 MRE values (one for
each row). To get a sense of the range of errors, we
sort all of them and report the 25,50,75th
percentile in that error (which for a list of 24
sorted numbers are the values at 6, 12, and 18).

```
            percent MRE
           -------------------
           25th   50th   75th
albrecht   16     39      61
```

(Aside: why do we report a distribution and not just the mean value?)

That was so much fun: let's  do it for more data.
The site http://openscience.us/repo/effort
contains numerous effort estimation data sets. After rewriting five of those data sets
in the format of the above figure,
we re-ran the above code, and sorted the results by the median error.
4.95 seconds later, we saw the following:

```
            percent MRE
			-------------------
			 25th   50th   75th
     china   15     33     55
  albrecht   16     39     61
desharnais   22     39     65
    nasa93   15     39     83
     coc81   34     76    171

```
These results seems simple enough, but they offer many insightful lessons.


#### Lesson1. Size does not matter


I'm are often asked "how much data do we need before
we can learn good models?".  The answer is that we
have no answer. There is no magic number, no central
limit theorem for inductive engineering that
promises that (say) 100 examples are enough.

To see this, consider the following table showing
the rows and columns of the data used in
the above results. Notice anything strange about
these numbers?

```
  dataset    rows  colums
1 albrecht    24    7 
2 coc81       63   19
3 desharnais  81   12
4 nasa93      93   24
5 china      499   19
```

The error rate is not correlated to size.

+ The two data sets with the lowest errors
are _china and _albrecht_.
+ Yet _china_ and _albrecht_  are the smallest and largest data sets in our sample.

 To see
why this may be so,
consider  two data sets:

+ Data2 contains with two rows: a perfect example of sad person and
a perfect example of a happy person.
+ Data1000 contains 1,000 rows where the all the values are filled in at random.

Our nearest neighbor algorithm will always correctly
identify happy or sad people from Data2. The same
algorithm will rarely, if ever, get anything right
from Data1000}.

The lesson here is that the success of data mining
is not tied to the _size_.  Rather, it is linked to
the _structure_ within the data.

#### Lesson2: The Middle Does Not Matter Much

t can be very misleading
to just report  the middle value of the results generated by a data miner.

To see this, consider the large range performance
values seen above. All the errors show a large
variation around the median value. For example,
observe the huge middle fifty range for coc81 (34%
to 171%)

The lesson here is that data mining results are not point solutions. Rather, they
are distributions with (potentially) very large variability. When reporting
results to users, it is therefore necessary to report not just the central
tendancy of some results but also the variation around that central point. For example, our software effort estimation colleagues report their estimates
as the 50th to 75th percentile range.


#### Lesson3: The Real World is a Mess, Get Used to It.


Some degree of uncertainty
is inherent in the analysis of real world data.
Some users can handle that, but others are quite shocked by distributions like the above.

We have
spent years struggling to reduce the large performance ranges in
these data sets. For
the cognoscenti, we note that we explored the following technologies:
feature selection, hundreds of different learners, and outlier removal.
Very recently, we have seen that ensemble learning or
spectral clustering might be useful- but those results are so bleeding edge
that we hesitate to include them here.

Long story short: while not all data has performance ranges as large
as those seen in above,
such ranges
are inherent in real-world data.

Some users are shocked at such large uncertainties.
"How can we make plans about our projects," they complain,
"when the uncertainty
in the estimates is so large?". For these users, we have several answers:


_The diplomatic answer:_
"Our predictions are only as good as the data. As data matures,
we can make better predictions."

This answer imparts a sense
of partnership  of the data mining task to the users.
In a nutshell, it is saying "Us inductive engineers done the best we can with the data you gave us. With
your help and better data we can do better".

_The statistical answer:_
"These predictions come from a sampling process
and, hence, these conclusions are a distribution rather than a single point."

This answer is recommended for  users with some level
of statistical sophistication.

_The planning answer:_ "These are _prediction_ results and that is a different
task to _planning_"

With grad students at NcState, we are working on ways to
use data like the above to learn what to change. Surprisingly.
when applied to data like the above, the variance in the plan
predictions are much less than prediction.


_The organizational answer:_
"Contingency planning is a common feature in many  organizations."
That is,
 now that
the space of possibilities has been defined, the users can take considered steps
on how to handle those possibilities.

(My favorite:) _The [Mary Shafer](http://yarchive.net/air/perfect_safety.html) answer:_
"Insisting on (certainty) is for people who don't have the balls to
live in the real world."

(Aside: we never actually say this to users, but we might  mutter
it under our breath in meetings).

Mary Shafer is a retired NASA aerospace research engineer that worked on the SR-71 and the X-15.
She accepts risks as the price of exploration:

+  No matter what you do, it will never be perfectly, 100% risk-free
   to fly.  Or to drive, or to walk, or to do anything.
   One of our pilots here died when he waited too long to eject from a
   spinning aircraft.  He was wrong; he should have jumped out earlier.
   He failed in his duty, IMO.
   One of our engineers was walking his dog when a car driven by a kid
   jumped the curb and hit him.  Only his leg was broken.  But he walks
   his dog again, now.  Who know better than him the danger?
   There's no way to make life perfectly safe; you can't get out of it alive.

In Shafer's work,  risks and uncertainty are factors to enumerate
and explore.
She distinguishes between a careless disregard for risk
and managed risk:

+ I have asked myself ``Have I told everybody exactly what we're
   going to do and what the known risks are and are we agreed that
   these risks are acceptable''. When I can answer that "yes" I (will accept the risk).

The lesson here is that, like the organizational answer shown above,
 uncertainty is a factor that must be understood before it can be managed.

+ Large performance ranges  should  not be shunned or ignore.
+ Ideally,  they need to be exposed
and discussed at the highest level of management.

In practice, inductive engineers need
to know that some users are just not
ready for the truth about the inherent uncertainties in their environment. For such
users, we advise  patience and gentle tutoring.

## References
