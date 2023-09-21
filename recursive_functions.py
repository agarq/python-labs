#RECURSIVE FUNCTION: a function that calls itself in its body

#example: get the factorial of a number:
# 1! = 1
# 2! = 2 * 1 = 2
# 3! = 3 * 2 * 1 = 6

'''
def factorial(n):
    """Return the factorial of positive integer n """
    if n == 1: #base case
        return 1
    else: #recursive case
        return n * factorial(n - 1)
    
print(factorial(4))


def sum_digits(n):
    """Return the sum of digits of positive integer n """
    if n < 10:
        return n
    else:
        all_but_last = n // 10 # with double // express the result of the division as an integer.
        last = n % 10
        return sum_digits(all_but_last) + last

print(sum_digits(45))

'''

#palindrome examples: mom, nun, k, 151, 1221
#function returns is something is palindrome or not

def isPalindrome(s):
    '''return whether a string is a palindrome'''
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

word = input("Write the word you want to check if is a Palindrome: ")
print(isPalindrome(word))


