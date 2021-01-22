import random


def get_integer(prompt):
    """
    Get an integer from standard input (stdin)

    The function will continue looping, and prompting the user, until a valid `int` is entered.
    :param prompt: The string that the user will see when they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        print("{0} is invalid response".format(temp))

# def get_integer(prompt):
#     while True:
#         temp = input(prompt)
#         if temp.isnumeric():
#             return int(temp)
#         else:
#             if temp.isalpha():
#                 print("invalid response")




highest = 10
answer = random.randint(1, highest)

guess = 0
print("please guess a number between 1 and {}:".format(highest))

while guess != answer:
    guess = get_integer(": "")
    if guess == "exit".casefold():
        break
    if guess == answer:
        print("good job")
        break
    else:
        if guess < answer:
            print("go higher!")
        else:
            print("guess lower")

# if guess < answer:
#     print("nope, try again")
#     guess=int(input())
#     if guess == answer:
#         print("nice job!")
#     else:
#         print("nah, wrong again")
# elif guess> answer:
#     print("go down!")
#     guess=int(input())
#     if guess == answer:
#         print("nice job!")
#     else:
#         print("nah, wrong again")
# else:
#     print("well done!")
