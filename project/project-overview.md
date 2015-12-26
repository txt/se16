<img align=right  src="http://sirteddybertie.com/wp-content/uploads/2013/07/5ScienceExperiments1-300x270.jpg">

# Project Overview

Good news: Your start-up has been bought out by the
very large software company Microoglebook and you
and your entire team has been acq-hired (at very
large salaries, with shares that vest[:vest] in three years).



[^vest]: _Vesting_ refers to the process by which an
employee earns her shares over time; e.g. monthly
over four years with a one-year _cliff_. That means
you earn the right to 1/48th of the shares you were
originally granted per month over four years (48
months), but you don’t get anything if you leave
prior to your one-year anniversary (and go over the
cliff). In other words on your one-year anniversary
you earn 1/4th of your stock and then vest an
additional 1/48th per month thereafter. For example
if you leave two years into your employment, you
would earn the right to exercise 1/2 your
options. The one-year cliff was created to protect
companies against issuing stock to bad hires, which
typically are not recognized at least until at least
a few months into their tenure. For more on vesting,
see[^rach14].

[^rach14]: _RACH14


Bad news: now you are the newbies working on new
projects with new people in long-established teams. And all those
old-timers and looking at you with that "so... what have you got?" expression.
To gain some credibility in those teams, you have to do something _impressive_.

Therefore, in this project you must:

- Document a problem with some user group doing some task;
- Propose two or three different ways to fix that problem;
- Implement those two or three different ways;
- Make a case that one of those ways should be adopted.

## How to do this project

Start now and form groups today. Your first major technical deliverable is due in 24 days-- and
this is a report that requires some research and (perhaps) some experimentation.
So [read about the deliverables, tonight](.)

All work will be in Github. Students are encouraged to
meet weekly then, otherwise, communicate regularly via Github issue reports.

The project is in two parts.

In part1:

- Feb1 will be some proof of technology competency by your tools with your team,
- Mar1 will be all your ideas coded up
- Apr1 will be a talk to the class (15 mins, sometime in April) as well as a 2000 word report (due  Apr1).

In part2, due  May1:

+ You will write a  decision
support tool that generates "reports of interest"
about patterns in the Github issues seen for the
work Jan to April.


## Why This Project?

Note that this is the new reality in software engineering:

- BEFORE, software engineers were machines that
  inputted requirements and outputed code;
- NOW, software engineers are like scientists,
  observing some phenomena, then proposing changes
  to change that phenomena.


Note how this is a profound change in how we develop systems:

+ About 20% of the features implemented in a software product are often or always used;
+ 64% of the features get rarely or never used.
     + E.g In Microsoft Windows Explorer[^sino11], a mere 10 commands make up 81% of the commands actually ever used.
     + Ditto with Eclipse[^murp06].

[^sino11]: $SINO11

[^murph06]: $MURP06

This means that substantial development effort is wasted. But even worse

+ It means that maintenance cost of the product (constituting the majority of the total product effort) is higher than needed.
+ This often implies delays in delivering products or lack of quality"

In this new reality, every feature is an experiment

+ The key to a running a lean enterprise is to "take an experimental approach
  to product development".
+ In this view, no feature is likely to persist for very long
  without data justifying its existence.
  +  Previously, features choices were carefully considered and
  traded off. Those chosen were designed, built, and then delivered.
  + While agile processes would
allow for design changes during the development process, evidenced rarely supported
decisions.
  + With continuous deployment, every planned feature is treated as an experiment, of
    which some deployed features are allowed to die.
  + For example, on Netflix.com if not enough
people even hovered over a new feature, then a new experiment might move the element to a
new location on the screen.
+ If all experiments showed a lack of interest, the new feature would
ultimately be deleted.

Experimentation may begin even before a feature is fully designed. For example:

+ if a developer
at Netflix wanted to make improvements to the queue feature, a developer might first gather
data related to how many people use queues. The developer would first try increasing clicks on
the queue by performing several A/B experiments.
+ After some initial prototyping, the developer
would next start targeting a small segment of users who currently are watching movies put into
queues in order to validate that the enhancement can improve watch frequency.
+ Then, the new
enhancement would be deployed to users who place movies in queues, but do not watch them.
+ Finally, with enough evidence collected, several hypotheses about customer behavior validated,
a feature can successfully proceed with wider development and deployment. 

