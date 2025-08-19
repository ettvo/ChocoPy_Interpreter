package chocopy.pa3;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

// import chocopy.common.analysis.SymbolTable;
// import chocopy.common.analysis.types.FuncType;
// import chocopy.common.analysis.AbstractNodeAnalyzer;
// import chocopy.common.codegen.ClassInfo;
// import chocopy.common.astnodes.Stmt;
// import chocopy.common.astnodes.ReturnStmt;
// import chocopy.common.codegen.CodeGenBase;
// import chocopy.common.codegen.FuncInfo;
// import chocopy.common.codegen.GlobalVarInfo;
// import chocopy.common.codegen.Label;
// import chocopy.common.codegen.Constants;
// import chocopy.common.codegen.RiscVBackend;
// import chocopy.common.codegen.SymbolInfo;

import chocopy.common.codegen.*;
import chocopy.common.Utils;

import chocopy.common.analysis.*;
import chocopy.common.analysis.types.*;
import chocopy.common.astnodes.*;

import static chocopy.common.codegen.RiscVBackend.Register.*;
import chocopy.common.codegen.RiscVBackend.Register;

import java.lang.Math.*;
import java.nio.ByteBuffer;
/**
 * This is where the main implementation of PA3 will live.
 *
 * A large part of the functionality has already been implemented
 * in the base class, CodeGenBase. Make sure to read through that
 * class, since you will want to use many of its fields
 * and utility methods in this class when emitting code.
 *
 * Also read the PDF spec for details on what the base class does and
 * what APIs it exposes for its sub-class (this one). Of particular
 * importance is knowing what all the SymbolInfo classes contain.
 */
public class CodeGenImpl extends CodeGenBase {

    /** A code generator emitting instructions to BACKEND. */
    public CodeGenImpl(RiscVBackend backend) {
        super(backend);
        // // initHelperFunctions();
        // FuncInfo boxPrimitiveFunc = makeFuncInfo("print", 0, Type.INT_TYPE,
        //                          globalSymbols, null, this::emitStdFunc);
        // boxPrimitiveFunc.addParam(makeStackVarInfo("arg", Type.OBJECT_TYPE,
        //                                     null, printFunc));
        // functions.add(boxPrimitiveFunc);
        // globalSymbols.put(boxPrimitiveFunc.getBaseName(), boxPrimitiveFunc);        
    }

    @Override
    /**
    * Generates assembly code for PROGRAM.
    *
    * This is the main driver that calls internal methods for
    * emitting DATA section (globals, constants, prototypes, etc)
    * as well as the the CODE section (predefined functions, built-in
    * routines, and user-defined functions).
    */
    public void generate(Program program) {
        analyzeProgram(program);

        backend.startData();

        for (ClassInfo classInfo : this.classes) {
            emitPrototype(classInfo);
        }

        for (ClassInfo classInfo : this.classes) {
            emitDispatchTable(classInfo);
        }

        for (GlobalVarInfo global : this.globalVars) {
            backend.emitGlobalLabel(global.getLabel());
            emitConstant(global.getInitialValue(), global.getVarType(),
                            String.format("Initial value of global var: %s",
                                        global.getVarName()));
        }

        backend.startCode();

        Label mainLabel = new Label("main");
        backend.emitGlobalLabel(mainLabel);
        backend.emitLUI(A0, HEAP_SIZE_BYTES >> 12,
                        "Initialize heap size (in multiples of 4KB)");
        backend.emitADD(S11, S11, A0, "Save heap size");
        backend.emitJAL(heapInitLabel, "Call heap.init routine");
        backend.emitMV(GP, A0, "Initialize heap pointer");
        backend.emitMV(S10, GP, "Set beginning of heap");
        backend.emitADD(S11, S10, S11,
                        "Set end of heap (= start of heap + heap size)");
        backend.emitMV(RA, ZERO, "No normal return from main program.");
        backend.emitMV(FP, ZERO, "No preceding frame.");

        emitTopLevel(program.statements);

        for (FuncInfo funcInfo : this.functions) {
            funcInfo.emitBody();
        }

        emitStdFunc("alloc");
        emitStdFunc("alloc2");
        emitStdFunc("abort");
        emitStdFunc("heap.init");
        //    System.out.println("Trying to add box_primitive.");
        emitStdFunc(boxPrimitiveLabel, "box_primitive", addedAssemblyDirectory);
        emitStdFunc(transferContentsLabel, "transfer_contents", addedAssemblyDirectory);
        emitStdFunc(unboxPrimitiveLabel, "unbox_primitive", addedAssemblyDirectory);
        // emitStdFunc(boxPrimitiveLabel, addedAssemblyDirectory);
        //    System.out.println("Box primitive added.");

        emitCustomCode();

        backend.startData();
        emitConstants();
    }

    /** Ecall numbers for intrinsic routines. 
        * EXIT_ECALL = 10,
        * EXIT2_ECALL = 17,
        * PRINT_STRING_ECALL = 4,
        * PRINT_CHAR_ECALL = 11,
        * PRINT_INT_ECALL = 1,
        * READ_STRING_ECALL = 8,
        * FILL_LINE_BUFFER__ECALL = 18,
        * SBRK_ECALL = 9
        * Taken numbers: 1, 4, 8, 9, 10, 11, 17, 18
        * Added ecalls: 1, 4, 8, 9, 10, 11, [12], 17, 18
        backend.emitLI(A0, EXIT_ECALL, "Code for ecall: exit");
            backend.emitEcall(null);
    */
    protected final int
    BOX_PRIM_ECALL = 12;

