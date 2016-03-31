# Review9: Week of Mar 24

## Visual Notation for Programming

1. Let us say that a 'useful diagram' is close to some code base. List two visual notations that are 'useful'. Justify your answer.
2. Define the main parts of a state chart. Give a small example of state chart diagram of a person waiting for an elevator.
3. Define the main parts of compartmental models. Give a small example using the scenario of filling your car with gasoline.
4. Define the main parts of ER diagram. Give a small example using the scenario of placing a book order on Amazon.com.
5. What are the limitations of compartmental models?
6. How is UML similar to ER diagrams?
7. How is UML not similar to ER diagrams?
8. How does compartmental model differ from UML?
9. Why it is bad to get the entity wrong early in the development cycle in ER diagrams?
10. What kind of visual notation is the following diagram? State and explain all of it's parts.
    
    ![](../_img/crc_ex.JPG)

11. Propose and draw a class diagram equivalent to the above diagram.
12. Why we should not build dialogs directly from the data?
13. When and for what purposes should you use visual notations?

## Prolog
1. Why prolog can be used in a mass distributed system easily?
2. What is clause reordering in Prolog? Why is it important? Give an example. What other languages uses clause reordering?
3. From the given facts below, write a function in Prolog to find a food's flavor.

        food_type(velveeta, cheese).
        food_type(ritz, cracker).
        food_type(spam, meat).
        food_type(sausage, meat).
        food_type(jolt, soda).
        food_type(twinkie, dessert).
        flavor(sweet, dessert).
        flavor(savory, meat).
        flavor(savory, cheese).
        flavor(sweet, soda).
    
    - Use your function to find the flavor of 'velveeta'.
    - Use your function to find the the foods of 'savory' flavor.
4. Consider the following facts and function in Prolog. Will the following two coloring result in 'Yes' or 'No' in Prolog?

        different(red, green). different(red, blue).
        different(green, red). different(green, blue).
        different(blue, red). different(blue, green).
        coloring(Alabama, Mississippi, Georgia, Tennessee, Florida) :-
            different(Mississippi, Tennessee),
            different(Mississippi, Alabama),
            different(Alabama, Tennessee),
            different(Alabama, Mississippi),
            different(Alabama, Georgia),
            different(Alabama, Florida),
            different(Georgia, Florida),
            different(Georgia, Tennessee).
            
        % Coloring 1
        Alabama = blue.
        Florida = green.
        Georgia = red.
        Mississippi = red.
        Tennessee = green.
        
        % Coloring 2
        Alabama = red.
        Florida = green.
        Georgia = green.
        Mississippi = red.
        Tennessee = blue.
    
5. Explain what the following prolog code does.

        append([], List, List).
        append([Head|Tail], List, [Head|Rest]) :- append(Tail, List, Rest).
        
    
6. `A predicate is not a function` - discuss.

## Requirements Engineering
1. What is requirements document? What are the properties of requirements document?
2. State the components of the requirements document structure and explain them.
3. Define functional requirements. Give an example.
4. Define non-functional requirements. Give an example.
5. Define product constraints. Give examples.
6. State and explain three types of product constraints.
7. What are the issues encountered in product requirements.
8. What are the identifiable requirements classes. Explain and give examples for each.
9. What is a stakeholder in software?
10. Why are stakeholders important when reasoning about software?
