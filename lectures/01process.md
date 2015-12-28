# Some Process Notes

Software development costs (from Brookes' Mythical Man Month[^brooks75] text).

+ 1/3 planning (requirements, design);
+ 1/6th coding;
+ 1/4 unit test (testing code written by one programmer);
+ 1/4 system test (test code assemblies built by _"N"_ programmers).

[^brooks75]: _BROO75

# Waterfall

The following notes come from
[blogs/invisiblethread](https://www.ibm.com/developerworks/community/blogs/invisiblethread/entry/beyond_devops_distributedops_noops_and_bizdevops?lang=en).

In the beginning was the
[waterfall model](/resources/70waterfall.pdf):

<center><a
href="/_img/process1.png"><img
width=700
src="/_img/process1.png"></a></center>

Royce 70's critique of waterfall[^royce70]:

+  "Unfortunately,  design iterations are never confined to the successive steps."
        + i.e. later tests can lead to changes to document very much upstream.

His solution? More documentation!

+  Write an overview document that is understandable,
   informative and current. Each and every worker
   must have an elemental understanding of the
   system. At least one person must have a deep
   understanding of the system which comes partially
   from having had to write an overview document.
+  How much documentation?" My own view is "quite a
   lot;" certainly more than most programmers,
   analysts, or program designers are willing to do
   if left to their own devices.

[^royce70]: _ROYC70

# The Agile Rebellion

The rebellion document, 2001 (death to paper-driven development):

<center><a href="http://agilemanifesto.org/"><img
   width=650
   src="/_img/agilemanifesto.png"></a></center>


<center><a
href="/_img/process2.png"><img
width=700
src="/_img/process2.png"></a></center>

Advantages of Agile model (from [http://goo.gl/n33v09](http://goo.gl/n33v09)):

+ Customer satisfaction by rapid, continuous delivery of useful software.
+ People and interactions are emphasized rather than
  process and tools. Customers, developers and
  testers constantly interact with each other.
+ Working software is delivered frequently (weeks rather than months).
+ Face-to-face conversation is a productive form of communication.
+ Close, daily cooperation between business people and developers.
+ Continuous attention to technical details and good design.
+ Regular adaptation to changing circumstances.
+ Even late changes in requirements are welcomed

Disadvantages of Agile model
(from [http://goo.gl/n33v09](http://goo.gl/n33v09)):

+ In case of some software deliverables, especially
  the large ones, it is difficult to assess the
  effort required at the beginning of the software
  development life cycle.
+ There is lack of emphasis on necessary designing
  and documentation.
+ The project can easily get taken off track if the
  customer representative is not clear what final
  outcome that they want.
+ Only senior programmers are capable of taking the
  kind of decisions required during the development
  process. Hence it can be harder for newbies to be agile,
  unless combined with experienced
  resources.

A common agile-practice: test-driven development; a.k.a. red-green-refactor (the following notes come from [http://goo.gl/3kVivq](http://goo.gl/3kVivq)):

+ TDD is a discipline for writing code, writing
  developer (unit) tests, and doing design work in
  an integrated approach. 
+ A small, fast-spinning motor.
+ Very short cycle that repeats over and over again.

+ Details:
    + RED: Start by thinking of a behavior you want
      the software to have which could be
      implemented by a few lines of code (fewer than
      five is a good target). Then write a test
      (also only a few lines of code) that will fail
      unless that behavior is present. Focus on:
             + The class behavior and its public
               interface - not how to implement the
               internals of the class.
             + The class user, not the class implementer - you may need to write the first few tests with class and method names that do not yet exist. Run the test suite, and watch the new test should fail. If the test either does not fail or fails in a different way than you intended, make the necessary fixes.
    + REEN: Write just enough code to get the test to
pass. Focus on:
             + Getting something to work
             + Simplest possible implementation, rather than the most elegant solution (even hard-coded values are okay).
             + Reverting to known good code if the test continues to fail
             + If after a few attempts you can't make the test pass, consider starting over with a different test, possibly employing even less code. You are done with this step when the test passes.
    + REFACTOR: Now that the code does what you want, use refactoring to make the design right. Focus on:
             + Making the code readable and eliminating duplication
             + Existing behavior (refactoring means changing the code without changing its behavior; adding new behavior requires writing a new [failing] test).
             + Working in small steps, running the tests each time.
 
The cycle then repeats with each new behavior you want to have. The entire cycle should take between 5-10 minutes.  A couple of last points to emphasize:

+ Tests are checked in with the rest of the code (they are essentially living documentation of the code)
+ Tests are run with every build
+ Some tests require accessing parts of a system
  that are not built yet. In that case, programmers
  build a _mock_, a fake bit of code that the same
  interfaces as the real code, but fake internal
  contents that just returns canned responses.

Note that TDD is also a communication tool between programmers.

+ If you want to understand someone else's code ...
+ ... start with the tests.


# After Agile

<center><a
href="/_img/process3.png"><img
width=700
src="/_img/process3.png"></a></center>


<center><a
href="/_img/process4.png"><img
width=700
src="/_img/process4.png"></a></center>


<center><a
href="/_img/process5.png"><img
width=700
src="/_img/process5.png"></a></center>



