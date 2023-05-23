import random
name = input("Enter Your Name: ")
print("So ,Good Luck!",name)

words = ['Python','Web','Machine','Data Science','AI','Metaverse','SQL']


x= input("Guess the words:  ")


word = random.choice(words)
print("You Guessed",x)


if x == words:
     print("You Won")

else:
     print("The word is",word)


     print("You lose")
