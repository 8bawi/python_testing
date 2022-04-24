import random

highest = 10
answer = random.randint(1,highest)
print(answer)
print("Please guess number between 1 and {}: ".format(highest))
guess=-1
trials=1
while (trials <= 10):
    # print(trials)
    guess = int(input())
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

