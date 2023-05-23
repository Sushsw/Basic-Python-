
import random
import time
def dice():
    while True:
        user = input("Roll the Dice")
        print("Rolling Dice.........")
        time.sleep(5)
        print("The value is", random.randint(1,6))
         
        again = input("Try Again?'y' for Yes and 'n' for No: ")
        if again == 'n':
            print("Ok")
            break
    

(dice())
