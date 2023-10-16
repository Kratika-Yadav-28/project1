import random
def gameWin(comp,you):
    if(comp==you):
        return None
    elif(comp=="s"):
        if(you=="w"):
            return False
        elif(you=="g"):
            return True
    elif(comp=="w"):
        if(you=="s"):
            return True
        elif(you=="g"):
            return False
    elif(comp=="g"):
        if(you=="s"):
            return False
        elif(you=="w"):
            return True
print("comp turn :snake(s),water(w) or gun(g) ?")
randNo = random.randint(1,3)
if(randNo==1):
    comp = "s"
elif(randNo==2):
    comp="w"
elif(randNo==3):
    comp="g"

you = input("Your turn:snake(s),water(w) or gun(g) ?\n")
a = gameWin(comp,you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie !")
elif a :
    print("You won....")
else:
    print("You lose...")