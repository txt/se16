# LUa

## A single data structure

There are few fundamental types in Lua and only one of them is designed to store others: tables. That means what in other languages would be arrays (sequences) and dictionaries (maps) are the same thing.

This is probably the only thing that really bothers me in Lua. Sequential types are something fundamentally different from associative types in my mind, and I have on several occasions wanted them to be distinct.

## First order functions, closure and true tail calls

Not going to teach a CS class in a Quora answer to explain what the first two are, they are found in other languages but Lua does have them. The last one, however, is actually pretty rare in dynamic languages. Some Lisps have it, but not, for instance, Python, Ruby or Clojure.

What it means in practice is that returning a call to a function does not make the execution stack grow. For instance, this code will work for any value of n (ignoring numeric issues) whereas in other languages you would have a stack overflow for large values of n:

```lua
local function f(n)
  if n < 1 then
    return true
  else
    return f(n-1)
  end
end
```

C isn’t that hard: void (*(*f[])())() defines f as an array of unspecified size, of pointers to functions that return pointers to functions that return void.


Why Pinterest just open-sourced new tools for the Elixir programming language
http://venturebeat.com/2015/12/18/pinterest-elixir/


https://h3rald.com/articles/10-programming-languages/

- Haskell
- Erlang
- Io
- PLT scheme
- Clojure
- Spueak
- OCaml
- Factor
- Lua
- Scala
- CoffeeScript: JavaScript made clean and simple
- Julia: Bringing speed to Python land
- Scala: Functional programming on the JVM

THe JVM.

<center>
<img
width=750
src="http://www.thesoftwareguild.com/wp-content/uploads/Programming-Languages-Infographic.jpg">
</center>

Programmers are mostly unaware
that that their programs (they use every day) are surrounded by structures.
_And that this is deliberate_ since the point of programming languages is
to write programs and _programs are things that make maths palatable_.

So every programmer is a mathematician (they just do need to know that).
But every programming language _designer_ needs to understand that maths
since it is that maths that defines what is (im)possible in that language.
  
Don't believe it? Well consider this:

+ Anytime you search for a string, you are probably using 
   [regular expressions](http://goo.gl/KASraS), which is a little language that
    specifies finite state machines.
+ Every time anyone tests a program, they usually doodle a finite state
  machine to clarify the intent of the program.
+ Every time anyone compiles a program, they are using type theory
  to explore the range of operations available for the program types.
+ Every time you pass a variable to a procedure/method/function,
  you are using something like
  Alfonzo Church's [lambda calculus](http://en.wikipedia.org/wiki/Lambda_calculus)
  to ensure that all things that use
  that variable access the right contents. 
+ When the first computers were built in the USA, they were written
  by engineers who literally pulled about the book on some
  uber maths called the [Turing machine](http://en.wikipedia.org/wiki/Turing_machine).
  And the Turing machine was created by Church's Ph.D. student, Alan Turing.
  + Any functional programmer uses McCarthy's 1960 memo on
  [Recursive Functions of Symbolic Expressions](http://www-formal.stanford.edu/jmc/recursive/recursive.html) 
  (which is slightly easier to read in 
  [Paul Graham's version](http://lib.store.yahoo.net/lib/paulgraham/jmc.ps) 
  or in [Peter Norvig's lispy code](http://norvig.com/lispy.html). 
+ Logic programmers literally program in mathematical logic.
+ If you use the _make_ tool, it find the _dependencies_ in your files
  and can run one parallel computation for each separate set.

The syntactic sugar of a program
consists of all the stuff that makes
the language usable:

+ Simplifications of complex processing;
+ Short-cuts to quickly code common idioms (e.g. macros,
  commonly-used control structures, class or function libraries for
  patterns or idioms);
+ Watch dogs that raise alerts if you do something
  wrong.
 
(By the way- its not _just_ syntactic sugar since
some "sugar" actual enables the clear expression of
ideas that would otherwise be too long to write down
or [too slow to run](http://unbox.org/open/trunk/310/13/fall/doc/96koller.html). Also, the watch dogs
can only report problems if they know
what a problem is- which means they
have to understand the purpose and limits of
the underlying maths.)

The maths defines what can be done, and what cannot
be done in that language. Such maths includes:

+ Closures
+ Dependencies
+ Logic
+ The predicates of logic programming
+ Functions
+ Objects
+ State machines
+ Etc

And underneath that maths is another layer of uber maths
([Turing machine](http://en.wikipedia.org/wiki/Turing_machine))
 that defines the ultimate limits of all the above. 

![](http://dberkholz-media.redmonk.com/dberkholz/files/2014/04/github_new_repos-custom.png)

Study: Language Choice Has Only a Small Impact on Code Quality


A [new study](http://macbeth.cs.ucdavis.edu/lang_study.pdf) conducted by computer scientists from UC Davis attempts to settle a long-term debate among developers: does the choice of a programming language impact code quality in a given project? The answer, according to the researchers, is yes, but that impact is very small.

The paper, titled "A Large Scale Study of Programming Languages and Code Quality in Github," analyzed 729 GitHub projects written in 17 different languages with 80 million lines of code and 1.5 million commits. They found that C, C++, JavaScript, Objective-C, PHP and Python tended to have slightly more errors than average, while Clojure, Haskell, Ruby, Scala and TypeScript were less likely than average to have bugs.

However, the report authors caution that the impact of the language choice was "quite small." Other factors, such as the size of the project and the size of the team, had a much bigger impact on code quality.


From the (in)famous [Tiobe index](http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html):

![](http://unbox.org/open/trunk/310/14/spring/doc/img/tiobe14.gif)

Languages, sorted by tags (in Stackoverflow.com) and lines changed (in Gitbuf)

+ http://langpop.corger.nl

What language will you use next? From
[Empirical Analysis of Programming Language Adoption
Leo A. Meyerovich Ariel Rabkin, OOPSLA 2013](http://www.eecs.berkeley.edu/~lmeyerov/projects/socioplt/papers/oopsla2013.pdf):

![](http://unbox.org/open/trunk/310/14/spring/doc/img/whatsnext.png)

["Learn Python" Overtakes "Learn Java" on Google Trends](https://dzone.com/articles/learn-python-overtakes-learn-java)

![](https://dzone.com/storage/temp/840751-learn-java-python.png)