    @Override
        /* Symbolic assembler constants defined here (to add others, override
        * initAsmConstants in an extension of CodeGenBase):
        * ecalls:
        *   @sbrk
        *   @fill_line_buffer
        *   @read_string
        *   @print_string
        *   @print_char
        *   @print_int
        *   @exit2
        * Exit codes:
        *   @error_div_zero: Division by 0.
        *   @error_arg: Bad argument.
        *   @error_oob: Out of bounds.
        *   @error_none: Attempt to access attribute of None.
        *   @error_oom: Out of memory.
        *   @error_nyi: Unimplemented operation.
        * Data-structure byte offsets:
        *   @.__obj_size__: Offset of size of object.
        *   @.__len__: Offset of length in chars or words.
        *   @.__str__: Offset of string data.
        *   @.__elts__: Offset of first list item.
        *   @.__int__: Offset of integer value.
        *   @.__bool__: Offset of boolean (1/0) value.
        */
        /** Define @-constants to be used in assembly code. */
        protected void initAsmConstants() {
        backend.defineSym("sbrk", SBRK_ECALL);
        backend.defineSym("print_string", PRINT_STRING_ECALL);
        backend.defineSym("print_char", PRINT_CHAR_ECALL);
        backend.defineSym("print_int", PRINT_INT_ECALL);
        backend.defineSym("exit2", EXIT2_ECALL);
        backend.defineSym("read_string", READ_STRING_ECALL);
        backend.defineSym("fill_line_buffer", FILL_LINE_BUFFER__ECALL);
        // Added ecalls
        // backend.defineSym("box_primitive", BOX_PRIM_ECALL);

        backend.defineSym(".__obj_size__", 4);
        backend.defineSym(".__len__", 12);
        backend.defineSym(".__int__", 12);
        backend.defineSym(".__bool__", 12);
        backend.defineSym(".__str__", 16);
        backend.defineSym(".__elts__", 16);

        backend.defineSym("error_div_zero", ERROR_DIV_ZERO);
        backend.defineSym("error_arg", ERROR_ARG);
        backend.defineSym("error_oob", ERROR_OOB);
        backend.defineSym("error_none", ERROR_NONE);
        backend.defineSym("error_oom", ERROR_OOM);
        backend.defineSym("error_nyi", ERROR_NYI);
    }



    /** Label for added built-in routine: box_primitive. */
    protected final Label boxPrimitiveLabel = new Label("box_primitive");

    /** Label for added built-in routine: unbox_primitive. */
    protected final Label unboxPrimitiveLabel = new Label("unbox_primitive");

    /** Label for added built-in routine: box_primitive. */
    protected final Label transferContentsLabel = new Label("transfer_contents");

    /** Directory path to the added assembly files. */
    protected final String addedAssemblyDirectory = "chocopy/pa3/";

    // protected void initHelperFunctions() {
    //     backend.defineSym("print_string", PRINT_STRING_ECALL);


    //     FuncInfo boxPrimitiveFunc = makeFuncInfo("box_primitive", 0, Type.NONE_TYPE,
    //                          globalSymbols, null, this::emitStdFunc);
    //     boxPrimitiveFunc.addParam(makeStackVarInfo("tag", Type.INT_TYPE, null, boxPrimitiveFunc));
    //     boxPrimitiveFunc.addParam(makeStackVarInfo("size", Type.INT_TYPE, null, boxPrimitiveFunc));
    //     boxPrimitiveFunc.addParam(makeStackVarInfo("dispatchTableAddress", Type.OBJECT_TYPE, null, boxPrimitiveFunc));
    //     boxPrimitiveFunc.addParam(makeStackVarInfo("attributes", Type.OBJECT_TYPE, null, boxPrimitiveFunc));
    //     functions.add(boxPrimitiveFunc);
    //     globalSymbols.put(boxPrimitiveFunc.getBaseName(), boxPrimitiveFunc);
    // }

    /** Operation on None. */
    private final Label errorNone = new Label("error.None");
    /** Division by zero. */
    private final Label errorDiv = new Label("error.Div");
    /** Index out of bounds. */
    private final Label errorOob = new Label("error.OOB");

    /**
     * Emits the top level of the program.
     *
     * This method is invoked exactly once, and is surrounded
     * by some boilerplate code that: (1) initializes the heap
     * before the top-level begins and (2) exits after the top-level
     * ends.
     *
     * You only need to generate code for statements.
     *
     * @param statements top level statements
     */
    protected void emitTopLevel(List<Stmt> statements) {
        StmtAnalyzer stmtAnalyzer = new StmtAnalyzer(null);
        backend.emitADDI(SP, SP, -2 * backend.getWordSize(),
                         "Saved FP and saved RA (unused at top level).");
        backend.emitSW(ZERO, SP, 0, "Top saved FP is 0.");
        backend.emitSW(ZERO, SP, 4, "Top saved RA is 0.");
        backend.emitADDI(FP, SP, 2 * backend.getWordSize(),
                         "Set FP to previous SP.");

        for (Stmt stmt : statements) {
            stmt.dispatch(stmtAnalyzer);
        }
        backend.emitLI(A0, EXIT_ECALL, "Code for ecall: exit");
        backend.emitEcall(null);
    }

    /**
     * Emits the code for a function described by FUNCINFO.
     *
     * This method is invoked once per function and method definition.
     * At the code generation stage, nested functions are emitted as
     * separate functions of their own. So if function `bar` is nested within
     * function `foo`, you only emit `foo`'s code for `foo` and only emit
     * `bar`'s code for `bar`.
     */
    protected void emitUserDefinedFunction(FuncInfo funcInfo) {
        backend.emitGlobalLabel(funcInfo.getCodeLabel());
        StmtAnalyzer stmtAnalyzer = new StmtAnalyzer(funcInfo);

        for (Stmt stmt : funcInfo.getStatements()) {
            stmt.dispatch(stmtAnalyzer);
        }

        backend.emitMV(A0, ZERO, "Returning None implicitly");
        backend.emitLocalLabel(stmtAnalyzer.epilogue, "Epilogue");

        // TODO, FIXME: {... reset fp etc. ...}
        // do later since its more complicated
        backend.emitJR(RA, "Return to caller");
    }

