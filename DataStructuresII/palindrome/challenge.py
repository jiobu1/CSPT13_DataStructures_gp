
'''
wrtie a function that checks if a string is a palindrome
if it is then return True ad if it is not return False
i.e.
"Mom" --> Reverse --> "Mom" return True
"ADD" --> Reverse --> "DDA" return False

clarifying question can we deal with case differences
- no, must normalize the case.
'''

# function is_palindrom 
def is_palindrome(s):
    """
    is_palindrome
    ---------------
    Takes in a string as an input 
    Outputs a boolean of True or False
    Depending on the outcome of the question
    - is this string a palindrome
    """
    # normalize our string to have all lower case characters
    lower_s = s.lower()
    # make lower_s into a list
    list_lower_s = list(lower_s)
    # reverse the lower_s using reversed() as rev_lower_s
    rev_lower_s =  list(reversed(list_lower_s))

    # compare the rev_lower_s with lower_s
    if list_lower_s == rev_lower_s:
        # return True
        return True
    # otherwise
    else:
        # return Flase
        return False

# is_palindrome with input of "Mom"
print(is_palindrome("Mom"))
# is_palindrome with input of "Mom"
print(is_palindrome("Add"))

def alternative(str):
    # normalize our string to have all lower case characters
    lower_s = str.lower()
    # reverse lower_s using a slice
    reversed_s = lower_s[::-1]
    # compare the lower_s and reversed_s
    return lower_s == reversed_s

print(alternative("Mom"))
print(alternative("Add"))