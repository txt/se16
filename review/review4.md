# Review4: Week of Feb 4

## Functional Programming
1. What is currying in functional programming? Give an example and explain.

## SQL and NoSQL
1. What particular purpose SQL is optimized for? Give three ways that SQL has this optimization.
1. State three differences between SQL and nosql.
2. What is database normalization? How SQL implements normalization? Give an example.
3. What are the advantages of normalization?
4. What are the disadvantages of normalization?
5. Explain how SQL maintains layered architechture.
6. Consider the following design where every data point is stuffed into one matrix. In the following, `ST` is some number that refers to the shipping status (e.g 20 means _order shipped_ and 30 means _received_), `PNO` are parts, `QTY` is quantity, and `SNO` is some shipping number (shipping ID).
     
     | SNO | ST | PNO | QTY | CLR   |
     |-----|----|-----|-----|-------|
     | S1  | 20 | P1  | 300 | red   |
     | S1  | 20 | P2  | 200 | blue  |
     | S1  | 20 | P2  | 400 | blue  |
     | S1  | 20 | P4  | 200 | gray  |
     | S1  | 20 | P5  | 100 | black |
     | S1  | 20 | P6  | 100 | white |
     | S2  | 30 | P1  | 300 | red   |
     | S2  | 30 | P2  | 400 | blue  |
     | S3  | 30 | P2  | 200 | blue  |
     | S4  | 20 | P2  | 200 | gray  |
     | S4  | 20 | P4  | 300 | gray  |
     | S4  | 20 | P5  | 400 | black |
    1. What is insert anomaly? Show how the above design suffers from it. How can SQL solve it.
    2. What is delete anomaly? Show how the above design suffers from it. How can SQL solve it.
    3. What is update anomaly? Show how the above design suffers from it. How can SQL solve it.
    
6. List and explain three drawbacks of SQL. How does nosql solves these drawbacks.
7. What is nosql optimized for?
9. What kind of applications should use nosql. Give an example and explain.
10. What kind of applications should not use nosql? Give an example and explain.

