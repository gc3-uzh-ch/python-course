Object-oriented Python training, Sept. 28, 2012
===============================================

This 1-day course assumes generic familiarity with programming and
basic computer programming concepts like variables, functions,
programs. Python syntax will be recapped and then we proceed on to
object-orientation.

[[!toc startlevel=2]]

Introduction (10')
------------------

[[slides (PDF)|part0.pdf]]

- Where to find the material used in the course
- Prerequisites: What's everyone's programming background? Experiences in other programming languages?
- Typographical convention of the slides
- Python 2 vs Python 3


Workstation setup (20')
-----------------------

[[slides (PDF)|part1.pdf]]

Ensure everyone has a working:
  - Python interpreter (at least version 2.6)
  - Text editor
  - Terminal for running the Python REPL

> _RM:_ We should have a recommendation ready for those who have never
> programmed Python before. Use `gedit`? (Default in GNOME/Ubuntu)

In particular:

- Everyone can has a running REPL in front of them
  - Everyone can download the sample [[welcome.py]] and execute it:
  
        >>> import welcome
        Welcome to Python!


The basics (30')
----------------

[[slides (PDF)|part2.pdf]]

- manipulating basic objects via the REPL (2x)
  - basic data types
  - string literals (2x)
- operators (2x)
- function calls
  - type conversion as an example of function calls
  - more examples: `abs`, `sum`
  - use of the `help()` function
    - _Hands-on:_ `help(sum)`, `help('+')`.
- defining own functions
  - the "hello(name)" example
  - indentation as code block delimiter
  - _Hands-on:_ Type the example and run it.
- modules
- statement vs functions
- assignment (3x)
  - if there are any C/Java programmers: assignment is a statement!
- `if`/`else`
- `while`
- _Exercise:_ modify the `hello` function to print a `"Welcome back, " + name` iff `name == (own name)`


Sequences and iteration (20')
-----------------------------
  
- `for ... in range(...)`
- sequences (8x)
- the `in` operator
- `for ... in (sequence)`
- deconstructing bind in `for`
  - _Exercise:_ Implement the `zip(A,B)` function
  
    > _RM:_ Too difficult?
    
  - _Exercise:_ Invert a mapping (swap values and keys).


1st break (15')
---------------

Coffee, etc.


String manipulation, file I/O (45')
-----------------------------------
- file operations:
  - opening a file
  - reading a file:
    - iterating over lines
    - the `readlines()` method
    - the `read()` method
  - _Exercise:_ write a `count_lines()` function that counts the lines in a file
- string methods: `split`, `startswith`, `endswith`, `capitalize`/`lower`/`upper`, `replace`
  - _Exercise:_ load the a simple data file into a list
  - _Exercise:_ load the [[euro.csv]] file into a mapping: currency names are the keys, conversion rates are the values.
  - _Exercise:_ Build a `rate[][]` 2D array that stores the convertion rate of two currencies given the name, e.g., `rate['ITL']['DEM']` gives the conversion rate of Italian Liras to Deutsche Marks.
- more filesystem operations (2x)
  - _Take-home exercise:_ write a `rename.py EXT1 EXT2 DIR` command that renames all files in DIR that end in EXT1 to an EXT2 ending.


Everything is an object! (60')
------------------------------

Detour: what are objects? / Motivation for OOP

- the CS/IT motivation: code reuse:
  - monolithic programs: bunch of functions and global variables, can only re-use code by copy+edit it
  - modular programs: module level visibility of variables and functions, but modules are singletons!
  - OO: an object is variables + functions; can have _multiple_ objects of the same kind in the same program
- the "biology" analogy:
  - species ⇒ `class`
    - e.g., _Felis catus_ ⇒ `class Cat`
  - individual ⇒ instance (syn. with object)
    - e.g., _my cat Romeo_ ⇒ `a_cat = Cat()`
  - inheritance: compare _Felis catus_ with _Felis mangul_: both can `meow` (common to all `Felis` species) but only Felis catus will `purr`.
- the "mathematics" analogy:
  - structure definition ⇒ `class`
    - e.g., _Vector space_ ⇒ `class Vector` (defines the operations/functions that can be applied to vectors)
  - elements in a structure ⇒ instances 
    - e.g., _vector (1,2,3)_ ⇒ `a_vector = Vector(1,2,3)`
  - inheritance: Vector spaces and rings both define a commutative sum, but only vector spaces define scalar multiplication.

> _RM:_ Is the above really needed? I guess most of it will sound incomprehensible for people that have no previous OOP experience!

- The Python way: an object is just a collection of named attributes
  - example: the `dir()` function
    - everything is an object!
  - instance variables _vs_ instance methods

- Defining a Python class:
  - _Example:_ Define a `Features` class that computes the average, minimum and maximum of a sequence of numbers.
    - the constructor initializes an empty sequence and sets `instance.min` and `instance.max` to `None`
      - topics to explain: `self`, constructor
    - there's a `send` method that takes a single number and updates `.max` and `.min`
      - topics to explain access to instance variables


Lunch break (45')
-----------------

Choices: ETH mensa, Polysnack (it's just in front of the room), nearby place that makes good Thai currys.


More OOP: inheritance (45')
---------------------------

- _Exercise:_ define a `Grep` class:
  - construct with a file name and match string, e.g., `matches = Grep(filename, pattern)`
  - implements the iterator protocol (explain it!)
  - each call to `next()` returns the next line in file that matches regex `pattern`
  
- _Exercise:_ define a `GrepOnlyMatching`, that returns only the part of the line that matches `pattern`.
  - use method `.group(0)` of the regexp object

- _Exercise:_ define a `GrepExactly` iterator, that returns the lines that contain a substring (not a regex)

- Inheritance: 
  - show how to do the `GrepOnlyMatching` and `GrepExactly` exercises with inheritance.
  - introduce the "template method" pattern in the discussion
  - mention multiple-inheritance

> _RM:_ Alternative introduction to Template method:
>
> - explain the "template method" pattern
> - example using MatPlotLib: 
>   - use generic class to plot 2D data, 
>   - specialize `plot()` method to change drawing type.
>   - _I'm not confident enough with MatPlotLib to do this!_


Exceptions and error handling (20')
-----------------------------------

- Exceptions: an important example of inheritance
- `try`/`except`/`finally`
  - how to ignore errors
  - how to deal with them
- `with`


Class attributes (20')
----------------------

- classes are objecs too!
- class _vs_ instance attributes
- the `AutoInc` class example
- pointer to a real example: cache/memoize


List comprehensions and generators (30')
----------------------------------------
- _Exercise:_ list dotfiles in a directory
- `for`-loop solution
- list comprehensions
- generator expressions
- generator functions
- _Exercise:_ write a `WordIterator` generator function, that `yields` a file word by word


Advanced topics
---------------

These do not fall in the scope of the course, but it's probably good
to provide pointers:

- "magic" methods
- decorators
- metaclasses

> _RM:_ anything else?


Feedback form
-------------

<iframe src="https://docs.google.com/spreadsheet/embeddedform?formkey=dFByQVZpMms5eTVhT0MteEZadlZacEE6MQ" width="640" height="2239" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