    /** An analyzer that encapsulates code generation for statments. */
    private class StmtAnalyzer extends AbstractNodeAnalyzer<Void> {
        /*
         * The symbol table has all the info you need to determine
         * what a given identifier 'x' in the current scope is. You can
         * use it as follows:
         *   SymbolInfo x = sym.get("x");
         *
         * A SymbolInfo can be one the following:
         * - ClassInfo: a descriptor for classes
         * - FuncInfo: a descriptor for functions/methods
         * - AttrInfo: a descriptor for attributes
         * - GlobalVarInfo: a descriptor for global variables
         * - StackVarInfo: a descriptor for variables allocated on the stack,
         *      such as locals and parameters
         *
         * Since the input program is assumed to be semantically
         * valid and well-typed at this stage, you can always assume that
         * the symbol table contains valid information. For example, in
         * an expression `foo()` you KNOW that sym.get("foo") will either be
         * a FuncInfo or ClassInfo, but not any of the other infos
         * and never null.
         *
         * The symbol table in funcInfo has already been populated in
         * the base class: CodeGenBase. You do not need to add anything to
         * the symbol table. Simply query it with an identifier name to
         * get a descriptor for a function, class, variable, etc.
         *
         * The symbol table also maps nonlocal and global vars, so you
         * only need to lookup one symbol table and it will fetch the
         * appropriate info for the var that is currently in scope.
         */

        /** Symbol table for my statements. */
        private SymbolTable<SymbolInfo> sym;

        /** Label of code that exits from procedure. */
        protected Label epilogue;

        /** The descriptor for the current function, or null at the top
         *  level. */
        private FuncInfo funcInfo;

        /** An analyzer for the function described by FUNCINFO0, which is null
         *  for the top level. */
        StmtAnalyzer(FuncInfo funcInfo0) {
            funcInfo = funcInfo0;
            if (funcInfo == null) {
                sym = globalSymbols;
            } else {
                sym = funcInfo.getSymbolTable();
            }
            epilogue = generateLocalLabel();
        }

        // RD = destination register 
        // RS = source register 
        // emitINSTR(rd, rs, "comment");

        // TODO FIXME: Example of statement.
        @Override
        public Void analyze(ReturnStmt stmt) {
            // TODO FIXME: Here, we emit an instruction that does nothing. Clearly,
            // this is wrong, and you'll have to fix it.
            // This is here just to demonstrate how to emit a
            // RISC-V instruction.
            backend.emitMV(ZERO, ZERO, "No-op");
            return null;
        }

        @Override
        public Void analyze(AssignStmt stmt) {
            // TODO FIXME: Here, we emit an instruction that does nothing. Clearly,
            // this is wrong, and you'll have to fix it.
            // This is here just to demonstrate how to emit a
            // RISC-V instruction.
            backend.emitMV(ZERO, ZERO, "No-op");
            return null;
        }

        @Override
        public Void analyze(IfStmt stmt) {
            // TODO FIXME: Here, we emit an instruction that does nothing. Clearly,
            // this is wrong, and you'll have to fix it.
            // This is here just to demonstrate how to emit a
            // RISC-V instruction.
            backend.emitMV(ZERO, ZERO, "No-op");
            return null;
        }

        @Override
        public Void analyze(ExprStmt stmt) {
            // TODO FIXME: Here, we emit an instruction that does nothing. Clearly,
            // this is wrong, and you'll have to fix it.
            // This is here just to demonstrate how to emit a
            // RISC-V instruction.
            ExprAnalyzer exprAnalyzer = new ExprAnalyzer();
            Expr e = stmt.expr;
            e.dispatch(exprAnalyzer);
            return null;
        }

        @Override
        public Void analyze(ForStmt stmt) {
            // TODO FIXME: Here, we emit an instruction that does nothing. Clearly,
            // this is wrong, and you'll have to fix it.
            // This is here just to demonstrate how to emit a
            // RISC-V instruction.
            backend.emitMV(ZERO, ZERO, "No-op");
            return null;
        }

        @Override
        public Void analyze(WhileStmt stmt) {
            // TODO FIXME: Here, we emit an instruction that does nothing. Clearly,
            // this is wrong, and you'll have to fix it.
            // This is here just to demonstrate how to emit a
            // RISC-V instruction.
            backend.emitMV(ZERO, ZERO, "No-op");
            return null;
        }

        // TODO FIXME: More, of course.

        

        private class ExprAnalyzer extends AbstractNodeAnalyzer<Label> {
            // Stores the results of every Expr analyze in T0 

            // Add and remove the highest value as needed 
            // Used when parsing lists of Exprs like in CallExpr
            // ArrayList<Integer> savedStacks = new ArrayList<>();

            protected final int wordSize = backend.getWordSize();
            ArrayList<Register> tempRegisters = new ArrayList<>(Arrays.asList(T0, T1, T2, T3, T4, T5, T6, A0, A1, A2, A3, A4, A5, A6, A7));

            List<String> mathSymbols = Arrays.asList("*", "+", "-", "/", "//", "^", "&", "|", "**", ">>", ">>>", "<<");
            List<String> logicSymbols = Arrays.asList("and", "or", "is");

            public Register getUnusedRegister(ArrayList<Register> usedRegisters) {
                for (int i = 0; i < tempRegisters.size(); i += 1) {
                    Register curr = tempRegisters.get(i);
                    if (!usedRegisters.contains(curr)) {
                        return curr;
                    }
                }
                return null;
            }

