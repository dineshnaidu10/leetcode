# Given a string s, find the length of the longest without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

# Constraints:

#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

s = 'au'

def lengthOfLongestSubstring(s):
    l = 0
    r = 1
    max_len = 0

    if len(s) == 1:
        return 1

    while r <= len(s):
        substring = s[l:r]
        if len(substring) == len(set(substring)):
            r += 1
            max_len = len(substring)
        else:
            l += 1
            r += 1
    
    return max_len

print(lengthOfLongestSubstring(s))

