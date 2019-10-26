The autocomplete feature is comprised of the find() function of the Trie and the suffixes() function of TrieNode.
The time efficiency of the find() function is O(n) where n stands for the linear / depth first search for a character
 in the children dictionary from each preceding node. 
 The time efficiency of the suffixes() function is O(n*m) where n stands for the linear search across the children
 dictionary for each node and where m stands for each node whose children dictionary is being checked to uncover 
 all possible suffixes after the prefix.
The space efficiency for the find() function is O(1) given that only pointers were used in the function. 
The space efficiency for the suffixes() is O(n*m), where n is for each character and m is for each word 
yielded as a list of words. 