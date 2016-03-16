# Modeling


<img align=right src="http://skreened.com/render-product/g/a/i/gaidmmslucnfakiwiklu/image.skreened-t-shirt.white.w460h520b3z1.jpg">

[TOC]

Warning: the following lecture does NOT reflect the widespread consensus of folks in SE
community.

+ It started out as a lecture on notations for requirements engineering.
+ Then things got... nasty. It turned into
a HATE rave against excessive  of modeling in SE.
+ Just to be clear, I LOVE models, just not the crazed obsessive way they are needlessly elaborated in SE.

Oh, and since you ask, now that this is written, I feel much better.

______

## _model-itis_

Definition: the obsessive and needless over-elaboration of descriptions of a system

+ Models become out of data, no one uses them
+ Time is wasted maintaining dull models.

### Case study of _model-itis_: options for software configuration:

+ Understanding options are important, especially when combining different systems.
+ Models of config options illustrate the strengths and weaknesses of models.

Background: Kang's feature maps:

![eg](http://se16.unbox.org/_img/fm1.png)

![eg](http://se16.unbox.org/_img/fm2.png)

Some real world feature maps (for software you might be using today): 

![eg](http://se16.unbox.org/_img/pl1.png)

How many of those config options do people get:


![eg](http://se16.unbox.org/_img/pl4.png)

But how many do they actually use:

![eg](http://se16.unbox.org/_img/pl5.png)

And how many do they actually need:

- Current research at NCSU.
- Relevant options very small subset of total options
- Task: pick N, then 2N, then 4N, then 8N etc configurations till a data mining can take those N examples are generate a model withe less than 5% estimation error.
- Observation: with clever sampling methods (here called S1 and S2),
  N can be very very small:


![eg](http://se16.unbox.org/_img/pl6.png)

Lessons:

1. Possible to reason from very lightweight descriptions (so do not waste time on needless
elaborations)
2. Within a system of N variables there are a small number  _M &ll; N_ variables that
actually matter.
3. So model a little, run a little, focus on the variables that actually matter.

## Lightweight modeling Options

### Use Test Cases

Don't write in words, write in test cases.

### Use Config Options

Take the Parnas route

+ Do not offer models of the internal structure
+ Instead, just model the interfaces
+ When mashing up N tools, drive things via the config files of those tools.
+ E.g. the above study


### Don't Document Code, Document Data

Code changes all the time.

But what can matter just as much is the data the code is applied too.

<img src="http://www.danielauener.com/wp-content/uploads/2012/11/erauthors.png">

<img src="http://i.stack.imgur.com/giz3A.png" width=500>

Note for the above:

- Diagram that can be directly implemented in SQL tools (design straight to running code! hooray!)
- Really only recommended for simple apps
- In the land of the app, have to model functionality etc. Also, with RESTFUL interfaces,
  who cares about the internals? Its just the interface man!

________

# The OO Approach




# A Heavyweight Notation: Unified Modeling Language

Full disclosure: Lecturer made a lot on money in the 19XXs teaching UML.

Lot of money in selling industrial design tools.

- To broaden market, unify design notations

Its just a notation, not  a magic way to clarify design discussions

- In fact, it can be harmful since it allows you encode _one_ model and not multiple possible version

Best to understand UML as "notation envy" from ER.

Also, beware of class-itis (excessive generation of classes)


<iframe width="420" height="315" src="https://www.youtube.com/embed/o9pEzgHorH0" frameborder="0" allowfullscreen></iframe>


### UML Details

<a href="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/OO_Modeling_languages_history.jpg/1024px-OO_Modeling_languages_history.jpg"><img width=600 src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/OO_Modeling_languages_history.jpg/1024px-OO_Modeling_languages_history.jpg"></a>

![eg](http://agilemodeling.com/images/models/classDiagramSketch.JPG)

### UNL Critique

<a href="http://se16.unbox.org/_img/uml.pdf">Details</a>

- "There's also a danger when people believe that
  UML is a formal enough notation that they can
  specify precisely what they mean. This leads to
  people who on the one hand are aware that natural
  languages are always ambiguous but on the other
  hand believe that because the UML is a (more or
  less) formal syntax it eliminates ambiguity."
- "I've just finished teaching a week-long UML course
   and one of the points that came out of it was the
realisation that it's very hard to precisely specify
semantics with diagrams. There are long debates
about how to interpret associations (such as the
difference between the <<import> and <<access>>
stereotypes) or when to use a dependency or
one-directional association. Sooner or later people
fall back to natural language text to
illustrate/elucidate the diagrams. Then we're in a
position where we are specifying the same thing
twice. Once in the diagram and again in the
accompanying text."

If you must use UML...

+ Don't add gets/setters to class methods
+ If there is a relationship classX to classY, don't add relationship variables to X,Y. Instead connect them with a line and lable if with a line.

Consider not writing classes:

### Ultra-lightweight





### Ulta-lightweight OO

CRC cards

<img width=500 src="http://www.inf.ed.ac.uk/teaching/courses/inf1/op/Tutorials/2008/blank-crc.png">

<img width=500 src="http://www.c-jump.com/CIT73/Week09/images/crc_card3.png">

<iframe width="560" height="315" src="https://www.youtube.com/embed/5IpsMwxL37k" frameborder="0" allowfullscreen></iframe>


## Alternatives

Don't write How, write What.

Which takes us to requirements engineering.....

