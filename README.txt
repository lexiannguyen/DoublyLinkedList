Welcome to homework 1 for ECS 32B.
Fall 2023
Instructor: Nicholas Weaver
nweaver@icsi.berkeley.edu


In this project you are given two files, pylist.py and pylist_test.py

You need to extend the LinkedList implementation in pylist.py with
some additional features:

1: appending and length need to be constant time operations.

2: Support for various idiomatic python components, so you can do
"linkedlist[index] = something" and "del linkedlist[index]" and have
those work, as well as having repr(linkedlist) and string(linkedlist)
work to aid in your debugging.

The easiest way to find what you need to change is look for the "raise
NotImplementedError" statements, which are included at the beginning
of each function that you need to modify.  You should also extend the
docstring comment on each function you modify to explain what you do
and why.

You do not actually have to write very much code here, and correctness
of your code is 50% of your grade.


You need to also add test cases in pylist_test.py to test your code.

33% of your grade is the effectiveness of these test cases.  Not only
will they be run for your code but they will be run against a staff
solution.  The staff solution has a series of "flags", corner cases in
the code that we expect your tests to trigger/cover.  You should
include docstrings in all these testcases to make it clear what they
are doing.

The final 17% will be "style": You must comment your code clearly,
primarily in docstrings to describe what each function or test
actually does.

This project is to be done individually.



Grading:

Grading will be autograded using Gradescope.  The autograder is not
yet released but it will operate as follows.  You can effectively
submit as many times as you want, although there may need to be a rate
limit imposed if this is overused.  The autograder will also ignore
anything you print out to "standard error", that is, using the syntax
"print(SOMETHING, file=sys.stderr)"



The autograding will consist of three pieces.

The first is a series of "sanity tests" that ensure that your code,
both pylist.py and pylist_test.py, works with our autograding
infrasturcture.  This will be reported each time your code is
submitted.

The second is the grading for your code in pylist.py.  This grading
will be applied to your final submission: you will not be able to see
the intermediate executions nor your grade until after the due date.

The final is the grading for your code in pylist_test.py.  This
grading will be run each time your code is submitted, and it will
report your final grade, but will not report what flags you found and
which ones you did not.

It will report which of your testcases reported our code as failing.
Our code should not fail any testcases, which suggests a problem in
your testcase.  If you believe that your testcase has found a problem
in our code, please show up to the instuctor's office hours.



The reason for this structure is because although testing is only 33%
of the grade, it is the forcing function to make sure your code works.
If you have a set of testcases where our code passes 100% and where
you find all our flags, you probably have a test that can ensure that
your code is also 100% correct!

Much of the purpose of this class is to make you a better programmer.
Good programmers write good, well documented test cases as they go
because it, in the end, serves as a timesaver.  It is far easier to
catch your bug in a testcase than it is to go "ok, I coded up this
entire thing, why isn't it working"
