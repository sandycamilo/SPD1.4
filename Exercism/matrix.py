
# Given a string representing a matrix of numbers, return the rows and columns of that matrix.

# So given a string with embedded newlines like:

# 9 8 7
# 5 3 2
# 6 6 7
# representing this matrix:

#     1  2  3
#   |---------
# 1 | 9  8  7
# 2 | 5  3  2
# 3 | 6  6  7
# your code should be able to spit out:

# A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
# A list of the columns, reading each column top-to-bottom while moving from left-to-right.
# The rows for our example matrix:

# 9, 8, 7
# 5, 3, 2
# 6, 6, 7
# And its columns:

# 9, 5, 6
# 8, 3, 6
# 7, 2, 7

# PROBLEM SOLVING STRATEGY
# Generate reasonable test inputs 
# Understand & solve the problem - simplify if needed
# Find a pattern in your solution
# Make a plan - write pseudocode 
# Follow your plan - write real code 
# Check your work - test your code 


# input string:
# print('9 8 7\n5 3 2\n6 6 7')

# understanding the problem: 
# rows: identify len of first row by starting from the first index to the start of the next new line, then create your next row.
# columns: identify and add a new column number after each new line defined by '\'.

# pattern: 
# '\' - indicates where row begins and ends 
# counter from input 

# write pseudocode:

# rows:
# set a counter for the number of characters before \n
# check if char "\" exists in string
# while char != '\'
# return
# create a string with the numbers at every other place in the range of counter
# prepend this string to the matrix string

# columns:
# if first char, add 1 before string
# else add 1 to counter
# insert counter after \n


# print('9 8 7\n5 3 2\n6 6 7')

input = '9 8 7\n5 3 2\n6 6 7'

def rows(matrix_str):
    row_count = 0
    row_string = ''
    for char in matrix_str:
        if char == ' ':
            continue
        # row_count += 1 
        print(char,row_count)
        if char == '\n':
            break
        row_count += 1
    print(row_count)
    for i in range(1, row_count +1):
        row_string += '{} '.format(str(i))
    matrix_str = row_string + '\n' + matrix_str
    print(matrix_str)

    # def columns(matrix_str):


if __name__ == "__main__":
    rows(input)
