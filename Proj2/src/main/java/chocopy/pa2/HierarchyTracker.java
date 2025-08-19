package chocopy.pa2;

import chocopy.common.analysis.types.*;
import chocopy.common.astnodes.*;
import java.util.HashSet;
import java.util.ArrayList;


public class HierarchyTracker {

    /* Tracks only classes. */
    private final TreeNode root;

    public TreeNode currNode;

    /* A list of all classes initialized, ignoring hierarchies. */
    private final HashSet<String> allClasses;

    private final ArrayList<ArrayList<String>> mappings; // memoization of superclasses and such from building the tree

    public HierarchyTracker() {
        VarTable<Type> curr = new VarTable<>();
        root = new TreeNode(null, "object", null, false, curr); // no need to update parent on root since it's null
        // root.setVarTable(curr);
        currNode = root;
        curr.setNode(root);
        allClasses = new HashSet<>();
        mappings = new ArrayList<>();
    }

    public HierarchyTracker(VarTable<Type> sym) {
        root =  new TreeNode(null, "object", null, false, sym);
        // root.setVarTable(sym);
        currNode = root;
        sym.setNode(root);
        allClasses = new HashSet<>();
        mappings = new ArrayList<>();
    }

    public void addClass(String name) {
        allClasses.add(name);
    }

    public HashSet<String> getAllClasses() {
        return allClasses;
    }

    public TreeNode getRoot() {
        return root;
    }

    /* Looks from the given startPoint towards the parents. 
     * Assumes that className has already been added and checks for superClass.
     * Looks upwards first before going down the tree for time cost optimization.
     * Looks for only the first match.
     * Can be edited / extended to a thorough version that checks for all matches by
     * having a list of matched nodes and changing the startpoint to be the superclass's
     * node after getting the match. 
    */
    public TreeNode findNode(ClassDef node, TreeNode startPoint) { 
        String className = node.name.name;
        String superClass = node.superClass.name;
        if (startPoint == null) {
            return null;
        }
        else if (superClass == null) {
            // String className, TreeNode startPoint, boolean findSuperclassNode
            return findClassNode(className, root, false, true);
        }
        TreeNode target = findMemberNode(superClass, className, startPoint, false);
        if (target == null) {
            target = findMemberNode(superClass, className, startPoint, true);
        }
        return target;
    }

    /* Looks from the given startPoint towards the parents. 
     * Assumes that className has already been added and checks for superClass.
     * Looks upwards first before going down the tree for time cost optimization.
     * Looks for only the first match.
     * Can be edited / extended to a thorough version that checks for all matches by
     * having a list of matched nodes and changing the startpoint to be the superclass's
     * node after getting the match. 
    */
    public TreeNode findNode(String className, String memberName, TreeNode startPoint, boolean isClass) { 
        if (startPoint == null) {
            return null;
        }
        else if (className == null) {
            // String className, TreeNode startPoint, boolean findSuperclassNode
            return findClassNode(className, root, false, isClass);
        }
        TreeNode target = findMemberNode(className, memberName, startPoint, false);
        if (target == null) {
            target = findMemberNode(className, memberName, startPoint, true);
        }
        return target;
    }


    
    /* Looks only for direct members either above or below the tree depending on findSuperClass. 
     * If a superclass is put as className and the subClass as memberName, it returns the node representing
     * the block of the superclass in which the subClass is defined.
    */
    public TreeNode findMemberNode(String className, String memberName, TreeNode startPoint, boolean findSuperclassNode) {
        TreeNode classNode = findClassNode(className, startPoint, findSuperclassNode, false);
        if (classNode != null) {
            VarTable<Type> curr = classNode.getSymbolTable();
            if (curr.declares(memberName)) {
                return classNode;
            }
        }
        return null;
    }

    /* Looks only for direct members either above or equal to the given node level. */
    public TreeNode findMemberNode(String memberName, TreeNode startPoint) {
        if (startPoint.declares(memberName)) {
            return startPoint;
        }
        for (TreeNode n: startPoint.getChildren()) {
            TreeNode ret = findMemberNode(memberName, n);
            if (ret != null) {
                return ret;
            }
        }
        return null;
    }

    /* Looks only for direct members either above or below the tree depending on findSuperClass. */
    public Type findMember(String className, String memberName, TreeNode startPoint, boolean findSuperclassNode) {
        TreeNode classNode = findClassNode(className, startPoint, findSuperclassNode, false);
        if (classNode != null) {
            VarTable<Type> curr = classNode.getSymbolTable();
            if (curr.declares(memberName)) {
                return curr.get(memberName);
            }
        }
        return null;
    }

    /* Looks by going up the tree because of inheritance. Does not check for the class. */
    public Type findMember(String memberName, TreeNode startPoint) {
        VarTable<Type> curr = startPoint.getSymbolTable();
        if (curr.declares(memberName)) {
            return curr.get(memberName);
        }
        // look through children
        while (startPoint != root && startPoint != null) {
            curr = startPoint.getSymbolTable();
            if (curr.declares(memberName)) {
                return curr.get(memberName);
            }
            startPoint = startPoint.getParent();
        }
        return null;
    }

