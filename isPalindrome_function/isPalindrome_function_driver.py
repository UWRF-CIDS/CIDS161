import sys
#from isPalindrome_function import isPalindrome

test_string = sys.argv[1]
if isPalindrome(test_string):
    print(f"\"{test_string}\" is a palindrome!")
else:
    print(f"\"{test_string}\" is not a palindrome...")
