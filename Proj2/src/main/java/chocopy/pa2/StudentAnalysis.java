package chocopy.pa2;

import chocopy.common.analysis.SymbolTable;
import chocopy.common.analysis.types.Type;
import chocopy.common.astnodes.Program;
import java.util.HashSet;
/** Top-level class for performing semantic analysis. */
public class StudentAnalysis {

    /** Perform semantic analysis on PROGRAM, adding error messages and
     *  type annotations. Provide debugging output iff DEBUG. Returns modified
     *  tree. */
    public static Program process(Program program, boolean debug) {
        if (program.hasErrors()) {
            return program;
        }

        DeclarationAnalyzer declarationAnalyzer =
            new DeclarationAnalyzer(program.errors);
        program.dispatch(declarationAnalyzer);
        
        VarTable<Type> globalSym =
            declarationAnalyzer.getGlobals();

        HierarchyTracker htracker = declarationAnalyzer.getHierarchyTracker();
        
        if (globalSym == null) {
            System.out.println("globalSym null in StudentAnalysis");
        }
        // VarTable<Type> globalSym =
        //     new VarTable<>();

        if (!program.hasErrors()) {
            TypeChecker typeChecker =
                new TypeChecker(globalSym, program.errors, htracker, declarationAnalyzer);
            program.dispatch(typeChecker);
        }

        return program;
    }
}
