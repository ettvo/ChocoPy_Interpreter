package chocopy.pa2;

import java.util.ArrayList;
import java.util.Set;
import chocopy.common.analysis.types.*;

public class TreeNode {

    // parent = superclass -> 1 to many to children

    private final TreeNode parent; // superclass
    private final ArrayList<TreeNode> children; // subclasses
    private final String className;
    private Type type;
    private final boolean isFunction;
    private VarTable<Type> symbols; // contains only the class's immediate (not inherited) methods and variables

    // object is the global class
    // this does not track non-classes and non-funcs (that is handled by the symbol table instead bc those are nested)

    public TreeNode(TreeNode p, String name, Type t, boolean isFunc, VarTable<Type> sym) { // just for 
        parent = p;
        className = name;
        type = t; // may change from null to a non-null in the case of functions with return types
        children = new ArrayList<>();
        isFunction = isFunc;
        symbols = sym; 
    }
    public TreeNode(TreeNode p, String name, Type t, boolean isFunc) { // just for 
        parent = p;
        className = name;
        type = t; // may change from null to a non-null in the case of functions with return types
        children = new ArrayList<>();
        isFunction = isFunc;
        symbols = null;
    }

    public VarTable<Type> getSymbolTable() {
        return symbols;
    }

    // Always run after instantiating
    public void setVarTable(VarTable<Type> curr) {
        symbols = curr;
    }

    public boolean isFunction() {
        return isFunction;
    }

    public Set<String> getSymbols() {
        return symbols.getDeclaredSymbols();
    }

    public boolean isRoot() {
        return parent == null;
    }

    public void addChild(TreeNode child) {
        children.add(child);
    }

    public TreeNode findSuperclassNode(String name) {
        if (className.equals(name)) {
            return this;
        }
        if (parent != null) {
            return parent.findSuperclassNode(name);
        }
        return null;
    }

    public TreeNode findDirectSubclassNode(String name) {
        for (TreeNode n : children) {
            if (n.getName().equals(name)) {
                return n;
            }
        }
        return null;
    }

    public boolean containsClass(String name) {
        for (TreeNode n : children) {
            if (n.getName().equals(name)) {
                return true;
            }
        }
        return false;
    }

    public Type getType() {
        return type;
    }

    public void setType(Type t) {
        type = t;
    }

    public VarTable<Type> getParentSymbols() {
        return parent.getSymbolTable();
    }

    public Type getSymbol(String name) {
        if (declares(name)) {
            return symbols.get(name);
        }
        else if (parent != null) {
            return parent.getSymbol(name);
        }
        return null;
    }

    public String getName() {
        return className;
    }

    public TreeNode getParent() {
        return parent;
    }

    public ArrayList<TreeNode> getChildren() {
        return children;
    }
    
    /** Declares member. Could also be declaring a function, however. */
    public boolean declares(String name) {
        return getSymbols().contains(name);
    }

    @Override
    public String toString() {
        if (parent == null) {
            return className + "(root)" + ", children: [" + children + "]";
        }
        return "{" + parent.getName() + ", classname `" + className + "`, symbols: {" +  getSymbols() + "}, children: [" + children.toString() + "]" + "}";
    }

    // java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy \--pass=.s src/test/data/pa2/sample/class_def_methods.py.ast
    // java -cp "chocopy-ref.jar:target/assignment.jar" chocopy.ChocoPy \--pass=.s src/test/data/pa2/sample/strings.py.ast
}
