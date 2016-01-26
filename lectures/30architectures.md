# Architectures

[TOC]


_____

The world is a big place

![](/_img/architecture.png)

Need **architectures** to divide complex parts into manageable bits.

____

# What is Architecture?

Something that lets you work alone:

- half the time

Team members 

- can be productive in isolation
- but know when they need to talk to others

Good fences make good neighbors!

<center><a href="/_img/fences.png"><img width=600 
src="/_img/fences.png"></a></center>

Large systems need large-scale organization:

- Allows large teams to work productivity on different parts of large constructions

<center><a href="/_img/archplane.png"><img width=600 
src="/_img/archplane.png"></a></center>


<center><a href="/_img/archplane2.png"><img width=600 
src="/_img/archplane2.png"></a></center>

## Traditional View of Architectures


Architecture the decisions you cannot change.

<center><a href="/_img/archbob.png"><img width=600 
src="/_img/archbob.png"></a></center>

Doug Schmidt:

- Architectural Evolution of DoD Combat Systemsm  Doug Schmidt, SEI blog, Nov 15, 2013
- "The Department of Defense (DoD) must move away from stove-piped solutions 
- "... towards a limited number of technical reference frameworks ..."
- "based on reusable hardware and software components and services"

<center><a href="/_img/archdod.png"><img width=750
src="/_img/archdod.png"></a></center>

## Another View of Architectures

Architectures =  the space within which we can conduct massive experimentation.

- e.g. the Queen Elizabeth aircraft carrier
- Life expectancy= 50 years
- A backbone within which 1000s of sub-systems can be
    - born,
    - evolved
    - replaced 


<center><a href="/_img/archliz.png"><img width=600 
src="/_img/archliz.png"></a></center>

<center><a href="/_img/archliz1.png"><img width=600 
src="/_img/archliz1.png"></a></center>

- e.g. package switching networks
     - Distributed packet-switching networks (On Distribute 
       Communications):  Rand memorandum RM-3103-PR, August 1964
     - An "architecture" that supports 1000 experiments within its framework
	   (e.g. the web). 

<center><a href="/_img/archpack.png"><img width=600 
src="/_img/archpack.png"></a></center>

- e.g. blackboard architectures in AI
      - The Blackboard Model of Problem Solving and the
        Evolution of Blackboard Architectures, H. Penny Ni, AI Magazine, 7(2), 1986.
      - How AI handled software engineering in the 1970s

<center><a href="/_img/archbb1.png"><img width=370 
src="/_img/archbb1.png"></a><a href="/_img/archbb2.png"><img width=370 
src="/_img/archbb2.png"></a></center>

<center><a href="/_img/archbb3.png"><img width=370 
src="/_img/archbb3.png"></a><a href="/_img/archbb4.png"><img width=370 
src="/_img/archbb4.png"></a></center>

- The lesson:
    - Some architectures are more change tolerant than others
    - E.g. LAMP is harder to change that MEAN
	
<center><a href="/_img/archlamp.png"><img width=700 
src="/_img/archlamp.png"></a></center>


- Mean:
       - M = MongoDB: a nonSQL DB(nested key-value pairs) ( death to SQL). No data traps
       - E = Express.js :  controller layer, directing application flow and marshaling data.
       - A = AngularJS : handles data presentation.
       - N = Node.js: an extensive javascript library (look ma, no operating system)
       - MEAN: one language up and down the stack (javascript)
             so (1) faster integrated testing;
             and (2) faster invention of new patterns.

<center><a href="/_img/archmean.png"><img width=700 
src="/_img/archmean.png"></a></center>

_____

# Classic Examples of Patterns


CRUD = create, read, update delete

From WIKIPEDIA

+ In computer programming, create, read, update and delete (as an acronym CRUD or possibly a backronym) (Sometimes called SCRUD with an "S" for Search) are the four basic functions of persistent storage.
+ Sometimes CRUD is expanded with the words retrieve instead of read, modify instead of update, or destroy instead of delete. It is also sometimes used to describe user interface conventions that facilitate viewing, searching, and changing information; often using computer-based forms and reports.
+ Used in many places including 
    + Databases
    + Distributed database services
    + RESTful interfaces

