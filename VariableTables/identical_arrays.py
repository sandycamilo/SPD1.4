#################################################################
# Given two arrays, determine if both arrays contain exactly the 
# same elements in the same order.

# Variable table:
# 0.  1. 2. 3    0. 1. 2. 3 
# [1, 2, 3, 4], [1, 2, 7, 4]
# Variable : Value
# i = 2
# len = 4 
# array1 [i] = 3
# array2 [i] = 7
# continue, continue,False- function ends

def arrays_identical(array1, array2):
  # If arrays are different lengths, they are not identical.
  if len(array1) != len(array2):
    return False
    
  # Loop over each element to see if the items are equal.
  for i in range(len(array1)): 
    if array1[i] != array2[i]:
      return False
    else:
      continue
  
  # If all items are equal, then arrays are identical.
  return True


actual = arrays_identical([1, 2, 3, 4], [1, 2, 7, 4])
expected = False

print(f"Testing on {[1, 2, 3, 4]}, {[1, 2, 7, 4]}")