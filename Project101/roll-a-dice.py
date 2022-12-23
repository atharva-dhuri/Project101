import random 

def RollDice():
    number = random.randint(1, 6)
    print(number)
    Choice()

def Choice():
    print("Press '1' to Roll the dice")
    print("         OR               ")
    print("Press '2' to exit")

    response = int(input("Do you want to roll the dice: "))

    if(response == 1):
        RollDice()
    if(response == 2):
        exit()

Choice()