            /** Helper that stores caller-saved registers on the stack. 
             * Saved registers: 
             * - RA, 
             * - temporary (t0-t6), 
             * - function args / return values (a0-a7)
             * 
             * Saved registers (saved by caller but not implemented):
             * - FP temporaries (ft0-ft11),
             * - FP args / return values (fa0-fa7)
             * 
             * Registers that are preserved across function calls:
             * - fp (current frame pointer)
             * - sp (current stack pointer; points to top of stack)
             * - ra
             * - s1-s9
             * 
             * a0-a7 and t0-t6 are temporaries (not preserved across function calls).
             * These are saved in the listed order (fp, sp, s1-s9). 
             */
            public void saveCallerRegistersOnStack() {
                // Total registers:
                // 1 (fp) + 1 (sp) + 9 (s1-s9) = 11
                // int wordSize = backend.getWordSize();
                backend.emitADDI(SP, SP, -11 * wordSize, "Decrement SP to save caller-saved registers on stack.");
                backend.emitSW(FP, SP, 0 * wordSize, "Save FP");
                backend.emitSW(SP, SP, 1 * wordSize, "Save SP");
                // backend.emitSW(RA, SP, 2 * wordSize, "Save RA");
                backend.emitSW(S1, SP, 2 * wordSize, "Save S1");
                backend.emitSW(S2, SP, 3 * wordSize, "Save S2");
                backend.emitSW(S3, SP, 4 * wordSize, "Save S3");
                backend.emitSW(S4, SP, 5 * wordSize, "Save S4");
                backend.emitSW(S5, SP, 6 * wordSize, "Save S5");
                backend.emitSW(S6, SP, 7 * wordSize, "Save S6");
                backend.emitSW(S7, SP, 8 * wordSize, "Save S7");
                backend.emitSW(S8, SP, 9 * wordSize, "Save S8");
                backend.emitSW(S9, SP, 10 * wordSize, "Save S9");
                backend.emitADDI(FP, SP, 11 * wordSize,
                         "Set FP to previous SP."); // might not use this? idk
            }
            
            /** Increments SP after function call and restores argument registers. 
             * Saved registers to be restored: 
             * - RA, 
             * - temporary (t0-t6), 
             * - function args / return values (a0-a7)
             * 
             * Saved registers (saved by caller but not implemented):
             * - FP temporaries (ft0-ft11),
             * - FP args / return values (fa0-fa7)
             * 
             * Registers that are preserved across function calls:
             * - fp (current frame pointer)
             * - sp (current stack pointer; points to top of stack)
             * - s1-s9
             * 
             * a0-a7 and t0-t6 are temporaries (not preserved across function calls).
             * These are saved in the listed order (fp, sp, s1-s9). 
             */
            public void restoreCallerSavedRegistersOnStack() {
                // returns the previous stack
                // int size = savedStacks.remove(savedStacks.size() - 1);
                // int wordSize = backend.getWordSize();
                backend.emitLW(FP, SP, 0 * wordSize, "Restore FP");

                backend.emitLW(SP, SP, 1 * wordSize, "Restore SP");
                // backend.emitLW(RA, SP, 2 * wordSize, "Restore RA");
                backend.emitLW(S1, SP, 2 * wordSize, "Restore S1");
                backend.emitLW(S2, SP, 3 * wordSize, "Restore S2");
                backend.emitLW(S3, SP, 4 * wordSize, "Restore S3");
                backend.emitLW(S4, SP, 5 * wordSize, "Restore S4");
                backend.emitLW(S5, SP, 6 * wordSize, "Restore S5");
                backend.emitLW(S6, SP, 7 * wordSize, "Restore S6");

                backend.emitLW(S7, SP, 8 * wordSize, "Restore S7");
                backend.emitLW(S8, SP, 9 * wordSize, "Restore S8");
                backend.emitLW(S9, SP, 10 * wordSize, "Restore S9");

                backend.emitADDI(SP, SP, 11 * wordSize,"Restore stack pointer.");
                // compare sp and fp 
            }

            /** Pushes args into A0-A7 for CallExpr, MethodCallExpr, etc. */
            public void pushArgsToStack(List<Expr> args) {
                // int wordSize = backend.getWordSize();
                int totalArgs = args.size();
                backend.emitADDI(SP, SP, -(totalArgs) * wordSize,"Make space for function arguments.");
                for (int i = totalArgs - 1; i >= 0; i -= 1) {
                    Expr curr = args.get(i);
                    Label l = curr.dispatch(this);
                    backend.emitSW(A0, SP, i * wordSize, "Save argument number [" + i + "] on stack.");
                }
            }

            /** Increases SP pointer to remove arguments from stack. */
            public void removeArgsFromStack(int totalArgs) {
                // int wordSize = backend.getWordSize();
                backend.emitADDI(SP, SP, totalArgs * wordSize,"Removes function arguments from stack.");
            }

            public void setPrologue(List<Expr> args) {
                saveCallerRegistersOnStack(); // saves FP, SP, S1-S9 on stack
                pushArgsToStack(args); // move function arguments into A0-A9
            }

            public void setFuncCall(FuncInfo func, String funcName) {
                backend.emitJAL(func.getCodeLabel(), "Invoke function with emitJAL: " + funcName + " with label name [" + func.getFuncName() + "]");
            }

            public void setEpilogue(FuncInfo func, List<Expr> args, boolean hasReturn) {
                if (hasReturn) {
                    backend.emitMV(T0, A0, "Move the return value from [" + func.getCodeLabel() + "] from A0 into T0");
                }
                removeArgsFromStack(args.size());
                restoreCallerSavedRegistersOnStack(); // Restores A0-A7 from stack
            }

