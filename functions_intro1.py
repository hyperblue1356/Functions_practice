def multiply(x: float, y: float) -> float:

    result = x * y
    print(result)
multiply(234,567)


#
#
# def is_palindrome(string: str) -> bool:
#     # backwards = string[::-1]
#     # return backwards == string
#     return string[::-1].casefold() == string.casefold()
# #
# #
# def palindrome_sentence(sentence: str) -> bool:
# #
# # word = input("Please enter a word to check: ")
# # if palindrome_sentence(word):
# #     print("'{}' is a palindrome".format(word))
# # else:
# #     print("'{}' is not a palindrome".format(word))
#
# def fibonacci(n: int) -> bool:
#     """Return the `n` th fibonacci number for positive `n`"""
#     if 0 <= n <= 1:
#         return n
#
#     n_minus1, n_minus2 = 1, 0
#
#     result = None
#     for f in range(n - 1):
#         result = n_minus2+ n_minus1
#         n_minus2 = n_minus1
#         n_minus1 = result
#
#     return result
#
# for i in range(36):
#     print(i, fibonacci(i))
#
# p = palindrome_sentence()