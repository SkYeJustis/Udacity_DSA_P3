This function takes in a list. The operations performed to yield two maximum sums are 
(1) a mergesort to sort the list through the mergesort() and merge() functions and 
(2) logic to go through the sorted list to build the maximum sums through the latter part of the
rearrange_digits() functions.
The time efficiency is O(n*log(n)), combining the use of (1) mergesort at O(log(n)) and (2) the linear time O(n) building of the two
maximum sums.
The space efficiency is O(n), given the recursive stack storage of the mergesort + merge function calls 
and the storage of the input when determining the maximum sums, via the first_num and second_num variables.