package chocopy.pa2;

import chocopy.common.analysis.types.*;

public class Entry {
    String symbolName;
    Type type;
    boolean isFunction; // if this is a function, Type becomes the return type

    public Entry(String name, Type t) {
        symbolName = name;
        type = t;
        isFunction = false; // will always be false until TypeChecker parses return statements
    }

    void setFuncStatus(boolean status) {
        isFunction = status;
    }

    String getSymbolName() {
        return symbolName;
    }

    boolean isFunction() {
        return isFunction;
    }

    void setType(Type newType) {
        // used only for functions
        type = newType;
    }

    Type getType() {
        return type;
    }

    @Override
    public String toString() {
        return "[name: " + symbolName + ", type: " + type.className() + "]";
    }
}
