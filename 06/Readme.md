# EDA 06

#### CST53 HeQi 2015011299

## Complete

Input: complete.in

line 1: Integer n, m. The number of states and type of inputs.

line 2~n+1: Each line contains m integers Tij, describes the next state when state i receives an input j.

line n+2~2\*n+1: Each line contains m integers Oij, describes the output when state i receives an input j.

Output: complete.out

line 1: Integer k, the number of minimized states.

line 2: N integers Si, describes the new state which state i belongs to.

## Incomplete

Input: incomplete.in

line 1: Integer n, m. The number of states and type of inputs.

line 2~n+1: Each line contains m integers Tij, describes the next state when state i receives an input j. -1 indicates such input won't exist.

line n+2~2\*n+1: Each line contains m integers Oij, describes the output when state i receives an input j. -1 indicates arbitary (don't care) outputs.

Output: incomplete.out

Same as complete.out.
