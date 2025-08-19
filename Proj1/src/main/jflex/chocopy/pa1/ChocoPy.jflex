package chocopy.pa1;
import java_cup.runtime.*;
import java.util.ArrayList; 
import java.util.List;
%%

/*** Do not change the flags below unless you know what you are doing. ***/

%unicode
%line
%column

%class ChocoPyLexer
%public

%cupsym ChocoPyTokens
%cup
%cupdebug

%eofclose false

/*** Do not change the flags above unless you know what you are doing. ***/

/* The following code section is copied verbatim to the
 * generated lexer class. */
%{
    /* The code below includes some convenience methods to create tokens
     * of a given type and optionally a value that the CUP parser can
     * understand. Specifically, a lot of the logic below deals with
     * embedded information about where in the source code a given token
     * was recognized, so that the parser can report errors accurately.
     * (It need not be modified for this project.) */

    /** Producer of token-related values for the parser. */
    final ComplexSymbolFactory symbolFactory = new ComplexSymbolFactory();

    /** Return a terminal symbol of syntactic category TYPE and no
     *  semantic value at the current source location. */
    private Symbol symbol(int type) {
        return symbol(type, yytext());
    }

    /** Return a terminal symbol of syntactic category TYPE and semantic
     *  value VALUE at the current source location. */
    private Symbol symbol(int type, Object value) {
        return symbolFactory.newSymbol(ChocoPyTokens.terminalNames[type], type,
            new ComplexSymbolFactory.Location(yyline + 1, yycolumn + 1),
            new ComplexSymbolFactory.Location(yyline + 1,yycolumn + yylength()),
            value);
    }

    /** Used for tokenizing entries in a list, tuples, etc. and indents. */
    int totalIndents = 0;
    int totalSpaces = 0;
    boolean isIndented = false;
    boolean indentIsProcessed = false;
    boolean firstNewLinePassed = false;
    boolean dedentPassed = true;
    List<Integer> indentLevelStack = new ArrayList<>();
    private void processIndent(String s) {
      for (int i = 0; i < s.length(); i += 1) {
        if (s.charAt(i) == ' ') {
          totalSpaces += 1;
        }
        else if (s.charAt(i) == '\t') {
          totalIndents += 1;
        }
        else {
          System.out.println("Invalid character in processIndent");
        }
      }
      indentIsProcessed = true;
    }
    
    private void resetAfterIndent() {
      totalIndents = 0;
      totalSpaces = 0;
      isIndented = false;
      indentIsProcessed = false;
      firstNewLinePassed = false;
      dedentPassed = false;
    }

    private Symbol endIndentOrDedent() {
      int previousIndentLevel = indentLevelStack.get(indentLevelStack.size() - 1);
      int remainingCurrentIndents = totalIndents - previousIndentLevel;
      boolean oneIndent = totalSpaces <= 8 && totalSpaces > 0;
      boolean noSpaces = totalSpaces == 0;
      boolean moreThanOneIndent = !oneIndent && !noSpaces;
      if (remainingCurrentIndents == 0) {
        if (noSpaces) {
          return symbol(ChocoPyTokens.INDENT, previousIndentLevel);
        }
        else if (oneIndent) { 
          indentLevelStack.add(previousIndentLevel + 1);
          return symbol(ChocoPyTokens.INDENT, previousIndentLevel + 1);
        } 
      }
      else if (remainingCurrentIndents > 0) {
        if (remainingCurrentIndents == 1 && noSpaces) {
          indentLevelStack.add(previousIndentLevel + 1);
          return symbol(ChocoPyTokens.INDENT, previousIndentLevel + 1);
        } 
        else {
          System.out.println("unrecognized");
          return symbol(ChocoPyTokens.UNRECOGNIZED, yytext()); // 2+ indents ahead
        }
      }
      else { // remainingCurrentIndents < 0
        if (remainingCurrentIndents == -1 && noSpaces) {
          indentLevelStack.remove(indentLevelStack.size() - 1);
          return symbol(ChocoPyTokens.DEDENT, previousIndentLevel - 1);
        } 
        else {
          System.out.println("unrecognized 3");
          return symbol(ChocoPyTokens.UNRECOGNIZED, yytext()); // 2+ dedents ahead
        }
      }
      System.out.println("somehow neither indent nor dedent nor malformed symbol");
      return symbol(ChocoPyTokens.UNRECOGNIZED, yytext());
    }
%}

/* Macros (regexes used in rules below) */

WhiteSpace = [ ]
Tab = \t
LineBreak  = [\r|\n|\r\n]+
Indent =  {LineBreak}({Tab}|{WhiteSpace})+ 
IntegerLiteral = 0 | [1-9][0-9]*
AlphabetLiterals = [A-Za-z]

BooleanLiterals = "False" | "True"

NoneLiteral = "None"

Comments = #[^]{LineBreak}
StringLiteral = \"{StringPhrase}\"
            | \'{StringPhrase}\'