            /** Stores a Chocopy Boolean object in T0 and the associated dispatch table label in T1. 
             * Bool tag: 2
             * Slots:
             * 1) Tag (0)
             * 2) Size in words (1)
             * 3) Address of dispatch table in memory (2)
             * 4+) Attributes (3+)
            */
            public void setBoolBox(boolean val) {
                ClassInfo curr = boolClass;
                Label dispatchTableLabel = curr.getDispatchTableLabel();
                Label l = constants.getBoolConstant(val);
                int tag = 2;
                boxPrimitive(tag, 8, dispatchTableLabel, Arrays.asList(new Boolean(val))); // size of bool not processed in box_primitive.s; set to 0 for error checking if necessary
            }

            /** Stores a Chocopy Integer object in T0 and the associated dispatch table label in T1. 
             * Slots:
             * 1) Tag (0)
             * 2) Size in words (1)
             * 3) Address of dispatch table in memory (2)
             * 4+) Attributes (3)
            */
            public void setIntBox(int val) {
                ClassInfo curr = intClass;
                Label dispatchTableLabel = curr.getDispatchTableLabel();
                int tag = 1;
                // System.out.println("got to intbox");
                boxPrimitive(tag, 8, dispatchTableLabel, Arrays.asList(new Integer(val)));
                Label l = constants.getIntConstant(val);
            }

            /** Stores a Chocopy String object in T0 and the associated dispatch table label in T1. 
             * Slots:
             * 1) Tag (0)
             * 2) Size in words (1)
             * 3) Address of dispatch table in memory (2)
             * 4+) Attributes (3+)
             * 
             * Strings have two attributes: __len__ and __str__
            */
            public void setStrBox(String val) {
                ClassInfo curr = strClass;
                Label dispatchTableLabel = curr.getDispatchTableLabel();
                Label contentLabel = constants.getStrConstant(val);
                int tag = 3;
                byte[] originalByteStream = val.getBytes();
                int originalByteLength = originalByteStream.length;
                byte[] paddedByteStream = new byte[originalByteLength + (4 - (originalByteLength % 4))];
                for (int padCounter = 0; padCounter < paddedByteStream.length; padCounter += 1) {
                    if (padCounter < originalByteLength) {
                        paddedByteStream[padCounter] = originalByteStream[padCounter];
                    }
                    else {
                        paddedByteStream[padCounter] = '\0';
                    }
                }
                int totalWords = (int)Math.ceil(4 + (val.toString().length()/4));
                boxPrimitive(tag, totalWords, dispatchTableLabel, Arrays.asList(new Integer(val.length()), paddedByteStream));
            }

            /** Stores a Chocopy List object in T0 and the associated dispatch table label in T1. 
             * Slots:
             * 1) Tag
             * 2) Size in words
             * 3) Address of dispatch table in memory
             * 4+) Attributes
            */
            public void setListBox(List<Expr> val) {
                
            }


            public void boxPrimitive(int tag, int size, Label dispatchTableAddress, List<Object> attributes) {
                // boxPrimitive(int tag, int size, dispatchTableAddress, <T> value)
                // System.out.println("got to inside box primitive");
                // bool, int, str have already the dispatch table address in the prototype label
                // int wordSize = backend.getWordSize();
                int totalInputs = -1;
                ClassInfo curr = null;
                switch(tag) {
                    case 1:
                        curr = intClass;
                        totalInputs = 4; // tag, size, dispatch table, value
                        break;
                    case 2:
                        curr = boolClass;
                        totalInputs = 4; // tag, size, dispatch table, value
                        break;
                    case 3:
                        curr = strClass;
                        totalInputs = 5; // tag, size, dispatch table, __len__, __str__
                        break;
                    default:
                        System.out.println("Tag [" + tag + "] not yet implemented");
                        return;
                }

                backend.emitADDI(SP, SP, -1 * totalInputs * wordSize, "Make space for args to box_primitive on stack.");

                // // load the prototype label
                // backend.emitLA(T0, prototypeLabel, "Load prototype label into T0.");
                // backend.emitSW(T0, SP, 0 * wordSize, "Save prototype label on stack.");
                // enter tag
                backend.emitLI(T0, tag, "Set T0 to tag [" + tag + "].");
                backend.emitSW(T0, SP, 0 * wordSize, "Save tag on stack.");
                // enter object size
                backend.emitLI(T0, size, "Set T0 to size [" + size + "].");
                backend.emitSW(T0, SP, 1 * wordSize, "Save object size on stack.");
                // enter dispatch table
                backend.emitLA(T0, dispatchTableAddress, "Load dispatch table label into T0.");
                backend.emitSW(T0, SP, 2 * wordSize, "Save object dispatch table address on stack.");
                
                 // handle multiple attributes
                 for (int i = 0; i < attributes.size(); i += 1) {
                    switch(tag) {
                        case 1: // int
                            if (i == 0) {
                                int intVal = (Integer)attributes.get(i);
                                backend.emitLI(T0, intVal, "Set T0 to int val [" + intVal + "].");
                                backend.emitSW(T0, SP, 3 * wordSize, "Save attribute on stack.");
                            }
                            else {
                                System.out.println("Invalid number of attributes.");
                            }
                            break;
                        case 2: // bool 
                            if (i == 0) {
                                boolean boolVal = (Boolean)attributes.get(i);
                                if (boolVal) {
                                    backend.emitLI(T0, 1, "Set T0 to 1 (true).");
                                    backend.emitSW(T0, SP, 3 * wordSize, "Save attribute on stack.");
                                }
                                else {
                                    backend.emitSW(ZERO, SP, 3 * wordSize, "Save attribute on stack.");
                                }
                            }
                            else {
                                System.out.println("Invalid number of attributes.");
                            }
                            break;
                        case 3: // string
                            if (i == 0) {
                                int intVal = (Integer)attributes.get(i);
                                backend.emitLI(T0, 1, "Set T0 to string length [" + intVal + "].");
                                backend.emitSW(T0, SP, 3 * wordSize, "Store string length on stack.");
                            }
                            else if (i == 1) {
                                byte[] paddedByteStream = (byte[])attributes.get(i);
                                for (int index = 0, wordCounter = 0; index < paddedByteStream.length; index += 4) {
                                    byte[] currWord_byte = new byte[]{paddedByteStream[index + 3], paddedByteStream[index + 2], paddedByteStream[index + 1], paddedByteStream[index]};
                                    int currWord_int = ByteBuffer.wrap(currWord_byte).getInt();
                                    backend.emitLI(T0, currWord_int, "Set T0 to the current word number [" + (wordCounter + 1) + "].");
                                    backend.emitSW(T0, SP, (4 + wordCounter) * wordSize, "Set next word for __str__. Save on stack.");
                                    wordCounter += 1;
                                }
                            }
                            break;
                        default:
                            System.out.println("Incorrect tag passed.");
                    }
                }
                
                backend.emitJAL(boxPrimitiveLabel, "Call box_primitive routine");
                // boxPrimitive(int tag, int size, dispatchTableAddress, attributes ... )

                // backend.emitADDI(SP, SP, totalInputs * wordSize, "Restore stack."); // values saved on stack

                // backend.emitLI(T1, tag, "Load tag number in T1");
            }

