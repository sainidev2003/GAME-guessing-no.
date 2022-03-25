# n=18
# guess any number smaller than 100 i will check your guessing is correct or not?
i=0
while(i< 100):
    n=int(input("guess the no\n"))
    if(n==18):
        print("congrats , GAME OVER")
        print("you guess in ", i)
        break
    elif (n<18):
        print("your guess number is smaller than the excat number choose again")
        i=i+1
        continue
        
    elif(n>18) and (n<100):
        print("your guess number is greater than the excat number please try again")
        i=i+1
        continue
    else:
        print("invalid input please enter  smaller  number than 100")
        i=i+1



