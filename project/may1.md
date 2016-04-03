_GIRLBOT


# May1 Project : The Question for Bad Smells


## Overview


Now that Project1 is over, we have some data on the patterns of issues
made in projects in this subject.

-  Project1: do something
-   Project2: reflect on what others did, observe "bad smells", suggest
    improvements.


Your task: to write scripts that

-   Find *bad smells* from this data.
-   (Extra marks) to offer an early warning on that bad smell.


For a good example of part2,  see [this example from 2015](https://github.com/CSC510-2015-Axitron/project2)

For a quick intro on how to pull issue reports out of Github, see [here](https://gist.github.com/timm/a87fff1d8f0210372f26)

Privacy Considerations
----------------------

Note the first rule of Project2:

-   Manners matter.

As you "look over the shoulder" of your friends' work, they will be
looking over yours. Hence, our goal is **not** to insult anyone by
calling them out over some programming practice. Rather, we want to
learn how to help them such that, in future projects, if they (or you)
start sinking then (a) someone else will notice and (b) will rush over
to help out. Hence, here's the second rule of Project2:

-   No one gets named (or maimed) in this process.

The **first** thing you will do when you get data is that you will (a)
look for all identifying symbols; then (b) replace them with (e.g.)
group1 or person27. Privately (and not on your repos) you might keep a
list mapping persons and groups to their real name but that is up to
you. And those lists will stay private.

## Your Tasks


### Data Colllection

Using the script
[gitable.py](https://gist.github.com/timm/a87fff1d8f0210372f26) then
grab data on three other projects:

-   To find those projects, look at the [class
    list](https://goo.gl/xVW0tN).
-   Make one of the projects your own... you'll at least know the
    background on what was happenning when those issues were being
    generated. Which could be useful for this analysis.
-   Pick two other projects with LOTS of issues

Note that the data will have to be:

-   Anonymized
-   Filtered into tables (comma seperated files, spreadsheets, whatever)
    -   If you are good with python, you might do that by tweaking
    gitable.py.

  -   If you do something cool with gitable, share it with
            everyone (post it to gists.github.con and post to the
            newsgroup).
    -   Failing that, there is nothing wrong with click-click-clicking

### Small Features Detection

A general pattern in human cognition is that smart folks:

-   Initially apply *feature extractors* to data such that the raw data
    gets turned into a small set of data items, each with tags.
-   Then a second layer combines these features into higher level bad
    smells.

So, what are your feature extractors? e.g.

-   Number of times each label was used?
-   Mean and standard deviation of times spent in each label?
-   "Unusually long" time; i.e. more than the usual values
-   "Unusually small" number of issues handled by person21?
-   "Unusually large" number of commits?

Think hard on this one. Define 10 to 20 feature extractors.

### Some Stats

What does ""unusual" mean?

- Using normal curves:  mean + 1.5 or 2 standard deviations time

![cdf](https://www.ibm.com/developerworks/mydeveloperworks/blogs/RationalBAO/resource/BLOGS_UPLOADED_IMAGES/ScreenShot2012-04-15at10.43.32AM.png)

But assumes the data is normal. If you graph the sorted values you see something like this:

![norm](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Normal_Distribution_CDF.svg/720px-Normal_Distribution_CDF.svg.png)

(Exam question: how is the second graph generated from the first)

There are tests for "normal" but here's the cheat sheet:

- The graph of the sorted values should be:
      - smooth flowing
      - symmetric about the mean
      - should gently flow to either end a smooth plateau

If you are not normal then use upper sorted range:

- sort all the values (keeping repeated ones)
- declare "unusually large" to the the upper 10%

By the way, upper sorted range works for normal and non-normal so...

### Bad Smell Detector

Combining the feature extractors, report on the bad smells.

### Early Detector (Extra Marks)

Anyone can see the forest fire. But can you see the smoke?

Sort all your data chronologically and map out at what times t1,t2,etc
these bad smells occur.

Now, how early before t1,t2, etc can you raise a red flag saying "bad
smell ahead?"

## What to Hand in

In our [submissions sheet](https://goo.gl/xVW0tN),
paste a link to a PDF file in our usual format. We
are expecting 8+ pages, double column with LOTS of
illustrations. 

