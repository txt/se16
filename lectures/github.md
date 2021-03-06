<img width=400
align=right src="https://tommcfarlin.com/wp-content/uploads/2013/02/drunktocat.jpg">

# Github tips and tricks

[TOC]

_____

From Wikipedia:

+ Git is a widely-used version control system for
  software development.
+ It is a distributed revision control system with
  an emphasis on speed, data integrity, and support
  for distributed, non-linear workflows.
+ Git was initially designed and developed in 2005
by Linux kernel developers (including Linus
Torvalds) for Linux kernel development.  As with
most other distributed version control systems, and
unlike most client–server systems, every Git working
directory is a full-fledged repository with complete
history and full version-tracking capabilities,
independent of network access or a central server.
+ GitHub is a Web-based Git repository hosting service.
+ Github offers all of the distributed revision control and source code management (SCM) functionality of Git as well as adding its own features.
+ Unlike Git, which is strictly a command-line tool, GitHub provides a Web-based graphical interface and desktop as well as mobile integration.
+ It also provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.



# World's best guides to Github

Read these, now:

1. [just a simple guide for getting started with git.
  no deep sh*t)](http://rogerdudler.github.io/git-guide/)" by
  Roger Dudler.
     - 10 mins to read
2. Work this
[tutorial on branching](http://pcottle.github.io/learnGitBranching/).
    - Can do first 4 levels in about 20 minutes.
    - Whole thing might take 2-4 hours.


Have you looked at those guides?

Then you may continue.


# Github as a Productivity Tools

There are two "yous"

+ One creative brilliant inspired soul with great ideas
     + Another dullard that just wants more coffee and do some
       drudge work before heading home for the day
+ The inspired one only shows up now and again:
     + And assembles the materials needed for the dullard
+ The dullard just works on what is in front of them

Your mission: make the dullard most productive.

Can software help the
dullard?  Slack, Trello, Assembla, Jira etc all all fine tools.
And for more, [see here](https://www.g2crowd.com/categories/project-management#span-class-service-mark-grid-span-for-project-management).
But I live by Github issues:

+ Give us this day my daily issues.

<center><a href="/_img/timmIssues.png"><img width=400
src="/_img/timmIssues.png"></a>
</center>

Use issues to capture ideas and tasks as they occur to you.

+ Kids ask you  to bake  a carrot cake
+ See a poster for a circus you want to see? Buytickets is an issue.

The barrier for adding something to your in list
should be as low as possible.


# Using issues

Issues are ways that team members communicate with each other,
and with themselves.

1. General github issue tutorial: [tutorial](https://guides.github.com/features/issues/)
2. [A simple styleguide for tagging Github issues](https://robinpowered.com/blog/best-practice-system-for-organizing-and-tagging-github-issues/).


![](/_img/githubIssues.png)

# Using Milestones

Issues can be aggregated into Milestones... when things are actually
due (and the number of closed issues in the Milestone is a report
of "percent done").

Project bad smell: all issues, no milestones.



# Commit tricks:

+ Pull frequently
+ Commit early and often
    + "The dog ate my homework" don't cut it no more.
    + Now you, and your team mates, and github.com all
	keep copies of your work.
+ Comment your commits as you would have others comment theirs

# Gists

Use gists to share snippets and pastes (a place to share
code hints and tips):

+ GitHub "gists" -- shared code snippets -- are not a
Git feature, but they use Git.
+ All gists are Git
repositories, andGitHub Gist makes it easy to share
them.
+ You can search Gist for public gists by topic,
programming language, forked status, and starred
status.
+ You can also create secret gists and share
them by URL.


<center><a href="https://gist.github.com/timm"><img width=400
src="/_img/giststimm.png"></a></center>


# Branching tricks

Good advice from [teaching a Designer to Use GitHub](http://www.slideshare.net/liamdempsey/teaching-a-designer-to-use-github):

Small teams (K.I.S.S.):


![](/_img/githubbranches1.png)

Bigger teams:

+ Don't bother big team with all the micro changes
+ Every branch is a promise that something interesting will come
  back.

![](/_img/githubbranches2.png)

# .gitignore

Do not pollute your team mate's repo with your temporaries.

E.g. Mac users:

```
.DS_Store
```

e.g. Latex users:

```
## Core latex/pdflatex auxiliary files:
*.aux
*.lof
*.log
*.lot
*.fls
*.out
*.toc
```

e.g. Python users:

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*,cover
.hypothesis/

# Translations
*.mo
*.pot

# Django stuff:
*.log

# Sphinx documentation
docs/_build/

# PyBuilder
target/
```

For other suggested configurations for gitignore
[see here](https://github.com/github/gitignore).

# Shell tricks

## Simple tricks

Mac and Linux users:

- add these short cuts to your _$HOME/.bashrc_ file

```bash
# Git related
alias gs='git status'
alias gc='git commit'
alias ga='git add'
alias gd='git diff'
alias gb='git branch'
alias gl='git log'
alias gsb='git show-branch'
alias gco='git checkout'
alias gg='git grep'
alias gk='gitk --all'
alias gr='git rebase'
alias gri='git rebase --interactive'
alias gcp='git cherr
```

## Make tricks

I have a `Makefile` in the root of all my repos. This file
has _rules_ whose _actions_ are useful Git tricks.

(Note the  use of `@-`  in this file; they are optional
but, for the record, they suppresess output
and ignores any error conditions.)

```make
url=se16.unbox.org

publish : typo

typo: ready
	@- git status
	@- git commit -am "saving"
	@- git push origin master
	@- wget -O -  http://$(url)/update.cgi

commit: ready
	@- git status
	@- git commit -a
	@- git push origin master
	@- wget -O - http://$(url)/update.cgi

update: ready
	@- git pull origin master

status: ready
	@- git status

ready: readmes
	@git config --global user.name "Tim Menzies"
	@git config --global user.email "tim.menzies@gmail.com"
	@git config --global credential.helper cache
	@git config credential.helper 'cache --timeout=3600'

readmes: project/README.html

project/README.html : project/_etc/README.md
	./render.cgi project/_etc/README nohead > $@
	git add $@
```

### Example Usages

`make ready` is nice: caches my password for an hour so I don't
have to type in my password all the time. Lets me commit often!

`make commit` batches up all the usual commands.

`make typo` is a bad cheat: quick commit without comments (bad man! bad man!).

Note that my `typo` and `commit`s end with a call to an `update.cgi`
file on this subject's website. So as a side-effect of committing,
the site updates.


### The Mock Trick

Also, my `$HOME/.bashrc` has the following script:

```bash
mock() {
    root=$(git rev-parse --show-toplevel)
    if [ -d "$root" ]; then
       	(cd $root;
	 if [ ! -f Makefile ]; then
	     makefile0 > Makefile
	     git add Makefile
	 fi
       	 make $* ;)
    else
	echo "mock: nothing to do"
    fi
	}
```

This lets me access the `Makefile` in any sub-directory of
my checked out repos.

- It finds the root of the current repo using `git rev-parse --show-toplevel`
- It (temporarily) changes to that directory
- It changes to that directory.
- It called `make` using what ever arguments were given to `mock`.

So my repos have one, and only one, `Makefile` in their root.
