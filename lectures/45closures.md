# Stateful Closures

_(from http://nathansjslessons.appspot.com/lesson?id=1070)_

A useful thing that closures can do is keep track of internal state. A closure is created when:

- The scope of some inner function refers to an outer scope's variables. 
- The inner function is passed around as a variable, carrying with it the inner scope _and_ the
  outer scope.

For example, here's a function that uses closures to create a counter.

```javascript
var makeCounter = function () {
    var count, f;
    count = 0;
    f = function () {
        count = count + 1;
        return count;
    };
    return f;
};
var counter = makeCounter();
/* counter is a function that takes no arguments
   and returns a count */
 
var a = counter(); // gets 1
var b = counter(); // gets 2
var c = counter(); // gets 3
 
var counter2 = makeCounter(); // create another one
var d = counter2(); // gets 1
var e = counter2(); // gets 2
var f = counter(); // gets 4 from first one
```

Where is the state kept? It's in the variable count in the outer scope. Why are there two copies? Each invocation of makeCounter creates a new scope for count, and the closure surrounding the inner function f captures that scope.

# Applications to SE

In the next para, objects DRY, layers, 3-tierd architecture, the 3.5 rule

## Parallelism

_Pure functions_ return values that are determined _only_ by their inputs (no 
reference to globals):

       x = plus(y,x)

So the whole execution of _plus_ can run in its own separate environment.  
Enter _closures_ .Bundle all you need into closures, call  n functions, each running on its
own CPU.

## Packages

Internal details hidden from the user of the package. Just use the published 

In a language called _Lua_, 

```lua
do
    local function checkComplex (c) # function local to inside this do-end block
      if not ((type(c) == "table")
         and tonumber(c.r) and tonumber(c.i)) then
        error("bad complex number", 3)
      end
    end
    
    local function new (r, i) return {r=r, i=i} end
    
    local function add (c1, c2)
      checkComplex(c1);
      checkComplex(c2);
      return new(c1.r + c2.r, c1.i + c2.i)
    end
    
    #other functions here
    
    complex = {  # when not marked "local", defaults to global
      new = new,
      add = add,
      sub = sub,
      mul = mul,
      div = div,
    }
end
```

Note that _checkComplex_ is not in the public interface.

Oh, and to call it:

```lua
require "complex"
C= complex
i = C.new(2,2)
j = C.new(10,0)
k = C.add(i,j)
```

## Objects, Classes

Once you've got closures and packages, you are nearly all the way to an OO language

##  Applications of Closures:  a 3-tiered architecture:

- Data : persistence storage; e.g. some SQL tools
- Model : the semantics; e.g. objects for _Person_,
  _Employee_, _Account_,  with methods like _promote_, 
 _hire_, etc
- Dialag: user interaction control; e.g. Employee Editor

Layers allows for:

- faster development (build the Model, then reuse someone's database layer)
- portability can take the same model and port it to different
platforms (different database or different GUIs on different platforms)

For years, this 3-tiered architecture was _the_ standard architecture and we did estimation as follows:

- Design the _"N"_ classes in the model
- Assume total number of classes is _N*3.5_ (each model class gets one friend in
  the database and dialog layer plus maybe some general utilities (half a class).
- Assume 20 lines per method and 5 methods per class.
- LOC =  _N*3.5*20*5_ = 350 lines*N model classes
- Track LOC per month with your local developers (including testing)
- Effort = LOC per month * LOC  = effort in months
      + Assume half that time is in testing (developers' local tests 
         and integrating  their code with other people)

More generally, think of the interactions between buttons pressed in the Dialog layer 
and the Model layer (all these services in the Dialog need Model information).

E.g. where to define, say the range of legal values for age of an employee?

- In _Person_ (0 to 120) in the model layer?
- In _PersonEditor_ in the dialog layer?
- As a trigger on updates in the database layer?

E.g. when you hit "ok" on the Employee Editor:

- You can't close the window till all the constraints check out;
- After close, you have to save the Employee... Dialog updates the list of Employees in the Model layer and maybe even update the Employee in the database layer.

So the "layers" aren't really separated: so much interaction

### Solutions

#### Rails, DRY

DRY= Don't Repeat Yourself.

Define it once, auto-propagate to the rest of the system.

Write the model, the auto-generate most of the Data and Dialog layer

- E.g. auto write the triggers on the database layers
- E.g. auto create on one database table for each business model.
- E.g. auto create on editor for each model object.

#### Closures

The model generates closures (functions to that, e.g. return False if the some contents
and not valid w.r.t. to model constraints).

At the Dialog layer, buttons have "call backs" ; closures generated by Model objects and
cached in Dialog layer.

Note that the Dialog does not need to know much about the model

- Just, when contents change, as the _constraints_ closure if it returns "True".

## Closure and Clojure

Closures should not be confused with `Clojure`.

+ Closures are a general programming construct that are used in many
  languages.
+ `Clojure` is a modern variant of `Lisp` that supports closures and
  concurrency via closures.

`Clojure` supports immutable variables-- variables which can only ever be
written once and once only. This seems like a strange idea- but it
actually simplifies debugging and concurrency (since once a variable
gets a value, it is a stable binding for the life of that variable).

To get a feel for how immutable variables and recursion changes
programming, consider the following standard example of iteration.
Note that is uses _mutable variables_ (ones that can be updated).

```
double result = 1.0;
for (int i = 0; i < y; i++)
{
  result = result * x;
}
```

Here's the equivalent call in `Clojure`.  Note that
we do not reset any variable, we just create news
one in some nested environment:


```clojure
(defn power
  ([x y] (power x y 1))
  ([x y current]
  (if (= y 0)
    current
    (if (> y 0)
      (recur x (- y 1) (* x current))
      (recur x (+ y 1) (/ current x))))))
```


Immutable variables and programming-by-recursion are widely-used
techniques in functional programming.  In the older languages,
they are depreciated since recursive calls to functions become
stack of recursive calls that eat up memory. However, for
languages that support _tail recursive optimization_ (like the we can replace
the recursive call with a loop back to the same function call on the current
stack (caveat: the tail recursive call has to be the _last_ thing
down in the function; i.e. we do  not need any space of additional
variables after that final recursive call).

Note that `Clojure` supports tail recursive optimization, sort of.
`Clojure` compiles into the Java Virtual Machine where such optimizations
are... complicated, which `Clojure` finesses uses certain technical tricks
[see here for details](http://goo.gl/2ZxvW3).
