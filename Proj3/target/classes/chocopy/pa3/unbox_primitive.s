# unbox_primitive(Register pointer_to_boxed_object)
# Destroys original boxed object? 
# >> No. It is destroyed at the end of any function
# Returns:
# >> A0: pointer to value if string/list; actual value if int or bool
# Slots:
# 1) Tag (0)
# 2) Size in words (1)
# 3) Address of dispatch table in memory (2)
# 4+) Attributes (3+)
    lw a0, 0(sp)                # Load the pointer to the boxed object
    lw a1, 4(a0)                # Load object tag into a1
    li a2, 3                    # Load str tag
    beq a1, a2, unbox_str       # Unbox string
    bge a1, a2, unbox_other     # Unbox list or user object
    lw a1, 12(a0)               # A1 = value
    mv a0, a1                   # A0 = value
    jr ra

unbox_str:
    lw a1, 16(a0)               # A1 = pointer to __str__ attribute
    mv a0, a1                   # A0 = pointer to __str__ attribute
    jr ra

unbox_other:
    j abort                     # list / user object unboxing not defined