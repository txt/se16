# Modeling

## How Not To Document

Don't write in words, write in test cases.


## Ultra lightweight Notation


CRC cards

<img width=500 src="http://www.inf.ed.ac.uk/teaching/courses/inf1/op/Tutorials/2008/blank-crc.png">

<img width=500 src="http://www.c-jump.com/CIT73/Week09/images/crc_card3.png">

<iframe width="560" height="315" src="https://www.youtube.com/embed/5IpsMwxL37k" frameborder="0" allowfullscreen></iframe>



# Ultra-heavyweight Notation: Unified Modeling Language

Full disclosure: Lecturer made a lot on money in the 19XXs teaching UML.

Lot of money in selling industrial design tools.

- TO broaden market, unify design notations

Its just a notation, not  a magic way to clarify design discussions

- In fact, it can be harmful since it allows you encode _one_ model and not multiple possible version

<a href="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/OO_Modeling_languages_history.jpg/1024px-OO_Modeling_languages_history.jpg"><img width=600 src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/OO_Modeling_languages_history.jpg/1024px-OO_Modeling_languages_history.jpg"></a>

![eg](http://agilemodeling.com/images/models/classDiagramSketch.JPG)

![samples](../_img/uml.pdf)

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

<iframe width="420" height="315" src="https://www.youtube.com/embed/o9pEzgHorH0" frameborder="0" allowfullscreen></iframe>

## Alternative:

Don't write How, write What.

Which takes us to requirements engineering.....

