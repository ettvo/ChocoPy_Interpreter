package chocopy.pa2;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

import com.fasterxml.jackson.annotation.JsonCreator;

import chocopy.common.analysis.AbstractNodeAnalyzer;
import chocopy.common.analysis.NodeAnalyzer;
import chocopy.common.analysis.SymbolTable;
import chocopy.common.analysis.types.*;
import chocopy.common.astnodes.*;
import java_cup.runtime.ComplexSymbolFactory.Location;

/**
 * All analyze functions of this file should return a type from chocopy.common.analysis.types.
 */

/**
 * Analyzes declarations to create a top-level symbol table.
 */
    public class DeclarationAnalyzer extends AbstractNodeAnalyzer<Type> {


    /** Current symbol table.  Changes with new declarative region. */
    private VarTable<Type> sym = new VarTable<>();
    
    /** Global symbol table. */
    private final VarTable<Type> globals = sym;

    /** Receiver for semantic error messages. */
    private final Errors errors;

    /* Keeps track of scope level and class hierarchies. 
     * See: HierarchyTracker and VarTable for more.
     */
    private final HierarchyTracker htracker;

    /** Global "class". Non-null for testing purposes. */
    private final String globalClass = "0Global"; 

    TreeNode curr;

    public HierarchyTracker getHierarchyTracker() {
        return htracker;
    }

    /** A new declaration analyzer sending errors to ERRORS0. */
    public DeclarationAnalyzer(Errors errors0) {
        errors = errors0;
        htracker = new HierarchyTracker(sym);
        curr = htracker.getRoot();
        sym.setNode(htracker.getRoot());
    }

    public void getAnalysis(Declaration d, VarTable<Type> t) {
        sym = t;
        d.dispatch(this);
    }

    /** Inserts an error message in NODE if there isn't one already.
     *  The message is constructed with MESSAGE and ARGS as for
     *  String.format. */
    private void err(Node node, String message, Object... args) {
        errors.semError(node, message, args);
    }

    public void addSymbol(Identifier id, Type type) {
        String name = id.name;
        // if (type == null || decl instanceof ClassDef) {
        //     return;
        // }
        if (type == null) {
            return;
        }

        if (isInvalidName(name) || sym.declares(name)) {
            err(id,
                "Duplicate declaration of identifier in same "
                + "scope: %s",
                name);
        }
        else if (!sym.declares(type.className()) && !isBuiltInType(type.className())) {
            err(id, "Invalid type annotation; there is no class named: %s", type.className());
        }
        else {
            sym.put(name, type);
        }
    }

    @Override
    public Type analyze(Program program) {
        handleDeclarations(program.declarations);
        return null;
    }

    /* Declarations:
     * - VarDef
     * - ClassDef
     * - FuncDef
     * - GlobalDecl // add to symbol table w/o checking for duplicates, but do check that it exists
     * - nonLocal // add to symbol table w/o checking for duplicates, but do check that it exists
     */

    // @Override
    // public Type analyze(Declaration d) {

    // }

    public void handleDeclarations(List<Declaration> declarations) {
        for (Declaration decl : declarations) {
            decl.dispatch(this);
        }
    }

    public void handleDeclarations(List<Declaration> declarations, VarTable<Type> t) {
        VarTable<Type> prev = sym;
        sym = t;
        for (Declaration decl : declarations) {
            decl.dispatch(this);
        }
        sym = prev;
    }

    public void handleDeclarations(Declaration decl, VarTable<Type> t) {
        VarTable<Type> prev = sym;
        sym = t;
        decl.dispatch(this);
        sym = prev;
    }

    public void handleDeclarations2(List<Declaration> declarations) {
        for (Declaration decl : declarations) {
            Identifier id = decl.getIdentifier();
            String name = id.name;

            Type type = decl.dispatch(this);
            // if (type == null || decl instanceof ClassDef) {
            //     continue;
            // }
            addSymbol(id, type);
            // addNonlocalSymbol
            // addGlobalSymbol
        }
    }

    public void handleStatements(List<Stmt> stmts) {
        // Assign
        // Expr
        // For
        // If
        // While
        // Return
        for (Stmt s: stmts ) {
            Type type = s.dispatch(this);
            // addNonlocalSymbol
            // addGlobalSymbol
        }
    }
    

    // public void handleDeclarations1(List<Declaration> declarations) {
    //     for (Declaration d: declarations) {
    //         Type currDecl = d.dispatch(this); 
    //         if (currDecl != null) {
    //             String name = d.getIdentifier().name;
    //             if (name != null) {
    //                 if (d instanceof VarDef) {
    //                     String declType = currDecl.className();
    //                     if (isInvalidName(name) || sym.declares(name)) { //
    //                         err(d.getIdentifier(),
    //                                         "Duplicate declaration of identifier in same "
    //                                         + "scope: %s",
    //                                         name);
    //                         ((VarDef)d).value.setInferredType(Type.OBJECT_TYPE);
    //                     } 
    //                     else if (!sym.declares(declType) && !isDeclaredType(declType)) {
    //                         err(d.getIdentifier(), "Invalid type annotation; there is no class named: %s", declType);
    //                         ((VarDef)d).value.setInferredType(Type.OBJECT_TYPE);
    //                     }
    //                     else {
    //                         sym.put(name, currDecl);
    //                         ((VarDef)d).value.setInferredType(currDecl);
    //                     }
    //                 }
    //                 else if (d instanceof FuncDef) {
    //                     FuncDef node = (FuncDef)d;
    //                     Identifier funcName = node.name;
    //                     String funcNameString = funcName.name;
    //                     VarTable<Type> newFunc = new VarTable<>(sym, true, funcNameString, true);
    //                     newFunc.setNode(sym.getNode());
    //                     sym.addToChildren(newFunc, funcNameString);
    //                     boolean needsSelfParam = isClassMethod();
                        
                    
    //                     node.name.setInferredType(currDecl);
    //                     if (sym.declares(funcNameString) || isInvalidName(funcNameString)) {
    //                         err(funcName, "Duplicate declaration of identifier in same scope: %s", funcNameString);
    //                     } 
    //                     else if (!sym.declares(funcNameString) && !isInvalidName(funcNameString)) {
    
    //                         sym.put(funcNameString, currDecl); 
    //                     }
    //                     sym = newFunc;
    //                     for (int i = 0; i < node.params.size(); i += 1) {
    //                         TypedVar currVar = node.params.get(i);
    //                         if ((i > 0 && needsSelfParam) || !needsSelfParam) {
    //                             ValueType currType = ValueType.annotationToValueType(currVar.type);
    //                             if (isClassMethod() && i == 0) {
    //                                 continue;
    //                             }
    //                             if (newFunc.declares(currVar.identifier.name) || isInvalidName(currVar.identifier.name)) {
    //                                 err(currVar.identifier,
    //                                                 "Duplicate declaration of identifier in same "
    //                                                 + "scope: %s",
    //                                                 currVar.identifier.name);
    //                             }
    //                             else if (!newFunc.declares(currType.toString()) && !isDeclaredType(currType.toString())) {
    //                                 err(node.getIdentifier(), "Invalid type annotation; there is no class named: %s", currVar.identifier.name);
    //                             }
    //                             else {
    //                                 newFunc.put(currVar.identifier.name, currType);
    //                             }
    //                         }
    //                     }
    //                     handleDeclarations(node.declarations);
    //                     sym = newFunc.getParent();

    //                 }
    //             }
    //         }
        
    //     }
    // }

    // /* For use when you need to track a className. In other words, this is for use with FuncDef to track the function name. */
    // public void handleDeclarations2(List<Declaration> declarations, String className) {
    //     int counter = 0;
    //     for (Declaration d: declarations) {
    //         Type currDecl = d.dispatch(this); 
    //         if (currDecl != null) {
    //             String name = d.getIdentifier().name;
    //             if (name.equals("self") && counter == 0) {
    //                 counter += 1;
    //                 break;
    //             }
    //             if (d instanceof FuncDef) {
    //                 FuncDef func = (FuncDef)d;
    //                 Identifier funcName = func.name;
    //                 String funcNameString = funcName.name;
    //                 TypedVar currVar = func.params.get(0);
    //                 String paramName = currVar.identifier.name;
    //                 TypeAnnotation currParamClass = currVar.type;
    //                 if (!paramName.equals("self") || !(currParamClass instanceof ClassType) || !(((ClassType)currVar.type).className.equals(className))) {  // get classvaluetype
    //                     err(d.getIdentifier(), "First parameter of the following method must be of the enclosing class: %s", funcNameString);
    //                 }
    //                 else {
    //                     sym.put(funcNameString, ValueType.annotationToValueType(func.returnType));
    //                 }
    //             }
    //         }
    //     }
    // }

    @Override
    public Type analyze(VarDef node) {

        ValueType curr = ValueType.annotationToValueType(node.var.type);
        String varType = curr.className(); // check if builtIn or declared
        String varName = node.var.identifier.name;
        if (!sym.declares(varType) && !isDeclaredType(varType)) {
            err(node.getIdentifier(), "Invalid type annotation; there is no class named: %s", varType);
            return node.value.setInferredType(Type.OBJECT_TYPE);
        }
        Type val = node.value.dispatch(this); 
        node.value.setInferredType(val);


        Identifier id = node.getIdentifier();
        // // Type t = ValueType.annotationToValueType(node.var.type);
        // Type type = node.value.setInferredType(ValueType.annotationToValueType(node.var.type));
        // // id.setInferredType(ValueType.annotationToValueType(node.var.type));
        // type = node.value.dispatch(this);
        // id.setInferredType(type);
        addSymbol(id, curr);
        return val;
    }

    @Override
    public Type analyze(IntegerLiteral node) {
        return Type.INT_TYPE;
    }

    @Override
    public Type analyze(BooleanLiteral node) {
        return Type.BOOL_TYPE;
    }

    @Override
    public Type analyze(NoneLiteral node) {
        return Type.NONE_TYPE;
    }
    
    @Override
    public Type analyze(StringLiteral node) {
        return Type.STR_TYPE;
    }

    @Override
    public Type analyze(ListType node) {
        return new ListValueType(node);
    }

    @Override
    public Type analyze(TypedVar node) {
        return ValueType.annotationToValueType(node.type);
    }


    @Override
    public Type analyze(ClassDef node) {
        // members: funcdef, classdef, globaldecl, nonlocaldecl, vardef
        // this is the only place that the classHierarchy in varTable and TypeChecker classHierarchies should be edited
        String className = node.name.name;
        ClassValueType curr = new ClassValueType(className);
        
        String superClass = node.superClass.name;

        if (isInvalidName(className)) {
            err(node.name,
                            "Duplicate declaration of identifier in same "
                            + "scope: %s",
                            className);
        }
        else {
            addSymbol(node.getIdentifier(), curr);
        }
        htracker.addClass(className);


        TreeNode superClassNode = htracker.findClassNode(superClass, sym.getNode(), true, true);
        if (superClassNode == null) {
            superClassNode = htracker.findClassNode(superClass, htracker.getRoot(), false, true);
        }
        
        VarTable<Type> newFunc = new VarTable<Type>(sym, true, className, false);
        TreeNode newNode = new TreeNode(superClassNode, className, curr, false, newFunc); // sets parent as 
        newFunc.setNode(newNode);
        if (superClassNode != null) {
            superClassNode.addChild(newNode);
        }
        
        // here
        // sym.put(className, curr);
        newFunc.put("self", curr);
        newFunc.put(className, new FuncType(curr)); // constructor
        newFunc.addToHierarchy(className); // ????????

        sym.addToChildren(newFunc, className);
        sym = newFunc;
        handleDeclarations(node.declarations); // check the vardefs
        // handleDeclarations(node.declarations, className); // check the function defs

        // if (newFunc.getParent() == null) {
        //     err(node, "Return on global scope");
        // }

        sym = newFunc.getParent(); // should never be null
        return curr; // set to null if it shows up too much on the symbol table
    }


    // @Override
    // public Type analyze(FuncDef node) {
    //     List<ValueType> params = new ArrayList<>();
    //     ValueType returnType = ValueType.annotationToValueType(node.returnType);
    //     for (int i = 0; i < node.params.size(); i += 1) {
    //         params.add(ValueType.annotationToValueType(node.params.get(i).type));
    //     }
    //     FuncType ret = null;
    //     if (params.size() == 0) {
    //         ret = new FuncType(returnType);
    //     }
    //     else {
    //         ret = new FuncType(params, returnType);
    //     }
    //     addSymbol(node.getIdentifier(), ret);
    //     VarTable<Type> newFunc = new VarTable<Type>(sym, true, sym.getCurrentClass(), false);
    //     sym.addToChildren(newFunc, node.name.name);
    //     sym = newFunc;
    //     handleDeclarations(node.declarations);
    //     sym = newFunc.getParent();
    //     return ret;
    // }
    
    @Override
    public Type analyze(GlobalDecl node) {
        // todo
        Identifier id = node.getIdentifier();
        String name = id.name;
        VarTable<Type> globalTable = getGlobals();
        if (!globalTable.declares(name)) {
            err(node, "Global variable DNE: %s", name);
            return null; 
        }
        else if (globalTable.equals(sym)) {
            err(node, "Illegal declaration of global variable at global level: %s", name);
            return null; 
        } 
        else {
            return globalTable.get(name);
        }
    }

    @Override
    public Type analyze(NonLocalDecl node) {
        Identifier id = node.getIdentifier();
        String name = id.name;
        Type curr = sym.get(name); 
        VarTable<Type> globalTable = getGlobals();
        if (globalTable.declares(name)) {
            err(node, "Illegal global declaration of nonlocal variable: %s", name);
            return null; 
        }
        else if (sym.getParent() == null || sym.getParent().equals(globalTable)) {
            err(node, "Illegal declaration of nonlocal variable outside of nested function: %s", name);
            return null; 
        }
        else if (curr == null) {
            err(node, "Invalid nonlocal: %s", name);
            return null; 
        }
        return curr;
    }

    /** Helpers. */
    
    /* Returns True if SUB is a subset of SUPERSET. For use when checking entries of lists in analyze(AssignStmt node).
     * Ex: if SUPER is Type.OBJECT_TYPE, isSupersetType returns True for everything
     * Ex: if SUB is Type.NONE_TYPE returns True for every value of SUPER
     * For this, INT is NOT a subset of BOOL
    */
    public boolean isSupersetType(Type superset, Type subset) {
        Type superset_type = superset;
        Type subset_type = subset;

        if (superset == null) {
            return false;
        }
        else if (superset == null || subset == null) {
            return false;
        }
        if (superset.equals(subset)) {
            return true;
        }
        if (superset instanceof ListValueType || superset.isListType()) {
            superset_type = ((ListValueType)superset).elementType();
        }
        if (subset instanceof ListValueType || subset.isListType()) {
            subset_type = ((ListValueType)subset).elementType();
        }
        if (superset.isListType() && subset.isListType()) {
            if (subset_type.equals(superset_type)
            || (subset_type.equals(Type.EMPTY_TYPE) || subset_type.equals(Type.NONE_TYPE))) 
            {
                return true;
            }
        }
        else if ((superset.isListType() && !subset.isListType())) {
            if (superset_type.equals(subset) 
            || superset_type.equals(Type.OBJECT_TYPE)
            || subset.equals(Type.NONE_TYPE) 
            || subset.equals(Type.EMPTY_TYPE)) 
            {
                return true;
            }
        }
        else if (!superset.isListType() && subset.isListType()) {
            if (superset.equals(Type.OBJECT_TYPE)) {
                return true;
            }
        }
        else if (superset_type.equals(Type.OBJECT_TYPE)) {
            // subset being None is valid only if superset is Obj
            return true;
        }
        return false;
    }

    /* For use with GlobalDecl's analyze function. */
    public VarTable<Type> getGlobals() {
        return globals;
    }

    /* Used to check if the current FuncDef is part of a class and therefore needs the "self" param. 
     * Works by checking if the current symbol table is the global symbol table or not. 
    */
    public boolean isClassMethod() {
        return !globals.equals(sym);
    }

    public boolean isInvalidName(String name) {
        List<String> invalidNames = Arrays.asList("self", "int", "bool", "char", "def", "True", "False", "None", "and", "as", 
        "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", 
        "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "print", 
        "raise", "return", "try", "while", "with", "yield", "float", "id", "len", "max", "min", "pow", 
        "range", "round", "str", "type");
        if (invalidNames.contains(name)) {
            return true;
        }
        return false;
    }

    public boolean isBuiltInType(String name) {
        List<String> types = Arrays.asList("int", "bool", "char", "float", "str", "object", "<None>"); // "list"?
        if (types.contains(name) || name == null) { // returned when ValueType type.className() gives a null because of not being from a "class"
            return true;
        }
        return false;
    }

    public boolean isDeclaredType(String name) {
        return isBuiltInType(name) || htracker.getAllClasses().contains(name);
    }
}