import random

def win():
    
    coin = random.choice([0,1,2])
    if coin == 0:
        print("Heads")
    elif coin == 1:
        print("Tails")
    elif coin == 2:
        print("Coin stands Straight ")
        
win()
