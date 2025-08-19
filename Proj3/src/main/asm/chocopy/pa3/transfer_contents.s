# transfer_contents(Register destination, Register source, int counter)
# counter is the total # of words needed to be moved from destination to source
    lw a0, 0(sp)                             # Load the destination pointer into A0
    mv a1, a0                                # Copy contents to A1; A1 and A2 will be used for incrementing the pointers
    lw a2, 4(sp)                             # Load the source pointer into A2
    lw a3, 8(sp)                             # Load counter into A3
    j move_contents_loop
move_contents_loop:
    beq zero, a3, end_move_contents_loop
    lw a4, a2, 0                            # Load the current word into A4
    # MEMORY[RS1 + IMM]:4 = RS2 for rs2, rs1, imm
    sw a4, a1, 0                            # Store the word at the current index within the destination pointer; contained within A1
    addi a1, a1, 4                          # Increment destination pointer 
    addi a2, a2, 4                          # Increment destination pointer 
    addi a3, a3, -1                         # Decrement word counter
end_move_contents_loop:
    jr ra                                   # Pointer to beginning of transferred contents is stored in A0

