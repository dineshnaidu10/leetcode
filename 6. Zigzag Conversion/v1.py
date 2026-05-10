# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"

# Constraints:

#     1 <= s.length <= 1000
#     s consists of English letters (lower-case and upper-case), ',' and '.'.
#     1 <= numRows <= 1000

numRows = 2
s = 'ABCDE'

def convert(s, numRows):
    if numRows == 1:
        return s

    # Init key variables
    rows = dict()
    counter = 1
    dir = 1
    return_s = ''

    # A for loop to init same number of lists as numRows in a dictionary
    for row in range(1, numRows+1):
        rows[f'list_{row}'] = []

    # Main logic loop
    for word in s:
        rows[f'list_{counter}'].append(word)
        counter += dir
        # If the current counter is same as numRows, flip the direction of add counter by *-1
        if (counter/numRows) == 1:
            dir = dir*-1
        # If the current counter is 0, flip the direction of add counter by *-1, and set counter to row 2
        elif counter == 0:
            counter = 2
            dir = dir*-1
        # If the current counter is more than numRows, reset counter to 1
        elif counter > numRows:
            counter = 1

    # Loop through the dictionary and combine all the strings in the list
    for row in range(1, numRows+1):
        return_s += ''.join(rows[f'list_{row}'])

    return return_s

print(convert(s, numRows))







