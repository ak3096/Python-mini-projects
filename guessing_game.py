import random

def guess(x):
    random_number = random.randint(1,x) #store random number
    guess_num=0
    while(guess_num!=random_number):
        guess_num = int(input(f"Guess a number between 1 and {x}:"))
        if(guess_num>random_number):
            print("too high")
        elif(guess_num<random_number):
            print("too low")
    print(f"You guessed correctly {guess_num}")

guess(10) #range till 10