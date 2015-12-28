# Patterns

Experts are experts since they've learned patterns of useful behavior (fyi: expert = 5 patterns per day * 10 years)

# Warning: beware generalization-itis

YAGNI! (your aint gonna need it)

- but, sometimes,  YAGNI (you are gonna need it)
- Remember the Rule of 3
    - First time, just do it;
    - Second time, note you are doing it the second time;
	- Third time, now you are allowed to refactor to generalize.

# Patterns in chess:

- more space in the center
- open lines
- weak squares
- pawn majority, pawn minority
- two weak points to attack - the Principle of Two Weaknesses
- weak kingside
- weak queenside pawn structures
- inactive knight at the corner
- dead bishop
- weak isolated d-pawn
- insufficient piece coordination
- attacking mark
- free protected pawn
- bishop pair
- better minor piece in open position - bishop versus knight
- better minor piece in blocked position - knight versus bishop
- break through
- and others etc. 

e.g forking:

![](/_img/chessfork1.png)

![](/_img/chessfork2.png)

![](/_img/chessfork3.png)





In object design

<img width=500 src="/_img/chbrowser.png">

<img width=500 src="/_img/filebrowser.png">

<img width=500 src="/_img/compositebrowser.png">

<img width=500 src="/_img/compositepattern.png">




<a href="/_img/gofpattern.jpg"><img width=500
src="/_img/gofpattern.jpg"></a>





