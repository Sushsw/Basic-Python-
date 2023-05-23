user = input("Enter first number")
operation = input ("select operation:( +,-,*,%) ")
user1 = input("Enter Second number")

user = int(user)
user1 = int (user1)

if operation == '+':
    print(user + user1)
elif  operation == '*':
    print(user * user1)
elif operation == '-':
    print(user - user1)
elif operation == '%':
    print(user % user1)
else:
    print("Invalid Symbol")