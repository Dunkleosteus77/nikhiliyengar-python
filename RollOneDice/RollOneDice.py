import random
def main():
    count=0
    dicelist=[]
    onelist=[]
    twolist=[]
    threelist=[]
    fourlist=[]
    fivelist=[]
    sixlist=[]
    while input("Do you wanna play? ")=="y":
        count=count+1
        number=int(input("How many dice? "))
        times=int(input("How many times do you roll? "))
        for dice in range(number):
            for dice in range(times):
                randInt=GenInt()
                dicelist.append(Dice(randInt))
                if randInt==1:
                    onelist.append(randInt)
                if randInt==2:
                    twolist.append(randInt)
                if randInt==3:
                    threelist.append(randInt)
                if randInt==4:
                    fourlist.append(randInt)
                if randInt==5:
                    fivelist.append(randInt)
                if randInt==6:
                    sixlist.append(randInt)
                Horizontal(dicelist)
                counterlist=len(onelist)+len(twolist)+len(threelist)+len(fourlist)+len(fivelist)+len(sixlist)
                print("There're "+str(len(onelist))+" ones, or "+str((len(onelist)/counterlist)*100)+"%")
                print("There're "+str(len(twolist))+" twos, or "+str((len(twolist)/counterlist)*100)+"%")
                print("There're "+str(len(threelist))+" threes, or "+str((len(threelist)/counterlist)*100)+"%")
                print("There're "+str(len(fourlist))+" fours, or "+str((len(fourlist)/counterlist)*100)+"%")
                print("There're "+str(len(fivelist))+" fives, or "+str((len(fivelist)/counterlist)*100)+"%")
                print("There're "+str(len(sixlist))+" sixes, or "+str((len(sixlist)/counterlist)*100)+"%")
        if count==1:
            print("You've played 1 time")
        if count!=1:
            print("You've played "+str(count)+" times")

def Dice(randInt):
    #diceOne="-------\n|     |\n|  *  |\n|     |\n-------"
    #diceTwo="-------\n|     |\n|*   *|\n|     |\n-------"
    #diceThree="-------\n|*    |\n|  *  |\n|    *|\n-------"
    #diceFour="-------\n|*   *|\n|     |\n|*   *|\n-------"
    #diceFive="-------\n|*   *|\n|  *  |\n|*   *|\n-------"
    #diceSix="-------\n|*   *|\n|*   *|\n|*   *|\n-------"
    Dash="-------"
    Blank="|     |"
    OneMiddle="|  *  |"
    OneLeft="|*    |"
    OneRight="|    *|"
    Sides="|*   *|"
    diceOne=[Dash,Blank,OneMiddle,Blank,Dash]
    diceTwo=[Dash,Blank,Sides,Blank,Dash]
    diceThree=[Dash,OneLeft,OneMiddle,OneRight,Dash]
    diceFour=[Dash,Sides,Blank,Sides,Dash]
    diceFive=[Dash,Sides,OneMiddle,Sides,Dash]
    diceSix=[Dash,Sides,Sides,Sides,Dash]
    dicelist=[diceOne,diceTwo,diceThree,diceFour,diceFive,diceSix]
    if randInt==1:
        return diceOne
    elif randInt==2:
        return diceTwo
    elif randInt==3:
        return diceThree
    elif randInt==4:
        return diceFour
    elif randInt==5:
        return diceFive
    elif randInt==6:
        return diceSix

def GenInt():
    return random.randint(1,6)

def Horizontal(dicelist):
    for row in range (0,5):
        for columns in range (0,len(dicelist)):
            print(dicelist[columns][row], end='\t')
        print()


main()
