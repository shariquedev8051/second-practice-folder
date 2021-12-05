import random
print("Hello Gambler")
print("Guess the number between 1 and 10 in three chances and win prizes!!")
print("")
gnum = random.randint(1,10)
for i in range(3):
    num = int(input("Enter you number here:- "))
    if num == gnum:
        print("Yeppi you have won the game!!!")
        break
    else:
        print("Try once again...")
else:
    print("You have used all of your turn")
input("Bye Bye Gambler")