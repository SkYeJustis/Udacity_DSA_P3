The Router's lookup feature is comprised of the find() function of the RouteTrie object.
The time efficiency of the find() function is O(n*m) where n stands for the linear search across the path_paths list 
 for path section separated by / and where m stands for each subsequent path after the preceeding path in the children
 dictionary where each item being checked see if it matches the lookup path.
The space efficiency for the find() function is O(n) given that the size of the path_paths list linearly 
varies based on the size of input path being looked up.