    /** Returns the node with a name CLASSNAME or that declares the given member. */
    public TreeNode findClassNode(String name, TreeNode startPoint, boolean findSuperclassNode, boolean isClass) {
        if (name == null || name.equals("") && findSuperclassNode) { // just going up
            return root;
        }
        if (isClass && startPoint.getName().equals(name)) {
            return startPoint;
        }
        else if (!isClass && startPoint.declares(name)) {
            return startPoint;
        }
        if (findSuperclassNode) {
            // look at startPoint, going up to superclasses
            // not recursive; no need to due to 1 to many nature of parents and children
            // goes up and laterally
            while (startPoint != null) {
                if (isClass && startPoint.getName().equals(name)) {
                    return startPoint;
                } 
                else if (!isClass && startPoint.declares(name)) {
                    return startPoint;
                }
                else {
                    if (isClass && startPoint.containsClass(name)) {
                        // searching for class
                        for (TreeNode n: startPoint.getChildren()) {
                            if (n.getName().equals(name)) {
                                return n;
                            }
                        }
                    }
                    else if (!isClass) {
                        if (startPoint.declares(name)) {
                            return startPoint;
                        }
                        for (TreeNode n: startPoint.getChildren()) {
                            if (n.declares(name)) {
                                return n;
                            }
                        }
                        // searching for variable
                    }
                    startPoint = startPoint.getParent();
                }
            }
            // return findClassNode(name, originalStart, findSuperclassNode, false);
        }
        else {
            // look at startPoint, going down to subclasses
            // recursive due to expansive nature of children
            for (TreeNode n : startPoint.getChildren()) {
                TreeNode ret = findClassNode(name, n, false, isClass);
                if (ret != null) {
                    return ret;
                }
            }
        }
        return null;
    }

    
    
    /** Returns the node with a name CLASSNAME or that declares the given member. */
    @SuppressWarnings("unlikely-arg-type")
    public TreeNode findClassNode(String name, String member, TreeNode startPoint, boolean findSuperclassNode) {
        if (startPoint.getParent() == null && findSuperclassNode) {
            return null;
        }
        if (startPoint.declares(member) && startPoint.getName().equals(name)) {
            return startPoint;
        }
        // if (findSuperclassNode && startPoint.getName().equals(name)) { 
        if (findSuperclassNode && startPoint.getName().equals(name)) { 
            // subclasses can use superclass methods but not viceversa
            // going bottom up, so the class could come before the method (i.e. B.get_A where A > B, B is the subclass)
            // findClassNode(String name, TreeNode startPoint, boolean findSuperclassNode, boolean isClass)
            return findClassNode(member, startPoint, true, false);
        }
        else if (!findSuperclassNode && startPoint.declares(member)) {
            // A.get_A >> B.get_A
            // going top down, so the member will come before the class (ex: B.get_A)
            // if (startPoint.getClass().equals(name)) {
            //     return startPoint;
            // }
            // for (TreeNode n : startPoint.getChildren()) {
            //     TreeNode ret = findClassNode(name, n, false, true);
            //     if (ret != null) {
            //         return ret;
            //     }
            // }
            boolean check = verifyInherited(name, startPoint);
            if (check) {
                return startPoint;
            }
        }
        if (findSuperclassNode) {
            // look at startPoint, going up to superclasses
            // not recursive; no need to due to 1 to many nature of parents and children
            // goes up and laterally
            for (TreeNode n: startPoint.getChildren()) {
                if (n.getName().equals(name)) {
                    TreeNode ret = findClassNode(member, n, findSuperclassNode, false);
                    if (ret != null) {
                        return ret;
                    }
                }
            }
            return findClassNode(name, member, startPoint.getParent(), findSuperclassNode);
            // return findClassNode(name, originalStart, findSuperclassNode, false);
        }
        else if (!findSuperclassNode) {
            // look at startPoint, going down to subclasses
            // recursive due to expansive nature of children
            // going top down, so the member will come before the class (ex: B.get_A)
            for (TreeNode n: startPoint.getChildren()) {
                TreeNode ret = findClassNode(name, member, n, findSuperclassNode);
                if (ret != null) {
                    return ret;
                }
            }
            return null;
        }
        return null;
    }
    
    // Verifies that class inherits from startPoint. Checks that C is the class of startPoint or of a child it has.
    public boolean verifyInherited(String c, TreeNode startPoint) {
        if (startPoint.getName().equals(c)) {
            return true;
        }
        for (TreeNode n : startPoint.getChildren()) {
            if (n.getName().equals(c)) {
                return true;
            }
            return verifyInherited(c, n);
        }
        return false;
    }
}
