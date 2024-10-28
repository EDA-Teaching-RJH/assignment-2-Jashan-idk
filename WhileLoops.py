### Part Two -- your code goes here. 
import random
secret_number = random.randint(1, 100)


print("guess a number from 1 to 100 ")
user = 0
while user != secret_number :
    user = int(input("what is your guess?"))

    if user == secret_number:
        print("correct")

    else:
        print("wrong try again")



