# Review6: Week of Feb 25

## Lazy Evaluation & goto
1. Below is a call to an ‘unless’ function, which prints “True” in the console if boolean_condition is true, “False” otherwise:

    ```unless(boolean_condition, write(“False”), write(“True”)```

    Why it is not possible to write functionality like this in traditional programming languages(C or Java)? Explain which programming concept can solve this problem and how.

2. Why is goto considered harmful? Give an example an example and explain. (ans: disrupts flow, invalidates the assumption of invariants in loops and conditional statements)

3. Give an example where goto can be useful.


## Closures
1. What is a closure? How is a closure created?
2. How can closures be applied? Give an example and explain.
3. There are many ways to create a closure. Describe one of those ways.
4. In the following code snippet, the last line of output is wrong. What should it generate (easy)? Explain exactly why it generates that output (harder)?

    ```
    var counter = (function() {
    
        var privateCounter = 0;
        
        function changeBy(val) {
            privateCounter += val;
        }
        
        return {
            increment: function() {
                changeBy(1);
            },
        
            decrement: function() {
                changeBy(-1);
            },
        
            value: function() {
                return privateCounter;
            }
        };
    })();
    
    console.log(counter.value()); // logs 0
    
    counter.increment();
    
    counter.increment();
    
    console.log(counter.value()); // logs 2
    
    counter.decrement();
    
    console.log(counter.value()); // logs 2
    ```
        
5. What features of object-oriented programming are demonstrated by the above example? What features of OO programming are missing from the above?


