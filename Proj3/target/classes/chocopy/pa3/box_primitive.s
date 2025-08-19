# Function boxPrimitive
# Boxes the following primitives:
# 0) (reserved)
# 1) int
# 2) bool
# 3) str
# -1) <T> (user defined)
# 
# - list (not implemented)
# boxPrimitive(int tag, int size, dispatchTableAddress, attributes ... )
# output: pointer to primitive object in A0, tag in A1
# We do not save/restore fp/ra for this function
# because we know that it does not use the stack or does not
# call other functions.
  lw a0, 0(sp)                             # Load tag arg into A0
  mv a1, a0                                # Load tag into A1
  li t1, 1                                 # Load int tag
  beq a0, t1, box_int                      # Go to box_int
  li t1, 2                                 # Load bool tag
  beq a0, t1, box_bool                     # Go to box_bool
  li t1, 3                                 # Load str tag
  beq a0, t1, box_str                      # Go to box_str
  li t1, -1                                # Load list(?) tag
  beq a0, t1, box_list                     # Go to box_list
  # j box_error
  j abort
box_int:
  la a0, $int$prototype                    # Load int prototype
  li t0, 1                                 # Load int tag
  sw t0, 0(a0)                             # Save int tag
  lw t0, 4(sp)                             # Set T0 to the primitive size
  sw t0, 4(a0)                             # Store primitive from T0 in 8(a0)
  lw t0, 8(sp)                             # Set T0 to the dispatch table address
  sw t0, 8(a0)                             # Store dispatch table from T0 in 8(a0)
  lw t0, 12(sp)                            # Set T0 to primitive value 
  sw t0, 12(a0)                            # Store primitive value from T0 in 12(a0)
  jr ra

box_bool:
  la a0, $bool$prototype                    # Load bool prototype
  li t0, 2                                 # Load bool tag
  sw t0, 0(a0)                             # Save bool tag
  lw t0, 4(sp)                             # Set T0 to the primitive size
  sw t0, 4(a0)                             # Store primitive from T0 in 8(a0)
  lw t0, 8(sp)                             # Set T0 to the dispatch table address
  sw t0, 8(a0)                             # Store dispatch table from T0 in 8(a0)
  lw t0, 12(sp)                            # Set T0 to primitive value 
  sw t0, 12(a0)                            # Store primitive value from T0 in 12(a0)
  jr ra

box_str: # receives the padded values
  la a0, $str$prototype                    # Load str prototype
  li t0, 3                                 # Load str tag
  sw t0, 0(a0)                             # Save str tag
  lw t0, 4(sp)                             # Set T0 to the primitive size
  mv t1, t0                                # Set T1 to the number of words to later value checking
  sw t0, 4(a0)                             # Store primitive from T0 in 8(a0)
  lw t0, 8(sp)                             # Set T0 to the dispatch table address
  sw t0, 8(a0)                             # Store dispatch table from T0 in 8(a0)
  lw t0, 12(sp)                            # Set T0 to the __len__ attribute
  sw t0, 12(a0)                            # Store __len__ attribute from T0 in 8(a0)
  mv t2, a0                                # Set T2 to be the current address of the prototype
  addi t2, t2, 16                          # Increment T2 to the location of the value field
  mv t3, sp                                # Set T3 to be the current address of the arguments on the stack
  addi t3, t3, 16                          # Increment T3 to the location of the value field on the stack
  j str_val_loop
str_val_loop:
  lw t4, 0(t3)                             # Set T4 to be the value of the current word; load word from args
  sw t4, 0(t2)                             # Store in memory the value of the current word to the pointer of the current address in the prototype (T2)
  addi t3, t3, 4                           # T3 += 4; increment pointer to address of value field on stack
  addi t2, t2, 4                           # T2 += 4; increment pointer to address of value field in the prototype
  addi t1, t1, -1                          # T1 -= 1; decrement indexing variable T1
  beq t1, zero, end_str_val_loop           # Break to end if no more words to read (t1 = 0)
  j str_val_loop                           # Begin next iteration of loop
end_str_val_loop: 
  jr ra                                    # Return to caller

# todo: check that the function works and the jumps and returns work correctly

box_list:
  mv zero, zero                            # list primitive not yet implemented; FIXME
  jr ra

# box_error:
#   li a0, @error_arg                                   # Exit code for: Invalid argument
#   la a1, STRING["Invalid argument / type tag"]        # Load error message as str
#   addi a1, a1, @.__str__                              # Load address of attribute __str__
#   j abort                                             # Abort
