This function takes in a number and iterates through potential sqrt solutions in a binary
search manner using the high and low pointers. If the squared result of the mid numbers
match, the exact number is returned after the else. The default return of high will return
the floor squared root. 
The time efficiency is O(log(n)) given the binary search approach taken.
The space efficiency is O(1) as regardless of the input value, 
only the pointers are used to hold values.