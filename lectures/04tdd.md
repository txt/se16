# Test-Driven Development

[TOC]

____

A common agile-practice: test-driven development; a.k.a. red-green-refactor (the following notes come from [http://goo.gl/3kVivq](http://goo.gl/3kVivq)):

+ TDD is a discipline for writing code, writing
  developer (unit) tests, and doing design work in
  an integrated approach. 
+ A small, fast-spinning motor.
+ Very short cycle that repeats over and over again.

# TDD, in 20 lines

Commercial TDD libraries contain extensive support for:

+ Managing large databases of test results;
+ DevOps tools for configuring, auto-building and auto-running code

But we can get a sense of TDD, just with a few lines of code.

<iframe width="700"  height=525 src="https://www.youtube.com/embed/nIonZ6-4nuU" frameborder="0" allowfullscreen></iframe>

Same code, in Python

+ Step1: install `rerun` with `pip install rerun`
+ Step2: write two files:
    + `xxxok.py` (which contains the tests for `xxx.py`)
    + `ok.py` (which contains the unit test engine)
+ Step3: `rerun 'python xxxok.py'`
    + Runs your tests, if anything in this directory (or its subs) are updated.

```python
# file = ok.py
from __future__ import print_function, division
import sys,traceback

def ok(*lst):
  print("### ",lst[0].__name__)
  for one in lst: unittest(one)
  return one

class unittest:
  tries = fails = 0  #  tracks the record so far
  @staticmethod
  def enough():
    print(unittest.score())
  @staticmethod
  def score():
    t = unittest.tries
    f = unittest.fails
    return "# TRIES= %s FAIL= %s %%PASS = %s%%"  % (
      t,f,int(round(t*100/(t+f+0.001))))
  def __init__(i,test):
    unittest.tries += 1
    try:
      test()
    except Exception,e:
      unittest.fails += 1
      i.report(test,e)
  def report(i,test,e):
    _, _, tb = sys.exc_info()
    f, line, fun, what = traceback.extract_tb(tb)[-1]
    print('{}: line {}, in {} ==> {} {}'.format(
         f, line, fun, what,e))
```

Example xxxok.py file:

```python
from ok import *

@ok
def _o():
  x=o(name='tim',age=55)
  x['name'] = 'tom'
  assert x.name == 'tom'
  x.name = 'tony'
  assert x.name == 'tony'
  assert str(x) == "o{'age': 55, 'name': 'tony'}"
```

Note:

- Unit tests as multiple functions in a file.
- Each of those functions contain `assert` statements.
- An `@ok` appears before all the test drivers.


# Details

+ **RED:** Start by thinking of a behavior you want
      the software to have which could be
      implemented by a few lines of code (fewer than
      five is a good target). Then write a test
      (also only a few lines of code) that will fail
      unless that behavior is present. Focus on:
      + The class behavior and its public
        interface - not how to implement the
            internals of the class.
      + The class user, not the class implementer - you may need to write the first few tests with class and method names that do not yet exist. Run the test suite, and watch the new test should fail. If the test either does not fail or fails in a different way than you intended, make the necessary fixes.
+ **GREEN:** Write just enough code to get the test to
pass. Focus on:
      + Getting something to work
      + Simplest possible implementation, rather than the most elegant solution (even hard-coded values are okay).
      + Reverting to known good code if the test continues to fail
      + If after a few attempts you can't make the test pass, consider starting over with a different test, possibly employing even less code. You are done with this step when the test passes.
+ **REFACTOR:** Now that the code does what you want, use refactoring to make the design right. Focus on:
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


# Assessment

## Advantages

Problems addressed by TDD (from Kent
Beck's [RIP TDD](https://www.facebook.com/notes/kent-beck/rip-tdd/750840194948847/)):

+ Over-engineering. I have a tendency to "throw in" functionality I "know" I'm "going to need". Making one red test green (along with the list of future tests) helps me implement just enough. I need to find a new way to stay focused.
+ API feedback. Get quick feedback about my API decisions.
+ Logic errors. Catches pesky errors.
+ Documentation. Communicate how I expect APIs to be used and to record what I was thinking during development.
+ Feeling overwhelmed. With TDD, even if I couldn't imagine an implementation I could almost always figure out how to write a test (finding the next "step up the mountain").
+ Separate interface from implementation thinking. I have a tendency to pollute API design decisions with implementation speculation. TDD separates the two levels of thinking while still providing rapid feedback between them.
+ Agreement. A way to be precise with a programming partner about what problem I'm solving.
+ Anxiety. TDD gives me an instantaneous "Is Everything Okay?" button.

## Disadvantages

"I get paid for code that works, not for tests, so
my philosophy is to test as little as possible to
reach a given level of confidence" – Kent Beck

+ James O Coplien [Why Most Unit Testing is Waste](http://www.rbcs-us.com/documents/Why-Most-Unit-Testing-is-Waste.pdf)
    + Notes that _unit tests_ are very small while _function tests_ (aka _system tests_)
      are much larger, much more complex.
	     + Much slower to run, not the kind of thing to give you instant feedback.
    + "Today however, my team told me the tests are
      more complex than the actual code."
	+ "Unit tests are unlikely to test more than one
      trillionth of the functionality of any given method in a
	  reasonable testing cycle. Get over it."
    + "If you find your testers splitting up
      functions to support the testing process,
      you’re destroying your system architecture and
      code comprehension along with it. **Test at a coarser level of granularity.**"
	+ "Tests should be designed with great care. Business
      people, rather than programmers, should design most
	  functional tests. Unit tests should be limited to those that
	  can be held up against some “third-party” success criteria."
	+ "If you have a large unit test mass, evaluate the feedback
      loops in your development process. Integrate code more
      frequently; reduce the build and integration times; cut the
      unit tests and go more for integration testing. "

Support for Coplien's case, from Google [^elba14]
     + Google runs billions of tests per year.
          + E.g. to test Python scripts, first it recompiles all of Python.
	 + Most tests are uninformative (less that 1% fail)
	      + So now they track the _effectiveness_ of each test (i.e. how many bugs they found
	      in the past)
		  + And they run, at higher frequency, those "informative" tests.

[^elba14]: _ELBA14