StringPhrase = ({AlphabetLiterals}+ | {IntegerLiteral}+ | {WhiteSpace}+ | {ValidEscapes}+ | {ValidSymbols}+)+
ValidEscapes = \" | \n | \t | \\
ValidSymbols =  \! | # | %| & | ' | \( | \)| \* | \+ | , | - | . | \/ | : 
                  | ; | < |= | > | \? | @ | "\[" | "\]" | \\ | _ | ` | \{ | \} | \~


LBracket = "\["
RBracket = "\]"
LParentheses = "\("
RParentheses = "\)"
Comma = ","

Identifier = ({AlphabetLiterals} | _)+({AlphabetLiterals} | _ | {IntegerLiteral})*

%state AfterIndent

%%


<YYINITIAL> {

  /* Delimiters. */
  {LineBreak}                 { 
                                if (indentLevelStack.size() > 1) {
                                  dedentPassed = true;
                                  int dedentLevel = indentLevelStack.remove(indentLevelStack.size() - 1);
                                  return symbol(ChocoPyTokens.DEDENT, dedentLevel);
                                }
                                return symbol(ChocoPyTokens.NEWLINE); 
                              }

  {Indent}                    {   
                                if (indentLevelStack.size() == 0) {
                                  indentLevelStack.add(0);
                                }
                                processIndent(yytext().substring(1));
                                Symbol result = endIndentOrDedent(); // always dedents if tab is > 0
                                resetAfterIndent();
                                return result;
                              }

  /* Whitespace. */
  {WhiteSpace}                { /* ignore */ }
  {Tab}                       { /* ignore */ }
  {Comments}                  { /* ignore */ }


  /* Literals. */
  {IntegerLiteral}            { return symbol(ChocoPyTokens.NUMBER, Integer.parseInt(yytext())); }
  {BooleanLiterals}           { return symbol(ChocoPyTokens.BOOLEANLITERALS, yytext());}
  {NoneLiteral}               { return symbol(ChocoPyTokens.NONELITERAL, yytext());}
  {StringLiteral}             { String matched = yytext();
                                matched = matched.substring(1, matched.length() - 1);
                                return symbol(ChocoPyTokens.STRINGLITERAL, matched); 
                              }
  {LBracket}                  { return symbol(ChocoPyTokens.LBRACKET); }
  {RBracket}                  { return symbol(ChocoPyTokens.RBRACKET); } 
  {LParentheses}              { return symbol(ChocoPyTokens.LPARENTHESES); }
  {RParentheses}              { return symbol(ChocoPyTokens.RPARENTHESES); } 
  {Comma}                     { return symbol(ChocoPyTokens.COMMA); }

  

  /* Operators. */
  "+"                         { return symbol(ChocoPyTokens.PLUS, yytext()); }
  "-"                         { return symbol(ChocoPyTokens.MINUS, yytext());}
  "*"                         { return symbol(ChocoPyTokens.MULTIPLY, yytext());}
  "%"                         { return symbol(ChocoPyTokens.MODULUS, yytext());}
  "//"                        { return symbol(ChocoPyTokens.FLOORDIVISION, yytext());}
  "=="                        { return symbol(ChocoPyTokens.EQ, yytext());}
  "="                         { return symbol(ChocoPyTokens.ASSIGNMENT, yytext()); }
  "**"                        { return symbol(ChocoPyTokens.EXPONENT, yytext());}
  ">"                         { return symbol(ChocoPyTokens.GT, yytext());}
  "<"                         { return symbol(ChocoPyTokens.LT, yytext());}
  ">="                        { return symbol(ChocoPyTokens.GTE, yytext());}
  "<="                        { return symbol(ChocoPyTokens.LTE, yytext());}
  ":"                         { return symbol(ChocoPyTokens.COLON, yytext());}
  "."                         { return symbol(ChocoPyTokens.DOT);}
  "->"                        { return symbol(ChocoPyTokens.RIGHTARROW);}
  "and"                       { return symbol(ChocoPyTokens.AND, yytext());} 
  "not"                       { return symbol(ChocoPyTokens.NOT, yytext());}
  "or"                        { return symbol(ChocoPyTokens.OR, yytext());}

  /* Control Structures */
  "if"                        { return symbol(ChocoPyTokens.IF, yytext());} 
  "else"                      { return symbol(ChocoPyTokens.ELSE, yytext());}
  "elif"                      { return symbol(ChocoPyTokens.ELIF, yytext());}
  "while"                     { return symbol(ChocoPyTokens.WHILE, yytext());}
  "for"                       { return symbol(ChocoPyTokens.FOR, yytext());}
  "def"                       { return symbol(ChocoPyTokens.DEF);}
  "in"                        { return symbol(ChocoPyTokens.IN, yytext());}
  "return"                    { return symbol(ChocoPyTokens.RETURN, yytext());}

  /* Other Keywords */  
  "pass"                      { return symbol(ChocoPyTokens.PASS, yytext());}

  {Identifier}                { return symbol(ChocoPyTokens.IDENTIFIER, yytext()); }

}


<<EOF>>                       { 
                                if (indentLevelStack.size() > 1) { // don't pop off index 0, indentLevelStack(0) == 0
                                  zzAtEOF = false;
                                  Integer stackLevel = indentLevelStack.remove(indentLevelStack.size() - 1);
                                  return symbol(ChocoPyTokens.DEDENT, stackLevel);
                                } 
                                zzAtEOF = true;
                                return symbol(ChocoPyTokens.EOF); 
                              } 

/* Error fallback. */
[^]                           { return symbol(ChocoPyTokens.UNRECOGNIZED, yytext()); }