            /** Boxes the provided primitive and stores the pointer in T0 and the tag number in T1.
             * Arguments provided in registers.
             * Tags:
             * 0) reserved
             * 1) int
             * 2) bool
             * 3) str
             * -1) [T]
             * 
             * Slots:
             * 1) Tag (0)
             * 2) Size in words (1)
             * 3) Address of dispatch table in memory (2)
             * 4+) Attributes (3+)
             * 
             * Int and bool have 1 attribute.
             * Str has 2 attributes (__len__, __str__ [value])
             * sizeOfAttributes is the total # of words and will be used as a register.
             */
            public void boxPrimitive(Register tag, Register size, Register dispatchTableAddress, Register sizeOfAttributes, Register attributes) {
                ArrayList<Register> usedRegisters = new ArrayList<>(Arrays.asList(tag, size, dispatchTableAddress, sizeOfAttributes, attributes));
                Register tempReg1 = getUnusedRegister(usedRegisters);
                usedRegisters.add(tempReg1);
                Register tempReg2 = getUnusedRegister(usedRegisters);
                usedRegisters.add(tempReg2);
                
                backend.emitLI(tempReg1, 3, "Load 3 into temp register 1 (All objects have: tag, size, dispatch table address).");
                backend.emitADD(tempReg1, tempReg1, sizeOfAttributes, "Set temp reg 1 to be the total words needed to store the object.");
                backend.emitLI(tempReg2, -1, "Load -1 into temp register 2.");
                backend.emitMUL(tempReg1, tempReg1, tempReg2, "Set temp reg 1 to what needs to be added to SP to make room for the obj.");
                backend.emitADD(SP, SP, tempReg1, "Make space for args to box_primitive on stack.");
                // enter tag
                backend.emitSW(tag, SP, 0 * wordSize, "Save tag on stack.");
                // enter object size
                backend.emitSW(size, SP, 1 * wordSize, "Save object size on stack.");
                // enter dispatch table
                backend.emitSW(dispatchTableAddress, SP, 2 * wordSize, "Save object dispatch table address on stack.");
                // handle multiple attributes
                // iterate until total number of words needed is decreased to 0
                backend.emitADDI(SP, SP, -3 * wordSize, "Prepare to call transfer_contents");
                // Args: transfer_contents(Register destination, Register source, int counter)
                // Destination = tempReg1, source = attributes, counter = sizeOfAttributes
                // put args on in backwards order
                // already boxed strings will have a prepadded length already
                backend.emitSW(sizeOfAttributes, SP, 0, "counter = sizeOfAttributes");
                backend.emitSW(attributes, SP, 1 * wordSize, "source = attributes");
                backend.emitSW(tempReg1, SP, 2 * wordSize, "destination = tempReg1"); 
                backend.emitJAL(transferContentsLabel, "Call transfer_contents routine");
                backend.emitADDI(SP, SP, 3 * wordSize, "Restore stack");
                backend.emitSW(tempReg1, SP, 3 * wordSize, "Save attributes on stack.");
                backend.emitJAL(boxPrimitiveLabel, "Call box_primitive routine");
            }

            /** Stores the tag of the object (index 0) located in SOURCE into RD. */
            public void getObjectTag(Register rd, Register source) {
                backend.emitLW(rd, source, 0, "Load object tag (index 0) into [" + rd.toString() + "].");
            }

            /** Stores the size of the object sizes (index 1) located in SOURCE into RD. */
            public void getObjectSize(Register rd, Register source) {
                backend.emitLW(rd, source, 1 * backend.getWordSize(), "Load object size (index 1) into [" + rd.toString() + "].");
            }

            /** Stores the dispatch table (index 2) of the object located in SOURCE into RD. */
            public void getObjectDispatchTable(Register rd, Register source) {
                backend.emitLW(rd, source, 2 * backend.getWordSize(), "Load object dispatch table (index 2) into [" + rd.toString() + "].");
            }