Gang of Four (1994

Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides 

If you read this book, and you are not excited, then check your pulse. You're dead.

<img width=400 src="/_img/gofbook.png">


Patterns are a religion

<img width=400 src="/_img/onering.png">
 
"Patterns" in function programming
Functional programmers (Haskell, Clojure, F#, Lisp, Skill, Racket,….) make up 10 patterns for breakfast.

Cause its so easy (say what? OO makes some easy things hard?)

In LISP, one (and only one) recursive data type, the list which contains either
atoms
or another list

e.g. visitor pattern in functional (5 lines)

```lisp
(defun visitr (things f)
  "visitor patterns in functional programming"
  (if (atom things)
      (funcall f things)   ; then
      (dolist (one things) ; else do for each
	(visitr one f))))

(defun demo (&aux all)
  (let ((nastyComplexThing
	 '(a 
	   (b 1) 
	   c
	   (d e 
	      (f g 
		 (2 3 4)
		 )
	      h)
	   (i j)
	   (k
	    (l
	     (m
	      (n o p q r 
		 (s 5 6 7)
		 (t 8 9 )
		 u v w x y z)))))))
    (visitr nastyComplexThing
	    (lambda (x)
	      (if (numberp x)
		  (push x all))))
    all))

(print(demo))

; output
; (9 8 7 6 5 4 3 2 1)
```

# Maybe not Patterns, but Anti-Patterns

## e.g. Test Smell Bad Smells

From [Reichart et al. 2007][^reichhart].

1. Harvest the tests and collect a list of problems found in
the tests through manual inspection.
     + Due the large number of tests we did
       not analyze all of them, but rather focused on a sample of approximately 500
       test-methods.
2. Cluster the problems to identify commonalities and differences.
3. Distill the lessons in automatic queries in a tool called TestLint.
    + Static analysis of the test code and dynamic
      analysis including code manipulation and
      instrumentation.
4. Apply  queries on all the tests in our case study
    + Manually inspected the detected Test Smells to identify false positives.

![](/_img/badsmells1.gif)

![](/_img/badsmells2.png)

[^reichhart]:
Stefan Reichhart and Tudor Girba, Stephane Ducasse,
[Rule-based Assessment of Test Quality](http://www.jot.fm/issues/issue_2007_10/paper12/),
Journal of Object Technology,
6(9), October 2007




## e.g. Arthur Riel: OO design heuristics

**Chapter 2: Classes and Objects: The Building Blocks of the Object-Oriented Paradigm**

2.1: All data should be hidden within its class.

2.2: Users of a class must be dependent on its public interface, but a class should not be dependent on its users.

2.3: Minimize the number of messages in the protocol of a class.

2.4: Implement a minimal public interface which all classes understand. This interface should include operations such as copy (deep versus shallow), equality testing, pretty printing, parsing from a ASCII description, etc.

2.5: Do not put implementation details such as common-code private functions into the public interface of a class.

2.6: Do not clutter the public interface of a class with things that users of that class are not able to use or are not interested in using.

2.7: Classes should only exhibit nil or export coupling with other classes.

2.8: A class should capture one and only one key abstraction.

2.9: Keep related data and behavior in one place.

2.10: Spin off non-related information into another class (i.e. non-communicating behavior).

2.11: Be sure the abstraction that you model are classes and not simply the roles objects play.

**Chapter 3: Topologies of Action-Oriented Vs. Object-Oriented Applications**

3.1: Distribute system intelligence horizontally as uniformly as possible, i.e. the top level classes in a design should share the work uniformly.

3.2: Do not create god classes/objects in your system. Be very suspicious of an abstraction whose name contains Driver, Manager, System, or Subsystem.

3.3: Beware of classes that have many accessor methods defined in their public interface, many of them imply that related data and behavior are not being kept in one place.

3.4: Beware of classes which have too much non-communicating behavior, i.e. methods which operate on a proper subset of the data members of a class. God classes often exhibit lots of non-communicating behavior.

3.5: In applications which consist of an object-oriented model interacting with a user interface, the model should never be dependent on the interface. The interface should be dependent on the model.

3.6: Model the real world whenever possible. (This heuristic is often violated for reasons of system intelligence distribution, avoidance of god classes, and the keeping of related data and behavior in one place).

3.7: Eliminate irrelevant classes from your design.

3.8: Eliminate classes that are outside the system.

3.9: Do not turn an operation into a class.

3.10: Agent classes are often placed in the analysis model of an application.

**Chapter 4: The Relationships Between Classes and Objects**

4.1: Minimize the number of classes with which another class collaborates.

4.2: Minimize the number of message sends between a class and its collaborator.

4.3: Minimize the amount of collaboration between a class and its collaborator, i.e. the number of different messages sent.

4.4 : Minimize fanout in a class.

4.5: If a class contains objects of another class then the containing class should be sending messages to the contained objects.

4.6: Most of the methods defined on a class should be using most of the data members most of the time.

4.7: Classes should not contain more objects than a developer can fit in his or her short term memory. A favorite value for this number is six.

4.8: Distribute system intelligence vertically down narrow and deep containment hierarchies.

4.9: When implementing semantic constraints, it is best to implement them in terms of the class definition. Often this will lead to a proliferation of classes in which case the constraint must be implemented in the behavior of the class, usually, but not necessarily, in the constructor

4.10: When implementing semantic constraints in the constructor of a class, place the constraint test in the constructor as far down a containment hierarchy as the domain allows.

4.11: The semantic information on which a constraint is based is best placed in a central third-party object when that information is volatile.

4.12: The semantic information on which a constraint is based is best decentralized among the classes involved in the constraint when that information is stable.

4.13: A class must know what it contains, but it should never know who contains it.

4.14: Objects which share lexical scope -- those contained in the same containing class -- should not have uses relationships between them.

**Chapter 5: The Inheritance Relationship**

5.1: Inheritance should only be used to model a specialization hierarchy.

5.2: Derived classes must have knowledge of their base class by definition, but base classes should not know anything about their derived classes.

5.3: All data in a base class should be private, i.e. do not use protected data.

5.4: Theoretically, inheritance hierarchies should be deep, i.e. the deeper the better.

5.5: Pragmatically, inheritance hierarchies should be no deeper than an average person can keep in their short term memory. A popular value for this depth is six.

5.6: All abstract classes must be base classes.

5.7: All base classes should be abstract classes.

5.8: Factor the commonality of data, behavior, and/or interface as high as possible in the inheritance hierarchy.

5.9: If two or more classes only share common data (no common behavior) then that common data should be placed in a class which will be contained by each sharing class.

5.10: If two or more classes have common data and behavior (i.e. methods) then those classes should each inherit from a common base class which captures those data and methods.

5.11: If two or more classes only share common interface (i.e. messages, not methods) then they should inherit from a common base class only if they will be used polymorphically.

5.12: Explicit case analysis on the type of an object is usually an error, the designer should use polymorphism in most of these cases.

5.13: Explicit case analysis on the value of an attribute is often an error. The class should be decomposed into an inheritance hierarchy where each value of the attribute is transformed into a derived class.

5.14: Do not model the dynamic semantics of a class through the use of the inheritance relationship. An attempt to model dynamic semantics with a static semantic relationship will lead to a toggling of types at runtime.

5.15: Do not turn objects of a class into derived classes of the class. Be very suspicious of any derived class for which there is only one instance.

5.16: If you think you need to create new classes at runtime, take a step back and realize that what you are trying to create are objects. Now generalize these objects into a class.

5.17: It should be illegal for a derived class to override a base class method with a NOP method, i.e. a method which does nothing.

5.18: Do not confuse optional containment with the need for inheritance, modelling optional containment with inheritance will lead to a proliferation of classes.

5.19: When building an inheritance hierarchy try to construct reusable frameworks rather than reusable components.

**Chapter 6: Multiple Inheritance**

6.1: If you have an example of multiple inheritance
in your design, assume you have made a mistake and
prove otherwise.

6.2: Whenever there is inheritance in an
object-oriented design ask yourself two questions:
1) Am I a special type of the thing I'm inheriting
from? and 2) Is the thing I'm inheriting from part
of me?

6.3: Whenever you have found a multiple inheritance
relationship in a object-oriented design be sure
that no base class is actually a derived class of
another base class, i.e. accidental multiple
inheritance.

**Chapter 7: The Association Relationship**

7.1: When given a choice in an object-oriented
design between a containment relationship and an
association relationship, choose the containment
relationship.

**Chapter 8: Class-Specific Data and Behavior**

8.1: Do not use global data or functions to perform
bookkeeping information on the objects of a class,
class variables or methods should be used instead.

**Chapter 9: Physical Object-Oriented Design**

9.1: Object-oriented designers should never allow
physical design criteria to corrupt their logical
designs. However, very often physical design
criteria is used in the decision making process at
logical design time.

9.2: Do not change the state of an object without
going through its public interface.


