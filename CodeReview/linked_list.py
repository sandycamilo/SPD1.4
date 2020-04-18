 
# Problem:

# Find the longest substring of unique letters in a given string of n letters.

# can be checked in linear time by scanning it from left to right and keeping a map of visited characters
# Time complexity of this solution would be O(n^3)
# O(n + d) where n is length of the input string and d is number of characters in input string alphabet

letters = 200

def find_substring(string):
    n = len(string)
    cur_len = 1  # store the length of current substring
    max_len = 1  # store the result
    prev_index = 0 #store the previous index
    index = 0 

    visited = [-1] * letters # -1 is used to indicate that character has not been visited yet. 
    visited[ord(string[0])] = 0 # mark first character as visited by storing the index of first character in visited array
    for index in xrange(1, n):
        prev_index = visited[ord(string[index])]
        if prev_index == -1 or (index - cur_len > prev_index): #If the currentt character is not present in the already processed substring, then do cur_len++ 
            cur_len += 1 
        else:
            if cur_len > max_len: # If the current character is present in currently considered  NRCS, then update NRCS to start from the next character of previous instance. 
                max_len = cur_len
            cur_len = index - prev_index
        visited[ord(string[index])] = index  # update the index of current character 

    if cur_len > max_len: # Compare the length of last NRCS with max_len and update max_len if needed 
        max_len = cur_len
    return max_len

string = "ABNSLAKJDSBA"
print(f'the string is {string}')
length = find_substring(string)
print(f'length of longest substring of unique letters is {str(length)}')