import random

computer_choose = random.choice([1, 0, -1])
you_str = input("Enter your choice :) ")
# 1 for snake, -1 for water, 0 for gun 
you_dict = {"s": 1, "w": -1, "g": 0} 
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

you_chose = you_dict[you_str]

print(f"You chose :) {reverse_dict[you_chose] } \nComputer Chose :) {reverse_dict[computer_choose]} ")

if(computer_choose == you_chose):
    print("Draw :)")

else:
    if(computer_choose == -1 and you_chose == 1):
        print("You Win :)")
    elif(computer_choose == 1 and you_chose == 0):
        print("You Win :)")
    elif(computer_choose == 0 and you_chose == -1):
        print("You Win :)")
    elif(computer_choose == -1 and you_chose == 0):
        print("You lose :(")
    elif(computer_choose == 1 and you_chose == -1):
        print("You lose :(")
    elif(computer_choose == 0 and you_chose == 1):
        print("You lose :(")