<img align=right src="http://sirteddybertie.com/wp-content/uploads/2013/07/5ScienceExperiments1-300x270.jpg">

# Project Overview

Good news: Your start-up has been bought out by the
very large software company Microoglebook and you
and your entire team has been acq-hired (at very
large salaries, with shares that vest in two years).

Bad news: now you are the newbies working on new
projects with new people in long-established teams.
To gain some credibility in those teams, you have to do something _impressive_.

Therefore, in this project you must:

- Document a problem with some user group doing some task;
- Propose two or three different ways to fix that problem;
- Implement those two or three different ways;
- Make a case that one of those ways should be adopted.

## How to do this project

All work will be in Github. Students are encouraged to
meet weekly then, otherwise, communicate regularly via Github issue reports.

The project is in two parts.

In part1:

- Feb1 will be some proof of technology competency by your tools with your team,
- Mar1 will be all your ideas coded up
- Apr1 will be a talk to the class (15 mins, sometime in April) as well as a 2000 word report (due  Apr1).

In part2, due  May1, you will write a  decision
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

XXXX
telemetry first

## Notes

[^sino11]: Steven Sinofsky,
[Improvements in Windows Explorer](https://blogs.msdn.microsoft.com/b8/2011/08/29/improvements-in-windows-explorer).
Microsoft Developer Blog, August 29, 2011.


[^murp06]: Gail Murphy, Mik Kersten,
[How are java software developers using the eclipse IDE](https://github.com/txt/se16/blob/master/todo/howDevelopersUseEclipseIDE.pdf).
IEEE Software, July 2006.

