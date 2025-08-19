# CS 164: Programming Assignment 2

[PA2 Specification]: https://drive.google.com/file/d/1AfItkkJScHLxIMLVBAsHk6uqM9bMx6jE
[ChocoPy Specification]: https://drive.google.com/file/d/1mrgrUFHMdcqhBYzXHG24VcIiSrymR6wt

Note: Users running Windows should replace the colon (`:`) with a semicolon (`;`) in the classpath argument for all command listed below.

## Getting started

Run the following command to build your semantic analysis, and then run all the provided tests:

    mvn clean package

    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy \
        --pass=.s --dir src/test/data/pa2/sample/ --test


In the starter code, only two tests should pass. Your objective is to implement a semantic analysis that passes all the provided tests and meets the assignment specifications.

You can also run the semantic analysis on one input file at at time. In general, running the semantic analysis on a ChocoPy program is a two-step process. First, run the reference parser to get an AST JSON:


    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy \
        --pass=r <chocopy_input_file> --out <ast_json_file> 


Second, run the semantic analysis on the AST JSON to get a typed AST JSON:

    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy \
        -pass=.s  <ast_json_file> --out <typed_ast_json_file>


The `src/tests/data/pa2/sample` directory already contains the AST JSONs for the test programs (with extension `.ast`); therefore, you can skip the first step for the sample test programs.

To observe the output of the reference implementation of the semantic analysis, replace the second step with the following command:


    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy \
        --pass=.r <ast_json_file> --out <typed_ast_json_file>


In either step, you can omit the `--out <output_file>` argument to have the JSON be printed to standard output instead.

You can combine AST generation by the reference parser with your 
semantic analysis as well:

    java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy \
        --pass=rs <chocopy_input_file> --out <typed_ast_json_file>


## Assignment specifications

See the [PA2 specification][] on the course
website for a detailed specification of the assignment.

Refer to the [ChocoPy Specification][] on the CS164 web site
for the specification of the ChocoPy language. 

## Receiving updates to this repository

Add the `upstream` repository remotes (you only need to do this once in your local clone):

    git remote add upstream https://github.com/cs164berkeley/pa2-chocopy-semantic-analysis.git


To sync with updates upstream:

    git pull upstream master

## Submission writeup

Team member 1: Evelyn Vo

Team member 2: Destiny Luong


Questions

    How many passes does your semantic analysis perform over the AST? List the names of these passes with their class names and briefly explain the purpose of each pass.

It takes 2 passes to go over the ASTs. The first pass is called Declaration Analyzer, it is used to store all the global variables, functions, classes, and methods, and create a hierarchy between these structures. It handles all the declarations outside of stmt nodes. The second pass is called Type Checker. This uses the symbol table to identify the inferred types for expressions and analyze the stmt nodes. (The symbol table was extended with VarTable which also tracks hierarchies for the current table.) Both passes look out for errors over the nodes they examine.


    What was the hardest component to implement in this assignment? Why was it challenging?

The hardest component to implement in this assignment was the idea of classes, superclasses, subclassess, and methods. Although these structures are separate they heavily rely on each other. For example, superclass methods and members need to be accessible to subclasses. Thus, we need to keep track of those outside of the superclass’s block, as well as all of the class relationships. As such it was very difficult to map out the relationships and apply them to the concepts of scope and they had in order to have proper behavior. Testing for correctness took a long time, too. We kept changing how we implemented the hierarchy tracking, from using various combinations of ArrayLists, HashMaps, etc. to using trees. Every time we added something, something else broke as well.


    When type checking ill-typed expressions, why is it important to recover by inferring the most specific type? What is the problem if we simply infer the type object for every ill-typed expression? Explain your answer with the help of examples in the student contributed/bad types.py test.

It is important to infer with the most specific type because subclasses will always have more or equal members and functions available to them than the superclasses as they inherit anything the superclass contains. If you default to the least specific type “object” for each ill-typed expression, it may be the case that using the expression (i.e. a member expression’s identifier) would require accessing a member or method that wouldn’t be available to object. In other words, an otherwise legal expression would be flagged as being legal.

For example, in the case of bad_type_id, the most specific type for x would probably be a float or int. However, if x defaults to being an object, you get an illegal expression in which an object is subtracting 1.
