'''
This problem is from
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

# idea: 
# scan from beginning to the end 
# using a hash table to store characters and their most recent index 
# using a variable `start` to store the beginning of the current string 
# if repeat, then compute length of the before-repeat string and update `start`
# complexity O(n)
# space complexity O(1) since there are only 26 lowercase chars


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLen = 0 
        apperred = {} 
        for i in range(len(s)):
            if s[i] in apperred and start <= apperred[s[i]]:
                start = apperred[s[i]] + 1 
            else: 
                maxLen = max(maxLen, i - start + 1)
            apperred[s[i]] = i  
        return maxLen 
        
tests = [ ('abcabcbbacdefabcdef', 6),
          ('bbbbbb', 1),
          ('a', 1),
          ('', 0),
          ('abcdaebcde', 5),
          ('pwwkew', 3)]

for test in tests:
    assert Solution().lengthOfLongestSubstring(test[0]) ==test[1], "incorrect in " + str(test)

print "All tests passed!"