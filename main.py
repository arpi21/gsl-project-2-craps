import random
def roll():
    dice_1 = random.randrange(1,7)
    dice_2 = random.randrange(1,7)
    return(dice_1,dice_2)

def dice(dice):
    dice_1,dice_2 = dice
    print("the sum is {} + {} = {}".format(dice_1,dice_2,sum(dice)))

Round1 = roll()
dice(Round1)

sum_of_dice = sum(Round1)
while True:
    if sum_of_dice in (7,11):
        print("You Won")
        break
    elif sum_of_dice in (2,3,12):
        print("You Lost")
        break
    else:
        goal = sum_of_dice
        while True:
            New_Roll = roll()
            dice(New_Roll)
            newsum = sum(New_Roll)
            if newsum == goal:
                print("You Won")
                break
            elif newsum == 7:
                print("You Lost")
                break
        break