            /** Stores the sum of the object sizes (index 1) located in SOURCE1 and SOURCE2 into RD. */
            public void sumObjectSize(Register rd, Register source1, Register source2) {
                backend.emitLW(rd, source1, 1 * backend.getWordSize(), "Load source1 size into rd.");
                backend.emitADDI(SP, SP, -1 * backend.getWordSize(), "Make room to save T0 on the stack."); 
                backend.emitSW(T0, SP, 0, "Save T0 on the stack.");
                backend.emitLW(T0, source2, 1 * backend.getWordSize(), "Load source2 size into T0.");
                backend.emitADD(rd, rd, T0, "rd = s1.size + s2.size");
                backend.emitLW(T0, SP, 0, "Restore T0 from the stack.");
                backend.emitADDI(SP, SP, 1 * backend.getWordSize(), "Make room to save T0 on the stack."); 
            }

            /** Unboxes primitive object stored in SOURCE and stores the primitive value in DEST. 
             * Uses T5 and T6 for indexing to avoid overlap with T0. This version handles strings and lists.
             * Stores the primitive value in T0 and the type tag in T1. 
             * 
             * Slots:
             * 1) Tag (0)
             * 2) Size in words (1)
             * 3) Address of dispatch table in memory (2)
             * 4+) Attributes (3+)
            */
            public void unboxPrimitive(Register valueDest, Register pointerDest, Register source) {
                backend.emitADDI(SP, SP, -1 * wordSize, "Prepare to call unbox_primitive");
                backend.emitSW(source, SP, 0, "Store pointer to object on stack.");
                backend.emitJAL(unboxPrimitiveLabel, "Call unbox_primitive");
                backend.emitMV(valueDest, A0, "Move the pointer / value to the correct register.");
                backend.emitMV(pointerDest, source, "Set " + pointerDest.toString() + " to the pointer of the object.");
                backend.emitADDI(SP, SP, 1 * wordSize, "Restore stack");
            }

            @Override
            public Label analyze(BooleanLiteral e) {
                Label l = constants.getBoolConstant(e.value);
                setBoolBox(e.value);
                return l;
            }

            @Override
            public Label analyze(StringLiteral e) {
                Label l = constants.getStrConstant(e.value);
                setStrBox(e.value);
                return l;
            }

            @Override
            public Label analyze(IntegerLiteral e) {
                Label l = constants.getIntConstant(e.value);
                setIntBox(e.value);
                return l;
            }

            @Override
            public Label analyze(NoneLiteral e) {
                Label l = constants.fromLiteral(e); // returns null as None label
                backend.emitLW(A0, l, "Expr (Literal) [" + "None" + "]");
                return l;
            }

            public void typecheck(Type type, Register reg1) {

                if (Type.BOOL_TYPE.equals(type)) {

                }
                else if (Type.INT_TYPE.equals(type)) {

                }
                else if (Type.EMPTY_TYPE.equals(type)) {

                }
                else if (Type.STR_TYPE.equals(type)) {

                }
                else if (Type.OBJECT_TYPE.equals(type)) {

                }
                else if (Type.NONE_TYPE.equals(type)) {

                }
                else {
                    backend.emitInsn("j abort", "Invalid type in expression");
                }
            }

            @Override // FIXME, add a label
            public Label analyze(BinaryExpr e) {
                Label left = e.left.dispatch(this);
                backend.emitMV(T0, A0, "Move left side to T0 for operation");
                Label right = e.right.dispatch(this);
                backend.emitMV(T1, A0, "Move right side to T1 for operation");
                
                
                System.out.println("Left and right evaluated");
                boolean intOperands = false;
                if (mathSymbols.contains(e.operator) || logicSymbols.contains(e.operator)) {
                    intOperands = true;
                    // unboxPrimitive(T2); // unboxed into t0, t1; move into t5 for now since the helper uses T0-T4
                    backend.emitMV(T5, T0, "Move unboxed primitive into T5");
                    // unboxPrimitive(T3);
                    backend.emitMV(T3, T0, "Move unboxed primitive into T3"); // move back into T3 for following operations
                    backend.emitMV(T2, T5, "Move unboxed T2 back from T5 for following operations");
                }
                switch(e.operator) {
                    case "*":
                        System.out.println("mul");
                        backend.emitMUL(T0, T2, T3, "Multiply; T0 = T2 * T3");
                        break;
                    case "+":
                        System.out.println("add");
                        backend.emitADD(T0, T2, T3, "Added; T0 = T2 + T3");
                        break;
                    case "-":
                        backend.emitSUB(T0, T2, T3, "Subtract; T0 = T2 - T3");
                        break;
                    case "/":
                        backend.emitDIV(T0, T2, T3, "Divide; T0 = T2 / T3");
                        // todo: add divide by 0 flag here
                        break;
                    case "//":
                        backend.emitREM(T0, T2, T3, "Remainder; T0 = T2 // T3");
                        break;
                    case "^":
                        backend.emitXOR(T0, T2, T3, "XOR; T0 = T2 ^ T3");
                        break;
                    case "&":
                    case "and":
                        backend.emitAND(T0, T2, T3, "AND; T0 = T2 & T3");
                        break;
                    case "**": // todo
                        // 2 ** 3 = 2 ^ 3 = 2 * 2 * 2
                        // int power = right.
                        // backend.emitMUL(T0, A0, A1, "Multiply; T0 = T2 * A1");
                        backend.emitMV(ZERO, ZERO, "No-op; ** not implemented");
                        break;
                    case "or":
                    case "|":
                        backend.emitOR(T0, T2, T3, "OR; T0 = T2 | T3");
                        break;
                    case "<<":
                        backend.emitSLL(T0, T2, T3, "SLL; T0 = T2 << T3");
                        break;
                    case ">>":
                        backend.emitSRA(T0, T2, T3, "SLL; T0 = T2 >> T3");
                        break;
                    case ">>>":
                        backend.emitSRL(T0, T2, T3, "OR; T0 = T2 >>> T3");
                        break;
                    default:
                        System.out.println("no op");
                        backend.emitMV(ZERO, ZERO, "No-op; " + e.operator + " not implemented");
                }
                backend.emitMV(A0, T0, "Move value to A0");
                // rebox output
                // if (intOperands) {
                //     boxPrimitive(nextTypeTag, , A1, SP, A0);
                // }
                // if (mathSymbols.contains(e.operator) || logicSymbols.contains(e.operator)) {
                //     boxPrimitive(nextTypeTag, HEADER_SIZE, right,  // todo: register only version
                // }
                return null;
            }