|Operation |	SQL |	HTTP |	DDS |
|---|---|---|---|
|Create|	INSERT	| PUT / POST	| write |
|Read (Retrieve) |	SELECT	|GET	|read / take|
|Update (Modify)|	UPDATE	|POST / PUT / PATCH|	write |
|Delete (Destroy)|	DELETE	|DELETE	| dispose|


Notice that _how_ CRUD is implemented is unknown. They are _interfaces_
to an unknowable underlying toolkit. [Modular design. Good practice.](/_pdf/kwic.pdf).

Classic pipe and filter. Used in UNIX (bad to
interaction across multiple pipes; good for easy
development, ease of maintenance)


![](/_img/pipe_and_filter.jpg)

Lots of small little programs, each focused on one task, ready to be combined in different ways:

```bash
# find biggest files changed in August
ls -l | grep "Aug" | sort +4n | more
```

Here's another example where `*ms` files contain a mark up language (think Latex or Mardown)
and

- `tbl` is an extension that handles tables
- `pic` is an extension that handles pictures
- `eqn` is an extension that handles equations
- `psduplex` handles printing on both sides of a page
- `lpr` is a device that actually prints the paper.

```
# apply the table (tbl) and picture (pic)
# and equation (eqn) to all the manuscript (.ms) files
	
cat *.ms |
tbl |
pic |
eqn |
troff -t  -ps |
psduplex -tumble |
lpr -Pps99 -h
```

LAMP = Linux apache mysql php (python)

![](/_img/LAMPStack.png)

After LAMP, comes MEAN (requires you to work in Javascript):

![](/_img/mean-stack.png)

MVC: good for tight/complex interaction. Complex to maintain

![](/_img/MVC-2.png)

Subject-observer. multiple views on one model

![](/_img/obser023.gif)

Looser collaboration with publish, subscribe

<img src="/_img/pub-sub.png" width=600>

_____


# Case Study: The Power of Architectures

