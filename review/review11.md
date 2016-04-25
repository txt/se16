# Review11: Week of April 7

## White-box Testing
1. Define the nodes in a control flow graph.
2. Define the nodes in a data flow graph.
3. Given the following program, draw the control flow graph for it.
    
        function P return INTEGER is
        begin
            X, Y, INTEGER;
            READ(X); READ(Y);
            while (X > 10) loop
                X := X - 10;
                exit when X = 10;
            end loop;
            if (Y < 20 and then X mod 2 = 0) then
                Y := Y + 20;
            else
                Y := Y - 20;
            end if;
            return 2*X + Y;
        end P

4. Given the following program, provide tests that gets you greater than 50% and less than 100% statemnet coverage.

        printSum(int a, int b) {
            int result = a + b;
            if (result > 0)
                printCol("red", result);
            else if (result < 0)
                printCol("blue", result);
            else
                printCol("green", result);
        }

5. Give an example where 100% statement coverage is required?
6. In the above program, what statement coverage is achieved from each of the following test cases:
    - a = 2, b = 5
    - a = -3, b = -6
    - Both of the above.
7. Define branch coverage. 
8. '100%  Branch coverage ensures 100% statement coverage' - discuss.
9. Define semantic coverage. What kind of testing methods can be used to achieve semantic coverage?