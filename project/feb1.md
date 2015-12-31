_GIRLBOT


# Feb1 Project

[TOC]

____

# Goals

+ Document some problem _"P"_ with some user group _"U"_ using some **software** tool _"T"_ to achieve some goal _"G"_.
+ Guess what tools you will be using to fix that problem:
    + Identify  some _start up exercise_ (not connected to the March and April deliverables) where

As to selecting some _start up exercise_, this is just some moderately complex piece
of quick coding in _"T"_  which:

+ Your team can demonstrate competency  using _"T"_
+ Your team can practice working together, using Github.
+ Note: this should NOT be a complex task. Just something to show you have a base competency with your toolset.

As  to _documenting some problem_ you can either

+ _Find one_, as described in the literature (e.g. standard programmer errors
  [^errors1]<sup>,</sup>[^errors2]<sup>,</sup>[^errors3]<sup>,</sup>[^errors4];
+ Or _document one_, by asking some sample users (say, 5 of your friends) to perform some task  conducting
  "think aloud studies"[^protocol1]<sup>,</sup>[^protocol2] or some "exploratory study"[^protocol3].

[^errors1]: Andrew Ko, Brad Myers, [Development and Evaluation of a Model of
Programming Errors](http://repository.cmu.edu/cgi/viewcontent.cgi?article=1183&context=hcii).
HCCC'03, pr 28-31, 2003.

[^errors2]: R.C. Bryce, A. Cooley, A. Hansen, N. Hayrapetyan,
[A one year empirical study of student programming bugs](http://dx.doi.org/10.1109/FIE.2010.5673143)
in Frontiers in Education Conference (FIE), 2010. 

[^errors3]:
Amjad Altadmri, Neil C. C. Brown, 
[37 Million Compilations:
Investigating Novice Programming Mistakes in Large-Scale
Student Data](https://kar.kent.ac.uk/46742/1/fp1187-altadmri.pdf).
SIGCSE'15, March 4–7.

[^errors4]: [Conference on Human Factors in Computing Systems](http://chi2016.acm.org/wp/)
which is now decades old.

[^protocol1]: [Think aloud protocol
study](https://www.youtube.com/watch?v=tbKnFaW69e0)

[^protocol2]: [Think Aloud Demonstration and
Explanation](https://www.youtube.com/watch?v=gyXOe0Jl-fI)

[^protocol3]: See section 3.3 of [Designing Useful Tools for
Developers](http://www.cs.cmu.edu/~NatProg/papers/plateau2011-latoza.pdf).

___

# Key Points

You do **NOT** have to have the SOLUTION by Feb1:

+ You only need to, by Feb1,  have documented some PROBLEM

Also, come April, you will have to show that whatever tools you build _changes_ (and hopefully,
  improves), the pattern of errors for user
  group _"U"_ using some software tool _"T"_ to achieve some goal _"G"_.

+ So for January, your goal is to document the baseline problems
  (so you can show improvement in April).

____

# How to Have a Rotten Time

Do not study enough people doing enough things.

## Participant Studies

Rule of 12:

- 12 people, working 1 hour each on something
- 24 people, working 1/2 hour on something

- Feb1 is 23 days away. That's **more** than 3 weeks people. Start now! Now! NOW!
- Divide and conqueror:
      - You are in a group of four. Use that labor!
          - Define your _instruments_ such that N people can do it separately.
- Pick your subjects carefully
      - Document their prior experience with this task
- Define your instruments.
      - Define your "intro" speech
	  - Define an intro example (which you do in front of them)
	  - Make notes on what they do (?video them, ?tape them)
	  - When its all down, leave time for a debrief
		  - What did they find hardest?
		  - What did they find easiest?

## Literature reviews


Places to search for papers:

- IEEE Xplore
- ACM Digital Library
- Google Scholar

Note that these search engines have "cited by" fields so if you find a good paper, you can run forward in the literature looking for subsequent studies.

Pruning rules (heuristic, take with a grain of salt):

- Recent better than past
- Highly cited better than not

Methodology:

1. To grab an initial set of documents, what were your search terms? How many documents did it match (hint:  usually 100s to 1000s)
2. To prune the intial set , what were your strategies (extra search terms? quick scans of abstracts? number of citation counts? restrictions by year?)
3. After pruning, how many docs did you have (hint, usually dozens)?
4. How did you study the pruned docs (e.g. what particular questions did you ask of each document? how did you collate the results)?
5. What sanity checks were applied?
     - Did the literature review find known key articles in the field
     - Potentially, is it possible to operationalize fixed to  the identified problems? e.g. lack of domain knowledge very hard to operationalize; not closing matching brackets (easier to operationalize).
	   Recall the Royce[^errors2] results: 22% of their problems were deep semantic while the result were simple logic and syntax problems.

____

# What to Hand In

At start of class, Jan 12, hand in one page containing:

+ A statement of what _start up exercise_ you will complete by Feb1 using _what tool_
  (note: it is too hard or too simple, we will not approve it).
+ The names of your team, listed on the page, and entered into [this sheet](https://goo.gl/kOunui).

By Feb1:

+ Submit a 4+ page report using the [report format](report.md) describing
    + Your evidence for _P,U,T,G_ (defined below)
    + Your data collection methods
			- If participant observation, then write up your instruments
	        - If literature review, define how you collected your data by answering these questions:
			       - What were the review documents’s inclusion and exclusion criteria described and appropriate?
                   - Is the literature search likely to have covered all relevant studies? 
                   - Did the reviewers assess the quality/validity of the included studies? (e.g. citations counts, recency)
                   - Were the basic data/studies adequately described? (hint: see list of 5 above).
    + Your implementation of the _start up exercise_ (with some sample output to show
	  that you can get anything working with those tools).
	      + Note: this should NOT be a complex task. Just something to show you have a base competency with your toolset.


What you will need to do, in the next few days:

+ Commit to some task;
+ Commit to some general software libraries within
  which you can customize a solution.

So think of some software-related task that some
people tend to mess up, a lot, and start thinking
how to document that problem and how, before April1,
you might be able to fix it.

____

# Pragmatics

Note that to succeed in this task, you have narrow
the focus as soon as possible; e.g. consider the
task of manually writing a web page and its associated errors:

+ Referencing an image or  style sheet that does not exist;
+ Number of closing list tags is less than the number of opening list tags;
+ etc.

For another task, consider  using a text editor to write a
timetable for a small high school.

- The text is a table with columns (for hours in the
  day) and rows (or rooms in the school) and each
  cell is the name of a class and a teacher.
- Mistakes in this format would be many fold including:
    - Forgetting to schedule a class;
    - Add a teacher twice to the same hour;
    - Giving teacher too many classes;
	- Making some class have to race across the
      campus between classes that are too far apart,
      etc.

The problem here, of course, is that the general
  text editor has no special knowledge of the thing
  it is editing. For example, with the schedule editor:
  
- It does not know the list of known teachers,
      distances between classes etc
- So we could declare that paragraph1 is a list of teachers,
- Paragraph2 is a list classes with distances to other classes
- etc

(Exercise for the reader: what are the errors associated with manual web page entry?)

With that special knowledge, an interactive editor
  could start marking, in red, problematic cell
  entries.
  
- That same editor could pop up a second window
      pane that keeps updating with the current list
      of errors
- In this approach, the editor contains a large
	  library of tiny code fragments, each one of
	  which is a _(pattern,errorReport)_ that prints
	  the _errorReport_ if the the _pattern_ is
	  satisfied. Note that as a side-effect of some
	  _patterns_ firing, some working memory might
	  be updated (e.g. list of teachers who are free
	  at a particular time).

Of course, there are 100 different ways to handle the above:

- Forget interactive text queries (to identify bad
  contents); instead use some macro language where
  every construct expands into a table cell while
  checking if any. Such macros can do things like (e.g.) demanding that when
  files/html tags are opened, they are always closed.
- Some structure editor that inputs a description of
  the _grammar_ of a school timetable, which drives
  the editting (so if we know that line 5 of the
  file is expanding some branch of the grammar, then
  query that part of the grammar and block any
  keystrokes that violate that part of the grammar.


## Some options for Editor Customizations

By the way, if you want to exploring
        customizations within an editor, there are
        many choices you can explore:
		
+ The usual ECLIPSE-based approaches (can get very complex, beware);
+ There are 100 Javascript text editors;
+ There are fewer, but perhaps somewhat simpler, LUA editors;
+ If you are feeling "old school" there is always EMACS (feeling LISP-ish?).
+ VIM has its own text language

More generally, with text editor
			  customizations, best to limit yourself
			  to pattern match/presentation stuff
			  with any editor's built-in
			  language. For working memory updates
			  (and any reasoning), work our how to
			  hook the text editor scripts into your
			  most productive language.

As to the macro approach, such macros are available in:

+ Julia,
+ Erlang/Elixir
+ LISP
