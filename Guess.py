import random
import time
def play():
    x = int(input("Guess the Number"))
    time.sleep(2)
    user = random.randint(1,6)
    print("You guess is",x)
    print("The guess Should be",user)
    
    if x == user:
        print("You Guessed Right")
    elif x!= user:
        print("Wrong Guess")
        

play()