            @Override
            public Label analyze(CallExpr e) {
                // TODO FIXME: Here, we emit an instruction that does nothing.
                // ints and booleans need to be boxed when they are callexpr arguments
                // might not return a literal but instead nothing or a label; just use labels
                CallExpr curr = e;
                String funcName = curr.function.name;
                FuncInfo currFunc = null;
                SymbolInfo lookupSymbol = sym.get(funcName);
                if (lookupSymbol != null && lookupSymbol instanceof FuncInfo) {
                    currFunc = (FuncInfo)lookupSymbol;
                }
                // System.out.println("Matched function is [" + ((currFunc != null) ? currFunc.getFuncName() : "N/A") + "]");
                ValueType ret = ((FuncType)(curr.function.getInferredType())).returnType;
                boolean hasReturn = !Type.NONE_TYPE.equals(ret) && ret != null; // None Type might be equal to Null
                // System.out.println("Has return [" + hasReturn + "] of type [" + ret.className() + "]");
                setPrologue(curr.args);
                setFuncCall(currFunc, funcName); // moves return value into T0
                setEpilogue(currFunc, curr.args, hasReturn);
                return null;
            }

            @Override
            public Label analyze(IfExpr e) {
                // TODO FIXME: Here, we emit an instruction that does nothing.
                backend.emitMV(ZERO, ZERO, "No-op");
                return null;
            }

            @Override
            public Label analyze(MemberExpr e) {
                // TODO FIXME: Here, we emit an instruction that does nothing.
                backend.emitMV(ZERO, ZERO, "No-op");
                return null;
            }

            @Override
            public Label analyze(MethodCallExpr e) {
                // TODO FIXME: Here, we emit an instruction that does nothing.
                backend.emitMV(ZERO, ZERO, "No-op");
                return null;
            }

            @Override
            public Label analyze(ListExpr e) {
                // TODO FIXME: Here, we emit an instruction that does nothing.
                backend.emitMV(ZERO, ZERO, "No-op");
                return null;
            }

            @Override
            public Label analyze(UnaryExpr e) {
                Label l = e.operand.dispatch(this);
                ClassValueType curr = (ClassValueType)e.getInferredType();
                if ("int".equals(curr.className())) {
                    if ("-".equals(e.operator)) {
                        backend.emitSUB(T0, ZERO, T0, "Move [" + e.operator + e.operand.toString() + "] to T0");
                        if (e.operand instanceof IntegerLiteral) { // FIXME, create correct label
                            l = constants.getIntConstant(((IntegerLiteral)e.operand).value * -1);
                        }
                    }
                    else {
                        backend.emitMV(ZERO, ZERO, "No-op; invalid UnaryExpr [" + e.toString() + "]");
                    }
                }
                else if ("bool".equals(curr.className())) {
                    if ("not".equals(e.operator)) {
                        if (constants.getBoolConstant(true).equals(l)) {
                            l = constants.getBoolConstant(false);
                            backend.emitLW(T0, l, "Set T0 to [" + e.toString() + "]" + " (false)");
                            return l;
                        }
                        else if (constants.getBoolConstant(false).equals(l)) {
                            l = constants.getBoolConstant(true);
                            backend.emitLW(T0, l, "Set T0 to [" + e.toString() + "]" + " (true)");
                            return l;
                        }
                        else {
                            backend.emitMV(ZERO, ZERO, "No-op; invalid boolean UnaryExpr [" + e.toString() + "]");
                        }
                    }
                    else {
                        backend.emitMV(ZERO, ZERO, "No-op; invalid UnaryExpr [" + e.toString() + "]");
                    }
                }
                else {
                    backend.emitMV(ZERO, ZERO, "No-op; invalid UnaryExpr [" + e.toString() + "]");
                }
                return l;
            }
        }
    }

    /**
     * Emits custom code in the CODE segment.
     *
     * This method is called after emitting the top level and the
     * function bodies for each function.
     *
     * You can use this method to emit anything you want outside of the
     * top level or functions, e.g. custom routines that you may want to
     * call from within your code to do common tasks. This is not strictly
     * needed. You might not modify this at all and still complete
     * the assignment.
     *
     * To start you off, here is an implementation of three routines that
     * will be commonly needed from within the code you will generate
     * for statements.
     *
     * The routines are error handlers for operations on None, index out
     * of bounds, and division by zero. They never return to their caller.
     * Just jump to one of these routines to throw an error and
     * exit the program. For example, to throw an OOB error:
     *   backend.emitJ(errorOob, "Go to out-of-bounds error and abort");
     *
     */
    protected void emitCustomCode() {
        emitErrorFunc(errorNone, "Operation on None");
        emitErrorFunc(errorDiv, "Division by zero");
        emitErrorFunc(errorOob, "Index out of bounds");
    }

    /** Emit an error routine labeled ERRLABEL that aborts with message MSG. */
    private void emitErrorFunc(Label errLabel, String msg) {
        backend.emitGlobalLabel(errLabel);
        backend.emitLI(A0, ERROR_NONE, "Exit code for: " + msg);
        backend.emitLA(A1, constants.getStrConstant(msg),
                       "Load error message as str");
        backend.emitADDI(A1, A1, getAttrOffset(strClass, "__str__"),
                         "Load address of attribute __str__");
        backend.emitJ(abortLabel, "Abort");
    }
}
