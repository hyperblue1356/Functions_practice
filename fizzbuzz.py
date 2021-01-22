counter = 0
value = counter
def fizz_buzz(number: int) -> str:
    """Two players- take turns counting alternate numbers, if num"""

    if number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    elif number % 15 == 0:
        return "fizzbuzz"
    else:
        return "is not a fizzbuzz"

def computer_turn():
    global counter
    print("I think that {} is {}"
          .format(counter, fizz_buzz(counter)))
    counter = counter + 1



while counter < 100:
    counter = counter +1
    computer_turn()
    user_guess = (input("The number is {}, so, is it fizz, buzz, fizzbuzz, or none of them? Enter 'fizz', 'buzz', 'fizzbuzz' or 'is not a fizzbuzz':".format(counter)))
    fizz_buzz(counter)
    if user_guess == "is not a fizzbuzz" and fizz_buzz(counter):
        print("you got it")
    elif user_guess == "fizz" and fizz_buzz(counter):
        print("you got it")
    elif user_guess == "buzz" and fizz_buzz(counter):
        print("you got it")
    elif user_guess == "is not a fizzbuzz" and fizz_buzz(counter):
        print("you got it")
    else:
        print("ah, maybe next time")









