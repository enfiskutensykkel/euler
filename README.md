Project Euler Solutions
=======================

These are my solutions to (some of) the problems that are found on 
[Project Euler](http://projecteuler.net/problems).

You will notice that my weapon of choice for a lot of these problems is
Python (2.7). This is because of the simplicity of the language, powerful standard
libraries (e.g. for [regular expressions](http://docs.python.org/2/library/re.html))
and the flexibility when dealing with weakly typed variables, large numbers 
(bigger than what fits in traditional data types), textual processing etc.
Sadly I'm not all too familiar with [numpy](http://www.numpy.org/),
therefore some of my solutions that require speed are in C (C99/GNU).

I've also included a script to copy problem descriptions and place them in the
problem sub-directories. Run `python descs.py` in the root repository directory.
The script will automatically search for sub-directories ( *so name them by problem numbers!* ).
