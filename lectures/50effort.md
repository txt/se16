# Effort Estimation

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

## Problem #3: Relucatance to Learn from Experience

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
- _Analogy_ : new estimates are variations of old
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
        - Good for producing one estimate, not a range of estimates
- _Algorithmic/Model-based methods_ : build models via data mining or
		via expert intuition then make use those models to make predictions about new
projects e.g. data mining
        - Good for finding the uncertainty in an estimate.		
		- _Combo_ : both the above.

[^jorh09a]: Jørgensen, Magne, and Stein
Grimstad. "Software development effort estimation:
Demystifying and improving expert estimation."
Simula Research Laboratory-by thinking constantly
about it (2009): 381-404.


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
	  

## Planning Poker (from Wikipedia)

![poker](https://upload.wikimedia.org/wikipedia/commons/e/eb/CrispPlanningPokerDeck.jpg)

+ Planning poker, also called Scrum poker, is a
  consensus-based, gamified technique for
  estimating,
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
+ Where as other methods are extensively explored [^others]

[^agile]: K Moløkken-Østvold, NC Haugen (10–13 April 2007). "Combining Estimates with Planning Poker—An Empirical Study". 18th Australian Software Engineering Conference (IEEE): 349–58. doi:10.1109/ASWEC.2007.15.
[^others]: [Google scholar search of "software effort estimation", since 2012](https://goo.gl/kyjxVH)




## Parametric Analysis

Collect data on some pre-defined set of values.

E.g. here are the COCOMO set (

+ Scale Drivers
      + Precedentedness	 (have we done this before)
      + Development Flexibility	
      + Architecture/Risk Resolution  (anyone looked at module interfaces)
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


[cocomoParems](/_img/cocomoParams.png)

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
	
	



## Example of analytics (Culure2)


In a nearest neighbor approach, we search a database of {\em past projects}
for examples that are nearest the {\em current project}. 
We then apply the  heuristic that {\em the present is like the past}
and return the esitmate of the nearest past project.


References
===========


