Object-oriented Python course
=============================

This repository collects slides, exercises and other supporting
material used in the [Python language courses](http://www.gc3.uzh.ch/edu/python) held by
the [GC3](http://www.gc3.uzh.ch/) at the [University of Zurich](http://www.uzh.ch/).

The material in this course covers the basics of Python programming
and object-orientation.  We assume that students are already familiar
with scripting languages (e.g. bash, perl) and have already written
some computer programs.


How to use the material
-----------------------

The files named `partNN.tex` are used as slide decks during the
lessons.  Exercises are interspersed in the slides; solutions are
provided in the `.py` files.

To create the PDF files for the slides, you need to download the
[GC3 beamer style](http://github.com/gc3-uzh-ch/beamer-theme-gc3).
Place the GC3 beamer style files in the directory there the
`partNN.tex` files are, then type `make all`.


Programme / Timetable
---------------------

We normally deliver the course in two sessions, of one day each:

- The first day of the course introduces Python syntax and the
  fundamental data types.

- The second day of the course covers Object-oriented Python: the
  basic concepts of object-oriented programming (class, instances,
  interfaces and inheritance) are introduced along with Python code
  examples.  Then we delve into object-oriented Python idioms that
  every working Python programmer should know about.


### Day 1: Python basics

* [Introduction](part00.tex)
* [Workstation setup](part01.tex)
   - Downloads: [welcome.py](welcome.py)
* [Basics 1: data types, operators, assignment, functions](part02.tex)
   - Downloads: [hello.py](hello.py)
   - Solutions to exercises: [ex02c.py](ex02c.py)
* [Basics 2: sequences and iteration](part03.tex)
  - Solutions to exercises: [ex03a.py](ex03a.py), [ex03b.py](ex03b.py), [ex03c.py](ex03c.py)
* [Everything is an object!](part04.tex)
* [String manipulation, file I/O](part05.tex)
  - Downloads: [values.dat](values.dat), [euro.csv](euro.csv)
  - Solutions to exercises: [ex05a.py](ex05a.py), [ex05b.py](ex05b.py), [ex05c.py](ex05c.py), [ex05d.py](ex05d.py), [ex05e.py](ex05e.py) (aka `rename.py`)


### Day 2: Object-oriented Python

* [Object-oriented programming: basics](part06.tex)
  - Downloads: [vector.py](vector.py)
  - Solutions to exercises: [ex06a.py](ex06a.py), [ex06b.py](ex06b.py)
* [Special methods](part07.tex)
  - Downloads: [vector2.py](vector2.py), [vector3.py](vector3.py), [vector4.py](vector4.py), [vector5.py](vector5.py)
* [Object-oriented programming: inheritance](part08.tex)
  - Downloads: [complexnum.py](complexnum.py), [vector_and_complexnum.py](vector_and_complexnum.py), [wt.csv](wt.csv)
  - Solutions to exercises: [ex08a.py](ex08a.py), [ex08b.py](ex08b.py), [ex08c.py](ex08c.py), [ex08d.py](ex08d.py), [ex08e.py](ex08e.py), [ex08f.py](ex08f.py)
* [Unit tests and doctests](part09.tex)
  - Downloads: [vector6.py](vector6.py)
* [Exceptions and error handling](part10.tex)
  - Downloads: [test.csv](test.csv)
  - Solutions to exercises: [ex10a.py](ex10a.py), [ex10b.py](ex10b.py)
* [Do not reinvent the wheel: a survey of useful Python libraries](part11.tex)


How to contribute
-----------------

We welcome contributions from other Python instructors, programmers,
students and enthusiasts in general :-).  Please submit a pull request
or send us an email at <mailto:info@gc3.lists.uzh.ch>.


--------

<a rel="license"
   href="http://creativecommons.org/licenses/by-nc-sa/3.0/">
       <img alt="Creative Commons License" style="border-width:0"
           src="http://i.creativecommons.org/l/by-nc-sa/3.0/80x15.png" />
</a>
<p>
The <span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Python Course</span>
by the <a xmlns:cc="http://creativecommons.org/ns#"
   href="http://www.gc3.uzh.ch/" property="cc:attributionName"
   rel="cc:attributionURL">Grid Computing Competence Center,
   University of Zurich</a> is licensed under a <a rel="license"
   href="http://creativecommons.org/licenses/by-nc-sa/3.0/">Creative
   Commons Attribution-NonCommercial-ShareAlike 3.0 Unported
   License</a>.
Permissions beyond the scope of this license may be available at <a xmlns:cc="http://creativecommons.org/ns#" href="mailto:info@gc3.lists.uzh.ch" rel="cc:morePermissions">mailto:info@gc3.lists.uzh.ch</a>.
</p>