def multiply(x, y):
    """
    Get two parameters `x` and `y` which are `int` multiply them
    and return the result.

    """
    result = x * y
    return result


def is_palindrome(string):
    """
    Get string and parse it backwards and match it to the original
    string to determine if it's a palindrome or not.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_senstence(sentence):
    """
    Get a sentence and parse it for alpha numberic
    characters and then call is_palindrome to check
    if the are palindrome or not.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)

    
# answer = multiply(10.5, 4)
# print(answer)

# word = input("Please enter a word to check: ")
# print(word)
# if palindrome_senstence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

answer = multiply (18,3)
print(answer)