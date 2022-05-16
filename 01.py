import random
def gamewin(comp,b):
    if comp == b:
        return None
    elif comp == 'snake':
        if b=='water' :
            return False  
        elif b=='gun':
            return True

    elif comp == 'water':
        if b=='snake' :
            return True  
        elif b=='gun':
            return False  
    elif comp == 'gun':
        if b=='water' :
            return True  
        elif b=='snake':
            return False      

rand= random.randint(1,3)
if rand==1:
    comp='snake'
elif rand==2:
    comp='water'
elif rand==3:
    comp='gun'
print("computer has choosen, yours turn")
b=input("enter the no snake(s) water(w) , gun(g)")
a=gamewin(comp,b)
print(f"computer choose{comp}")
print(f" you choose {b}")
if a==None:
    print("the game is tie")
elif a==True:
    print("you win")  
else:
    print("you are losser")  
print("GAME OVER!")    


            