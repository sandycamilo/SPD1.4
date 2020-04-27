#################################################################
# Interview Question:
# Given a list of n numbers, find the highest pair of adjacent
# elements. That is, maximize a[i] + a[i+1] for some i.

# Variable Table:
# Variable : Value
#  0  1  2  3  4  5
# [7, 2, 5, 9, 3, 4]
# i = 5 + 9 = 14
# the_list[i] = 14
# highest_pair = 9
# continue, continue, return highest_pair

def find_highest_pair(the_list):
  # Set it to lowest possible number
  highest_pair = float('-inf')
  
  # Loop over all indices in the list
  for i in range(len(the_list)):
    # For each index, see if the pair starting at index is higher
    # than highest we've seen so far
    if the_list[i] + the_list[i+1] > highest_pair:
      highest_pair = the_list[i] + the_list[i+1]
      
  return highest_pair
  

actual = find_highest_pair([7, 2, 5, 9, 3, 4])
expected = 14

print(f"Testing on {[7, 2, 5, 9, 3, 4]}")