import random


def get_integer(prompt):
    """
    Get an integar from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.
    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integar that the user enters.        
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp) # There is no need to write an else statement as if the "if" is true the function will return and 
                             # then it will continue to do the print statement.
        print("{0} is not a valid number.".format(temp))

print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)
highest = 1000
answer = random.randint(1,highest)
print(answer) #TODO: remove after testing
print("Please guess number between 1 and {}: ".format(highest))
guess=-1
trials=1
while (trials <= 10):
    # print(trials)
    guess = get_integer(": ")
    if guess ==0:
        print("you have exited the game") 
        break
    if guess == answer :
        # print ("You got it first time")
        print("Well done, you guessed it")
        break
    elif guess !=answer and guess !=0:
        if guess < answer:
            print("Please Guess higher")
        else:
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        #     break
        # else:
        #     print("Sorry, you have not guessed correctly")
    trials=trials+1
print(trials)              

