# CS 164: Programming Assignment 1

[PA1 Specification]: https://drive.google.com/open?id=1oYcJ5iv7Wt8oZNS1bEfswAklbMxDtwqB
[ChocoPy Specification]: https://drive.google.com/file/d/1mrgrUFHMdcqhBYzXHG24VcIiSrymR6wt

Note: Users running Windows should replace the colon (`:`) with a semicolon (`;`) in the classpath argument for all command listed below.

## Getting started

Run the following command to generate and compile your parser, and then run all the provided tests:

    mvn clean package

    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy --pass=s --test --dir src/test/data/pa1/sample/

In the starter code, only one test should pass. Your objective is to build a parser that passes all the provided tests and meets the assignment specifications.

To manually observe the output of your parser when run on a given input ChocoPy program, run the following command (replace the last argument to change the input file):

    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy --pass=s src/test/data/pa1/sample/expr_plus.py

You can check the output produced by the staff-provided reference implementation on the same input file, as follows:

    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy --pass=r src/test/data/pa1/sample/expr_plus.py

Try this with another input file as well, such as `src/test/data/pa1/sample/coverage.py`, to see what happens when the results disagree.

## Assignment specifications

See the [PA1 specification](https://drive.google.com/file/d/1kWncRoAomYg20UHWSaFfZ4n14JsOkOOK/view) on the course
website for a detailed specification of the assignment.

Refer to the [ChocoPy Specification][] on the CS164 web site
for the specification of the ChocoPy language. 

## Receiving updates to this repository

Add the `upstream` repository remotes (you only need to do this once in your local clone):

    git remote add upstream https://github.com/cs164berkeley/pa1-chocopy-parser.git

To sync with updates upstream:

    git pull upstream master


## Submission writeup

(1) Team Members: Destiny and Evelyn
(2) We went to office hours with Billy and also looked through a Stack Overflow for small java errors.
(3) 43 Hours

1. What strategy did you use to emit INDENT and DEDENT tokens correctly? Mention the filename
and the line number(s) for the core part of your solution.

In order to implement INDENT and DEDENT, we first edited our jflex to be able to switch between 2 different states, that being "yyinital" which reads from our lines and sends out tokens, and also "indenting" in order to deal with the logic of the indents. For vars, we kept a stack, which lets us know the level of indent we are on, and how many indents there are. We also keep track of the number of indents within a line, and also a var that checks the number of spaces that have been used. As we are parsing through the program, if we reach a Newline, we check if the stack size is greater than 1, if so that means we are within an indented paragraph, where we would remove an indent level from the stack and then Dedent. If not, then we are not within an indented paragraph, and can just output a NEWLINE token. 

If we reach an Indent while parsing we would then check if the size of the stack is equal to 0. If so, we push a 0 onto the stack to show this is our current indent level. If not, we would then first process the indent by checking the number of spaces or tabs, checking if they're valid inputs. We then go into the "endIndentorDedent" func, where we compare the current nummber of indents for the current line and the number of indents from the last line on the stack. If they are the same, then we check if there are 0 spaces, in which we output and INDENT token, else if the total number of spaces is positive but lower than 8 we add the current indent level to the stack (prev indent level + 1), and return both an INDENT token and the current stack index. If the amount of current indents is greater than the amount in the previous indents from our stack, we check if there the difference between them is 1 and there are no spaces, add that level to the stack and then return an INDENT token and the index of the stack we are currently on. Else we return an UNRECOGNIZED token. 

Lastly if the current number of indents is smaller than the last one on the stack by 1 and there are no spaces, we remove an indent level from the stack and return a DEDENT symbol. Then, we reset the total number of indents and spaces for this line back to 0. Finally, if we reach and EOF line we check if the stack still has indents, in which we will then set the zzAtEOF flag to false to ensure that matching will still continue even after reaching EOF. We then remove the remaining indents from the stack and send a DEDENT token for each stack level. After the indent stack is empty, we set the zzAtEOF flag to True and then return the EOF symbol. 

Core part of solution:
- File: ChocoPy.jflex
- Lines 52-121, 163-180, 242-250

2. What was the hardest language feature (not including indentation) to implement in this assign-
ment? Why was it challenging? Mention the filename and line number(s) for the core part of your solution.

The second hardest language feature was functions. This was difficult to implement mainly because it used INDENT and DEDENT the most but also because it had a lot of different parts. The grammar in the ChocoPy.cup file (Lines 548 to 560) was especially hard to implement because not only was there parameters and arguments with different class types to think about, but also many blocks within the function body that would repeat or recursively use eachother. We had to deal with a bunch of Shift/Reduce or Reduce/Reduce conflicts. We solved this by really trying to map out the functions and it's parts, changing the precedence values, and keeping in mind which part of the grammar would interact with which other part, and also really tried to understand the classes we were using and what they information was required. The Chocopy spec and the Cup file were really helpful when it came to this section. 

Core part of solution:
- File: ChocoPy.cup
- Lines 434-446
