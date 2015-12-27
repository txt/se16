<img align=right  src="http://sirteddybertie.com/wp-content/uploads/2013/07/5ScienceExperiments1-300x270.jpg">

# Term Project


[TOC]

____

## Background

### Introduction to Data-Driven Development

Increasingly, well-engineered software is being used
 by policy makers and researchers to better
 understand the world.  For example, in 2013 a Nobel
 Prize was awarded to chemists using software to
 explore fast chemical reactions. For that work, the
 Nobel Prize committee wrote
 ["Today the computer is just as important a
 tool for chemists as the test tube"](http://www.nobelprize.org/nobel_prizes/chemistry/laureates/2013/press.html).

Consequently, our
society is becoming increasingly reliant on
_data analytics_.
Many companies
  practice _data-driven policy development_ that
  is, the determination of organizational policies
  using extensive analysis of large data sets
  collected from large populations.
This is especially true in
 software engineering, where it is now routine for
 practitioners to treat every planned feature as an
 experiment, of which only a few are expected to
 survive. In this approach:

+ Key performance metrics are carefully monitored
  and analyzed to judge the progress of a
  feature[^facebook1]<sub>,</sub>[^facebook2].
+ Even simple design decisions such as the color of a link[^lina15]
  are chosen by the outcome of software experiments.

[^facebook1]:
For example, on Netflix.com if not enough people
even hovered over a new feature, then a new
experiment might move the element to a new location
on the screen. If all experiments showed a lack of
interest, the new feature would ultimately be
deleted.

[^facebook2]: For example: if a developer at Netflix
wanted to make improvements to the queue feature, a
developer might first gather data related to how
many people use queues. The developer would first
try increasing clicks on the queue by performing
several A/B experiments.  After some initial
prototyping, the developer would next start
targeting a small segment of users who currently are
watching movies put into queues in order to validate
that the enhancement can improve watch frequency.
Then, the new enhancement would be deployed to users
who place movies in queues, but do not watch them.
Finally, with enough evidence collected, several
hypotheses about customer behavior validated, a
feature can successfully proceed with wider
development and deployment.

[^lina15]: _LINA15

Note that _data-driven_ approach
solves a major problem in software engineering:

+ The historical record is that about 20% of the features implemented in a software product are often or always used;
+ For example, 64% of the features get rarely or never used.
     + E.g In Microsoft Windows Explorer[^sino11], a mere 10 commands make up 81% of the commands actually ever used.
     + Ditto with Eclipse[^murp06].

[^sino11]: _SINO11

[^murp06]: _MURP06

Note that this means that substantial development
effort is wasted. But even worse

+ It means that maintenance cost of the product
  (constituting the majority of the total product
  effort) is higher than needed.
+ This often implies delays in delivering products or lack of quality.

### Pragmatics

+ Before _data analytics_ comes _data_;
     + before _data_ comes _data collection_;
          + before _data collection_ comes _goals_
	        (that guide the data collection).

So this project we walk from goals to collection to data to analytics.

+ Pragmatically,  takes a while
  to manage (goals,collection,data) so most of this
  project's effort will be on goals,collection,data
+ But we'll do a little analytics.

_____

## So Here's the Set Up

Good news: Your start-up has been bought out by the
very large software company Microoglebook and you
and your entire team has been acq-hired (at very
large salaries, with shares that vest[^vest] in
three years).


[^vest]: _Vesting_ refers to the process by which an
employee earns her shares over time; e.g. monthly
over four years with a one-year _cliff_. That means
you earn the right to 1/48th of the shares you were
originally granted per month over four years (48
months), but you don't get anything if you leave
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
projects with new people in long-established
teams. And all those old-timers and looking at you
with that "so... what have you got?" expression.  To
gain some credibility in those teams, you have to do
something _impressive_.

Therefore, in this project you must:

- Document a problem with some user group doing some task;
- Propose two or three different ways to fix that problem;
- Implement those two or three different ways;
- Make a case that one of those ways should be adopted.

____

## How to do this project

Start now and form groups today. Your first major technical deliverable is due in 24 days-- and
this is a report that requires some research and (perhaps) some experimentation.
So [read about the deliverables, tonight](.)

All work will be in the public general Github repository (not the NC State one)

Students are required to
meet weekly then, as far as possible, work separately and
communicate via Github issue reports[^issues].

+ Exception:  _Tutorial sessions_ (where person X walks person Y through some technology) are best done face to face. 

[^issues]: Github issues: [tutorial](https://guides.github.com/features/issues/)
and [A simple styleguide for tagging Github issues](https://robinpowered.com/blog/best-practice-system-for-organizing-and-tagging-github-issues/).

The project is in two parts:

1. Jan,Feb,Mar: Build some code 
2. Apr: Reflect on how teams build code.
    + Write queries to Github issue tracking that detect project _bad smells_ (in the patterns of issues and commits for
      Csc510 2016 students).



In part1:

- Feb1 will be (a) some documentation of some
  user problem and (b) some proof of technology competency
  by your tools with your team,
- Mar1 will be all your ideas coded up
- Apr1 will the results of assessing how well your
  tools work. This sill be in two parts:
      + A talk to the class (15 mins, sometime in April);
      + A report (due  Apr1).

In part2, due  May1:

+ You will write a  decision
support tool that generates "reports of interest"
about patterns in the Github issues seen for the
work Jan to April
+ You will submit a report on that work.

**(IMPORTANT NOTE: You get _more_ marks by finding bad smells in other projects. That said,  you won't get  _less_ marks if someone finds bad smells in your project.)**

##	What to Hand in

1. Each group will write their files and commit their pdf files to a public Github repository.
2. For each such repo, add collaborators _timm_ and _shaowns_.
3. The url of those Githubs will then be written to 

