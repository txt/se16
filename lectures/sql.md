# SQL

Different languages are best for different tasks:

+ If raw speed, then ""`C`"";
+ If mass scale micro-currency, then `Erlang` or `Elixr`;
+ If publish-subscribe, then `Elm`; 
+ If portability, then:
    + `Java` or any other language that compiles down to the Java Virtual machine
       (e.g. `Clojure`, `Scala` or  [dozens of other languages](https://en.wikipedia.org/wiki/List_of_JVM_languages));
    + `JavaScript`  or any other language that compiles down to the JavaScript engine
	  (e.g. `CoffeeScript`, `Elm`)
+ If cross-platform GUI then many choices including `Python`, `Java`
+ Etc, etc

SQL is a language designed for _maintainability_:

1. SQL supports _layered architectures_ that
   separate data and model, thus allowing developers
   to reorganize the data storage layer without
   messing up the business logic.
2. SQL simplifies scripts by removing nested access
   paths.
3. SQL removes a set of standard anomalies with long term storage (_insert, delete, update_ 
  anomalies)
 
For notes  on the above 3 points, see below. But first, some details.

An SQL server consists of a relational database
which comprises of a set of tables containing data
with predefined categories or columns. It contains
structured data like names, email addresses, and
phone numbers. A relational database matches data by
using common characteristics found in the dataset
and the resulting group is termed as _Schema_ such
as the one shown below:


```
CREATE TABLE Supplier (
  SID     int          primary key,
  SName   varchar(10)  NOT NULL,
  Status  int          NOT NULL,
  City    varchar(10)  NOT NULL
)

CREATE TABLE Part (
  PID     int          primary key,
  PName   varchar(10)  NOT NULL,
  Color   int          NOT NULL,
  Weight  real         NOT NULL,
  City    varchar(10)  NOT NULL
)

CREATE TABLE Shipment (
  SID     int          NOT NULL FOREIGN KEY REFERENCES Supplier(SID),
  PID     int          NOT NULL FOREIGN KEY REFERENCES Part(PID),
  Qty     int          NOT NULL,
  PRIMARY KEY (SID, PID)
  )
```

In SQL _tables_ have columns and  rows and rows have cells and cells are _atomic_;
i.e. they are _one_ thing (strings, numbers, booleans, and no nested structure). That is:

+ Tables cannot contain tables recursively;
+ All tables live at the top-level in the global name space of a database.


## SQL and Layered Architectures

SQL supports a _layered_ architecture
where all the concerns about data storage, indexing, backing up, etc are handle in a
_database layer_ which applications talk too via a higher level _structured query language_ called SQL. For example, in Python:

```
import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

staff_data = [ ("William", "Shakespeare", "m", "1961-10-25"),
               ("Frank", "Schiller", "m", "1955-08-17"),
               ("Jane", "Wall", "f", "1989-03-14") ]
               
for p in staff_data:
    format_str = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
    VALUES (NULL, "{first}", "{last}", "{gender}", "{birthdate}");"""

    sql_command = format_str.format(first=p[0], last=p[1], gender=p[2], birthdate = p[3])
    cursor.execute(sql_command)
```

## SQL and Simpler Application Programming

The ability to globally reference all parts of the data structure simplifies
maintenance:

+ Nothing is inside anything else. E.g. `Parts` are not buried away inside `Suppliers`;
+ Data can be navigated in any direction; e.g. Q1: from `Suppliers` we can find all
the `Parts` they offer just as easily as Q2: finding what `Suppliers` sell what `Parts`.

Note the above is much more complicated for data storage designs that assume nested
data structures. For that nested-data approach
(the programmer needs to know the nested structure of the data to
find the data. If anyone every changes that nested structure then
_all scripts that assume that nesting must be rewritten_).

## SQL and "Data Anomalies"

It turns out that teasing everything into top-level tables avoids
many common problems in long-term data storage.  Consider the following
design where every data point is stuffed into one matrix. In the following:

+ `ST` is some number that refers to the shipping status (e.g 20 means _order shipped_ and 30 means _received_)
+ `PNO` are parts
+ `QTY` is quantity
+ `SNO` is some shipping number (shipping ID)

```
 --------------------------------
 | SNO │ ST │ PNO │ QTY │ CLR   |
 --------------------------------
 │ S1  │ 20 │ P1  │ 300 │ red   |
 │ S1  │ 20 │ P2  │ 200 │ blue  |
 │ S1  │ 20 │ P2  │ 400 │ blue  |
 │ S1  │ 20 │ P4  │ 200 │ gray  |
 │ S1  │ 20 │ P5  │ 100 │ black |
 │ S1  │ 20 │ P6  │ 100 │ white |
 │ S2  │ 30 │ P1  │ 300 │ red   |
 │ S2  │ 30 │ P2  │ 400 │ blue  |
 │ S3  │ 30 │ P2  │ 200 │ blue  |
 │ S4  │ 20 │ P2  │ 200 │ gray  |
 │ S4  │ 20 │ P4  │ 300 │ gray  |
 │ S4  │ 20 │ P5  │ 400 │ black |
 --------------------------------
```

Suppose the above table is _all_ we know about the data. Such a database would
 suffer from _insert_, _delete_ and _update_ anomalies.
 
**Insert Anomalies:**

 
+ _Problem_: If our warehouse receives 1000 new parts, which no one has ordered yet,
   then it cannot be added to our matrix database (without some bogus null fields-- which 
   significantly complicate long term maintenance).
+ _Diagnosis_: the above one-matrix design has too many data dependencies between cells 
           in each row. 
+ _Treatment_: Separate the cells into different tables such that each cell is now dependent
  on only one special cells in the table (the primary key). 
+ _Example_:  In the above 3 table design, it would be possible to insert new `Part`s
           without demanding that they exist in an order.

**Delete anomalies:**

+ _Problem_:  If we complete all our shipments for `S1` and `S4` (above), and we delete those rows  from our one-matrix, we would lose
access to the fact that we ship those a part called `P5`. This would be a problem if
anyone calls us up to ask if we can supply them with `P5`.
+ _Diagnosis_: As before, we have not separated out or dependent and non-dependent variables.
 The fact that we hold `P5` is a separate concept to whether or not `P5` is in any shipment.
+ _Treatment_: As before. Separate the cells into   tables defined by primary keys.
+ _Example_: In the above 3 table design, it would be possible to complete all shipments,
archive away rows in the `Shipment` to some long-term storage facility, and still have
access to what  `Part`s we hold in the warehouse.

**Update anomalies:**

+ _Problem_: There is a bug in the above one-matrix example. Can you see? Look at the colors
  for the `P2` part? Note that they are usually `blue` but in `S4` it is labeled `gray`.
  Someone has made a mistake?
+ _Diagnosis_:  When the definition of things is repeated in multiple places, then it is
  all to easy to update properties _here_ and forget to do it _there_, _there_, and _there_
  as well.
+ _Treatment_: As before, if everything is separated logically, then information about one
  thing is stored in one place only. Which means we could update color in one place and
  that color is now global across the hole database.
+ _Example_: In the above 3 table design, it would be possible to add a `color` filed
to `Part` holding the unique color of that part. Updates to that color would then
refer to all those `Part`s.

## Drawbacks of SQL

Despite the theoretical advantages of SQL, shown above, experience has shown that it
has drawbacks. Advocated of NoSQL databases eschew the schema approach and store
everything in nested dictionaries that look like this:

```
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
```

Hardware and software tools have evolved
to handle very large NoSQL databases. While experiences differ, the following are some
comments on the current state of the art in SQL vs NoSQL:

+ Speed:
    + SQL administrators   relied on scaling up or buying bigger, expensive, multiple servers as database load increased rather than scaling out or distributing the database across multiple hosts.  
    + NoSQL databases are designed to expand transparently and horizontally to take advantage of new nodes, and they’re usually designed with low-cost commodity hardware in mind.  
+ Quantity:
    + There are limits to the  data volumes that can be handled by a single SQL server.
     + Tools like Hadoop, which  enable of certain types of NoSQL distributed databases, allow data to be spread across thousands of servers with little reduction in performance .
+ Personnel cost:
     + Maintaining high-end SQL  systems is expensive and can be only done with the assistance of expensive, highly trained DBAs (database administrators). 
     + On the other hand, NoSQL databases require less management. Features like automatic repair, easier data distribution, and simpler data models make administration and tuning requirements lesser in NoSQL.
+ Server Cost
     + SQL databases  tends to rely on expensive proprietary servers and storage systems. 
     + NoSQL databases typically use clusters of cheap commodity servers to manage the exploding data and transaction volumes. Hence,
 storing and processing data cost per gigabyte in case of NoSQL can be many times lesser than the cost of SQL-based solutions.
+ Flexibility:
    + Data can be inserted in a NoSQL database without first defining a rigid database schema. 
    + On the contrary, change management is a big headache in SQL. Here, even minor changes to the data model have to be carefully managed and may necessitate down time or reduced service levels.

### Which to use? 

I dunno. Depends. Maybe we should say....

+ If optimizing to reduce long term maintenance cost of long   highly structured somewhat static data, then SQL
+ If optimizing to increase flexibility and scalability, then NoSQL


 
	  
	
