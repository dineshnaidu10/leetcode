# Given a string s, return the longest in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters.

s = 'cbbd'

def longestPalindrome(s):
    # Reverse the input string into another string
    s_reverse = s[::-1]
    # Init a dictionary to store Key (Length of Palindrome) - Value (Palindrome)
    substring_dict = dict()
    temp_substring = ''
    substring = ''

    # Init a left and right pointer like a sliding window
    l, r = 0, 1
    while r <= len(s):
        temp_substring = s[l:r]
        # If the current substring exists in the reverse order and the substring is equal to its reverse self, it is a palindrome
        if (temp_substring in s_reverse) and (temp_substring == temp_substring[::-1]):
            substring = temp_substring
            substring_dict[len(substring)] = substring
            # Increment right pointer by 1
            r += 1
        # If the current substring exists only in the reverse order and not a palindrome, increment right pointer by 1
        elif temp_substring in s_reverse:
            r += 1
        # Increment left pointer by 1
        else:
            l += 1

    return substring_dict[max(substring_dict)]

print(longestPalindrome(s))



