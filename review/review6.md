# Review6: Week of Feb 18

## Design Patterns
1. What is the Composite pattern? Give an example of the Composite pattern and explain it's components.
2. What is the cascade-delete policy? How can it be applied to editing directories in file systems and data in SQL.
3. What is the Proxy design pattern? Give an example of the Proxy pattern and explain it's components.
4. How does Proxy handle DRY (Don't Repeat Yourself)?
5. What is the Singleton design pattern? Give an example of the Singleton pattern and explain it's components.
6. What are the underlying design pattern(s) common in the following browsing systems? Explain.

    <left><img src="/_img/chbrowser.png" width=300></left><right><img src="/_img/filebrowser.png" width=300></right>

7. What is DRY? What problem is anti-DRY in layered architechture?
8. What is the Visitor pattern? Give an example of the Visitor pattern and explain it's components.
9. How can polymorphism solve the problem of OO abuse bad smell in switch statements?

## Arthur Riel's OO Design Heuristics
1. Below are a list of OO design heuristics and a design statement. Describe how to fix the design so that it agrees with the heuristic:

    - (Heuristic 3.3) Beware of classes that have many accessor methods defined in their public interface, many of them imply that related data and behavior are not being kept in one place.
        - Design: One central class has 20 distinct methods for account creation, 60 distinct methods for account auditing, 50 distinct methods for writing objects to a SQL database.
    - (Heuristic 3.5) In applications which consist of an object-oriented model interacting with a user interface, the model should never be dependent on the interface. The interface should be dependent on the model.
        - Design: You need to use a commercial API that highly couples the business logic and GUI layers.
    - (Heuristic 5.1) Inheritance should only be used to model a specialization hierarchy.
        - Design: In your math API, integer class inherits from fractions class.
    - (Heuristic 5.8) Factor the commonality of data, behavior, and/or interface as high as possible in the inheritance hierarchy.
        - Design: The car management app you are creating, both Car and Truck class has an 'unlock' method with the same code.


## Anti-patterns
1. What are anti-patterns. List three.
2. For each of the anti-patterns below give three examples:
    - Bloated
    - OO-abusers
    - Dispensables