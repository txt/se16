# Architectures

The world is a big place

![](/_img/architecture.png)

Classic pipe and filter. Used in UNIX (bad to interaction across multiple pipes; good for easy development, ease of maintenance)

![](/_img/ainfig05.gif)

LAMP = Linux apache mysql php (python)

![](/_img/LAMPStack.png)

After LAMP, comes MEAN (requires you to work in Javascript):

![](_img/meanstack.png)

MVC: good for tight/complex interaction. Complex to maintain

![](/_img/MVC-2.png)

Subject-observer. multiple views on one model

![](/_img/obser023.gif)

Looser collaboration with publish, subscribe

![](/_img/pub-sub.png)

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

# Parts

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




