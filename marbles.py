import random

timesPlayed = int(input("How many times are you going to play? \n"))
marblesBowl = ["green","green","green","red","red","black"]
playerEarnings = []

def marble_game(list1, timesPlayed):
    for i in range(timesPlayed):
        draw1 = random.randint(0,len(list1)-1)
        list1.pop(draw1)

        draw2 = random.randint(0,len(list1)-1)

        if draw1 == draw2:
            if i == 0:
                playerEarnings = [1]
            else:
                newValueWin = playerEarnings[i-1] + 1
                playerEarnings.append(newValueWin)
    
        else:
            if i == 0:
                playerEarnings = [-1]
            else: 
                newValueLose = playerEarnings[i-1] - 1
                playerEarnings.append(newValueLose)

        list1.append(draw1)

    return playerEarnings


print(marble_game(marblesBowl, timesPlayed))