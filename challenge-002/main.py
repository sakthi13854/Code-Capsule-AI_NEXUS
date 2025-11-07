"""
Problem Title: Valid Palindrome

Problem Description:
Given a string, determine if it is a palindrome, considering only alphanumeric 
characters and ignoring cases. A palindrome reads the same forward and backward.

Example:
Input: "A man, a plan, a canal: Panama"
Output: True
Explanation: After removing non-alphanumeric characters and converting to lowercase,
we get "amanaplanacanalpanama" which is a palindrome.

Input: "race a car"
Output: False
Explanation: After processing, we get "raceacar" which is not a palindrome.

Input: " "
Output: True
Explanation: An empty string (after removing non-alphanumeric) is considered a palindrome.

Function Signature:
def is_palindrome(s: str) -> bool:
    pass

Constraints:
- 1 <= len(s) <= 200,000
- The string consists of printable ASCII characters
- Consider only alphanumeric characters (letters and digits)
- Ignore case when comparing characters
"""

# Write your function here
def is_palindrome(s: str) -> bool:
    pass


# Test cases
def run_tests():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome(" ") == True
    assert is_palindrome("0P") == False
    assert is_palindrome("a.") == True
    print("✅ All test cases passed!")

run_tests()