Can architectures   make the complex comprehensible?. [Let's see](http://gogogarrett.sexy/programming-in-elixir-with-the-phoenix-framework-building-a-basic-CRUD-app/)

______

# Layers

The following notes are
from  the [MSDN](https://msdn.microsoft.com/en-us/library/ee658117.aspx) notes.

## Client/Server (layers=2)

Segregates the system into two applications, where
the client makes requests to the server. In many
cases, the server is a database with application
logic represented as stored procedures.

Advantages

+ Higher security. All data is stored on the server, which generally offers a greater control of security than client machines.
+ Centralized data access. Because data is stored only on the server, access and updates to the data are far easier to administer than in other architectural styles.
+ Ease of maintenance. Roles and responsibilities of a computing system are distributed among several servers that are known to each other through a network. This ensures that a client remains unaware and unaffected by a server repair, upgrade, or relocation.

## N-Tier / 3-Tier (layers=3)

Segregates functionality into separate segments in
much the same way as the layered style, but with
each segment being a tier located on a physically
separate computer.

## Layered Architecture (layers=3)

Partitions the concerns of the application into stacked groups (layers).

Advantages:

+ Abstraction. Layered architecture abstracts the
  view of the system as whole while providing enough
  detail to understand the roles and
  responsibilities of individual layers and the
  relationship between them.
+ Encapsulation. No assumptions need to be made
  about data types, methods and properties, or
  implementation during design, as these features
  are not exposed at layer boundaries.
+ Clearly defined functional layers. The separation
  between functionality in each layer is
  clear. Upper layers such as the presentation layer
  send commands to lower layers, such as the
  business and data layers, and may react to events
  in these layers, allowing data to flow both up and
  down between the layers.
+ High cohesion. Well-defined responsibility
  boundaries for each layer, and ensuring that each
  layer contains functionality directly related to
  the tasks of that layer, will help to maximize
  cohesion within the layer.
+ Reusable. Lower layers have no dependencies on
  higher layers, potentially allowing them to be
  reusable in other scenarios.
+ Loose coupling. Communication between layers is
  based on abstraction and events to provide loose
  coupling between layers.
+ Separation of concerns. Separated Presentation
  patterns divide UI processing concerns into
  distinct roles; for example, MVC has three roles:
  the Model, the View, and the Controller. The Model
  represents data (perhaps a domain model that
  includes business rules); the View represents the
  UI; and the Controller handles requests,
  manipulates the model, and performs other
  operations.
+ Event-based notification. The Observer pattern is
  commonly used to provide notifications to the View
  when data managed by the Model changes.
+ Delegated event handling. The controller handles
  events triggered from the UI controls in the View.

(Reality check: lately there has much movement away from LAMP towards
MEAN since LAMP is harder to modify (quickly) and test.)

____

# Parts

## Pipe-and-Filter


Recall the example above where

- `*ms` files contain a mark up language (think Latex or Mardown)
- `tbl` is an extension that handles tables
- `pic` is an extension that handles pictures
- `eqn` is an extension that handles equations
- `psduplex` handles printing on both sides of a page
- `lpr` is a device that actually prints the paper.

```
# apply the table (tbl) and picture (pic)
# and equation (eqn) to all the manuscript (.ms) files
	
cat *.ms |
tbl |
pic |
eqn |
troff -t  -ps |
psduplex -tumble |
lpr -Pps99 -h
```


From Wikipedia:

+ The pipeline concept was invented by Douglas
McIlroy and first described in the man pages of
Version 3 Unix.
+ One of the authors of the early
command shells, McIlroy noticed that much of the
time they were processing the output of one program
as the input to another.
+ His ideas were implemented in 1973 when ("in one
feverish night", wrote McIlroy) Ken Thompson added
the `pipe()` system call and pipes to the shell and
several utilities in Version 3 Unix.
+ "The next day",
McIlroy continued, "saw an unforgettable orgy of
one-liners as everybody joined in the excitement of
plumbing."
+ McIlroy also credits Thompson with the _"|"_
notation, which greatly simplified the description
of pipe syntax in Version 4.


Philosophy:

+ Write programs that do one thing and do it well. 
    + UNIX has hundreds of domain specific-languages, each doing one little task.
	+ e.g. ls, cp, rm, and (see below) bash, make.
+ Write programs to work together. 
+ Write programs to handle text streams, because that is a universal interface.
+ Small is beautiful.
+ Build a prototype as soon as possible.
+ Choose portability over efficiency.
+ Use shell scripts to increase leverage and portability.
+ Avoid captive user interfaces.
+ Make every program a filter.

The famous Mcllroy pipeline
          
+ Read a file of text, determine the n most frequently used words, and print out a sorted list of those words along with their frequencies.
    
    tr -cs A-Za-z '\n' |
    tr A-Z a-z |
    sort |
    uniq -c |
    sort -rn |
    sed ${1}q

+ BTW, the same thing in HASKELL:

    import qualified System
    import qualified Data.List as List
    import qualified Data.Char as Char
    import qualified Data.HashMap.Strict as HashMap
     
    main :: IO ()
    main = do
         [arg] <- System.getArgs
         text <- getContents
         let n = read arg
         putStr $ createReport n text
     
    createReport :: Int -> String -> String
    createReport n text =
         unlines $
         map (\(w, count) -> show count ++ " " ++ w) $
         take n $
         List.sortBy (flip compare) $
         map (\(w, count) -> (count, w)) $
         HashMap.toList $
         HashMap.fromListWith (+) $
         map (\w -> (w, 1)) $
         words $
         map Char.toLower $
         map (\c -> if Char.isLetter c then c else '\n') $
         text

Probably faster in HASKELL, but which would you rather code?

Notes from [David  March](http://www4.desales.edu/~dlm1/it533/class03/pipe.html):

Advantages:

+ Filters stand alone and can be treated as black
  boxes. This isolation of functionality helps to
  ensure quality attributes such as information
  hiding, high cohesion, modifiability, and reuse.
+ Filters interact with other components in limited
  ways. This connection simplicity helps to ensure
  low coupling.  Pipes and filters can be
  hierarchically composed. Higher order filters can
  be created from any combination of lower order
  pipes and filters.
+ The construction of the pipe and filter sequence
  can often be delayed until runtime (late
  binding). This permits a controller component to
  tailor a process based on the current state of the
  application.
+ Because the process performed by the filter is
  isolated from the other components in the system,
  it is relatively easy to run a pipe-and-filter
  system on parallel processors or in multiple
  threads on a single processor.

Disadvantages (Top) 

+ Because the problem is decomposed into sequential
  steps, a batch mentality is encouraged. It is
  difficult to create entire interactive
  applications using this style.
+ Filters often force the data to be represented in
  the lowest common denominator, typically byte or
  character streams. This means that if processing
  must be based on information tokens (words, lines,
  records), every filter may introduce overhead for
  parsing and unparsing the data stream.
+ If a filter can not produce any output until it
  has received all of its input, the filter will
  require a buffer of unlimited size. If fixed size
  buffers are used, the system could deadlock. A
  sort filter has this problem.

## Component-Based Architecture

Decomposes application design into reusable
functional or logical components that expose
well-defined communication interfaces.

Advantages (best case... not always realized...):

+ Reusable. Components are usually designed to be
  reused in different scenarios in different
  applications. However, some components may be
  designed for a specific task.
     + Ease of development. Components implement
       well-known interfaces to provide defined
       functionality, allowing development without
       impacting other parts of the system.
+ Replaceable. Components may be readily substituted
  with other similar components.
+ Ease of deployment. As new compatible versions
  become available, you can replace existing
  versions with no impact on the other components or
  the system as a whole.
+ Not context specific. Components are designed to
  operate in different environments and
  contexts. Specific information, such as state
  data, should be passed to the component instead of
  being included in or accessed by the component.
+ Extensible. A component can be extended from
  existing components to provide new behavior.
      + Reduced cost. The use of third-party
        components allows you to spread the cost of
        development and maintenance.
+ Encapsulated. Components expose interfaces that
  allow the caller to use its functionality, and do
  not reveal details of the internal processes or
  any internal variables or state.
+ Independent. Components are designed to have
  minimal dependencies on other
  components. Therefore components can be deployed
  into any appropriate environment without affecting
  other components or systems.

## Object-Oriented

A design paradigm based on division of
responsibilities for an application or system into
individual reusable and self-sufficient objects,
each containing the data and the behavior relevant
to the object.

Advantages:

+ See _Components_

_____


# Other

## Domain Driven Design

An object-oriented architectural style focused on
modeling a business domain and defining business
objects based on entities within the business
domain.

Advantages:

+ Communication. All parties within a development
  team can use the domain model and the entities it
  defines to communicate business knowledge and
  requirements using a common business domain
  language, without requiring technical jargon.
+ Extensible. The domain model is often modular and
  flexible, making it easy to update and extend as
  conditions and requirements change.

## Message Bus

An architecture style that prescribes use of a
software system that can receive and send messages
using one or more communication channels, so that
applications can interact without needing to know
specific details about each other.

Advantages:

+ Loose coupling. As long as applications expose a
  suitable interface for communication with the
  message bus, there is no dependency on the
  application itself, allowing changes, updates, and
  replacements that expose the same interface.
        + Message-oriented communications. All communication
          between applications is based on messages that use
          known schemas. 
+ Scalability. Multiple instances of the same
  application can be attached to the bus in order to
  handle multiple requests at the same time.
+ Complex processing logic. Complex operations can
  be executed by combining a set of smaller
  operations, each of which supports specific tasks,
  as part of a multistep itinerary.
+ Modifications to processing logic. Because
  interaction with the bus is based on common
  schemas and commands, you can insert or remove
  applications on the bus to change the logic that
  is used to process messages.
+ Integration with different environments. By using
  a message-based communication model based on
  common standards, you can interact with
  applications developed for different environments,
  such as Microsoft .NET and Java.

## Service-Oriented Architecture (SOA)

Refers to applications that expose and consume
functionality as a service using contracts and
messages.

Advantages:

+ Services are autonomous. Each service is
  maintained, developed, deployed, and versioned
  independently.
+ Services are distributable. Services can be
  located anywhere on a network, locally or
  remotely, as long as the network supports the
  required communication protocols.
+ Services are loosely coupled. Each service is
  independent of others, and can be replaced or
  updated without breaking applications that use it
  as long as the interface is still compatible.
+ Services share schema and contract, not
  class. Services share contracts and schemas when
  they communicate, not internal classes.
+ Compatibility is based on policy. Policy in this
  case means definition of features such as
  transport, protocol, and security.

## Etc, etc

Combinations, variants of the above (maybe with other stuff).




