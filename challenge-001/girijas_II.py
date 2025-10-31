"""
Problem Title: First Non-Repeating Character

Problem Description:
Given a string, return the first character that does not repeat anywhere in the string.
If all characters repeat or the string is empty, return an empty string.

Example:
Input: "aabbcddce"
Output: "e"
Explanation: 'e' is the first character that appears only once.

Input: "xxyz"
Output: "y"
Explanation: 'y' is the first character that appears only once.

Function Signature:
def first_unique_char(s: str) -> str:
    pass

Constraints:
- 1 <= len(s) <= 1000
- s contains only lowercase English letters

Bounty: 25 pts
"""
# Write your function here
def first_unique_char(s: str) -> str:
  for i in s:
    if s.count(i)==1:
      return i
  return " "

# Test cases
def run_tests():
    assert first_unique_char("aabbcddce") == "e"
    assert first_unique_char("xxyz") == "y"
    assert first_unique_char("aabbcc") == ""
    assert first_unique_char("abcabcde") == "d"
    assert first_unique_char("z") == "z"
    print("✅ All test cases passed!")

run_tests()
