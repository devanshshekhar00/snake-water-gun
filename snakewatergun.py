import random

print("WELCOME TO SNAKE WATER GUN")
options = ["s" , "w" , "g"]



# scores of games
score_computer = 0
score_user = 0



while(score_computer <= 5 or score_user <=5):

    userinput = input("Type s for snake ,w for water and g for gun\n")
    a = random.choice(options)
    if a != userinput:
            if a == options[0] and userinput == options[1]:
                score_computer += 1
                print(score_user , score_computer)
            elif a == options[0] and userinput == options[2]:
                score_user += 1
                print(score_user,score_computer)
            elif a == options[1] and userinput == options[2]:
                score_computer+= 1
                print(score_user , score_computer)
            elif a == options[1] and userinput == options[0]:
                score_user+=1
                print(score_user , score_computer)
            elif a == options[2] and userinput == options[0]:
                score_computer += 1
                print(score_user , score_computer)
            elif a == options[2] and userinput == options[1]:
                score_user+= 1
                print(score_user , score_computer)
    else:
        score_user+=0
        score_computer+=0
        print(score_user,score_computer)

    if score_computer == 5:
        print("YOU LOOSE")
        break
    elif score_user == 5:
        print("YOU WIN")
        break


