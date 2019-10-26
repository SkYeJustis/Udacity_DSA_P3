This function takes in a target and a list. The operations performed are 
(1) finds the index in which the array is rotated and (2) searches through the array based on
the rotated index location -- both in a binary search manner using the high and low pointers. 
The time efficiency is O(log(n)) given the binary search approach 
taken to find the rotated_index and binary_search, used in the main rotated_array_search
function.
The space efficiency is O(1) given the re-use of the nums list
and only the pointers are used to hold values.