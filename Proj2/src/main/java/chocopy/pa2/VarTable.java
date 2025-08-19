package chocopy.pa2;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Arrays;

import chocopy.common.analysis.SymbolTable;
import chocopy.common.analysis.types.*;

/** A block-structured symbol table a mapping identifiers to information
 *  about them of type T in a given declarative region. */
@SuppressWarnings("hiding")
public class VarTable<Type> extends SymbolTable<Type> {

    /** Contents of the current (innermost) region. */
    private final Map<String, Type> tab = new HashMap<>();
    
    /** Enclosing block. */
    private final VarTable<Type> parent;

    /** Direct children VarTables. */
    private final HashMap<String, VarTable<Type>> children; // issue: currently only tracks nested funcs and classes, not scopes like forstmt and whilestmt

    private final int mre_scope; // from HierarchyTracker

    /* An entry is in the following form:
     * ".superclass.subclass.subsubclass.subsubsubclass."
     * and each subsequent addition is followed by a period.
     * Nothing is added for the global level. 
     * This enables avoiding key errors from having
     * nested classes in different blocks with the same name.
    */
    private String classHierarchy;

    private final String currentClass;

    private TreeNode currNode;

    /** A table representing a region nested in that represented by
     *  PARENT0. 
     * incr_scope is true only when new classes or functions are made. */
    public VarTable(VarTable<Type> parent0, boolean incr_scope, String currClass, boolean isFunc) {
        parent = parent0;
        children = new HashMap<>();
        currentClass = currClass;
        if (incr_scope) {
            mre_scope = parent0.getScopeLevel() + 1;
            // classHierarchy = parent0.getHierarchy() + currentClass + ".";
            // children = new HashMap<>();
        }
        else {
            mre_scope = parent0.getScopeLevel();
            // classHierarchy = parent0.getHierarchy() + "[" + parentType + "]";
            // children = parent0.getChildren();
        }
    }

    public String getCurrentClass() {
        return currentClass;
    }

    public void setNode(TreeNode n) {
        currNode = n;
        if (n.getParent() != null) {
            n.getParent().addChild(n);
        }
    }

    /** A top-level symbol table. 
     * This constructor should never be called.
    */
    public VarTable() {
        this.parent = null;
        classHierarchy = ""; // does not include 0global by default
        mre_scope = 0;
        children = new HashMap<>();
        currNode = new TreeNode(null, "object", null, false);
        currentClass = "";
    }

    public TreeNode getNode() {
        return currNode;
    }

    public HashMap<String, VarTable<Type>> getChildren() {
        return children;
    }

    public void addToChildren(VarTable<Type> table, String name) {
        children.put(name, table);
    }

    public VarTable<Type> getChildTable(String name) {
        VarTable<Type> ret = children.get(name);
        if (ret == null) {
            return this;
        }
        return ret;
    }

    public int getScopeLevel() {
        return mre_scope;
    }

    /** Returns the mapping of NAME in the innermost nested region
     *  containing this one. */
    public Type get(String name) {
        if (tab.containsKey(name)) {
            return tab.get(name);
        } else if (parent != null) {
            return parent.get(name);
        } else {
            return null;
        }
    }

    /** Adds a new mapping of NAME -> VALUE to the current region, possibly
     *  shadowing mappings in the enclosing parent. Returns modified table. */
    public VarTable<Type> put(String name, Type value) {
        tab.put(name, value);
        return this;
    }

    /** Returns whether NAME has a mapping in this region (ignoring
     *  enclosing regions. */
    public boolean declares(String name) {
        return tab.containsKey(name);
    }

    /** Returns all the names declared this region (ignoring enclosing
     *  regions). */
    public Set<String> getDeclaredSymbols() {
        return tab.keySet();
    }

    /** Returns the parent, or null if this is the top level. */
    public VarTable<Type> getParent() {
        return parent;
    }

    public String getHierarchy() {
        return classHierarchy;
    }

    public void addToHierarchy(String className) { // cannot remove from hierarchy
        classHierarchy += className + ".";
    }

    public boolean containsClass(String name) {
        return getHierarchy().contains(name);
    }

    public boolean isBuiltInType(String name) {
        List<String> types = Arrays.asList("int", "bool", "char", "float", "str", "object"); // "list"?
        if (types.contains(name)) {
            return true;
        }
        return false;
    }

}
