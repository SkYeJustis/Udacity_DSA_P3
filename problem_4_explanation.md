This function takes in a list. Each item on the list is examined and its values switched to 0 or 2,
depending on the last seen position of a 0 or 2. One pass of the list is needed making this a linear, single traversal
operation. 
The time efficiency is O(n) as the list is traversed through linearly
The space efficiency is O(1), given the pointers used to keep track of the positions of the list being traversed via
current_pos, current_pos_0, and current_pos_2.