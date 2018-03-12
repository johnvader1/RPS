import random
import time
from gpiozero import Button
Choices = ["Rock", "Paper", "Scissors"]
Weak = ["Paper", "Scissors", "Rock"]
CPUwins = 0
PlayerWins = 0

def RPorS():
    Rock = Button(12)
    Paper = Button(23)
    Scissors = Button(17)
    PlayerInput = "None"
    print("Rock Paper or Scissors?")
    while(PlayerInput == "None"):
        if Rock.is_pressed:
            PlayerInput = "Rock"
        elif Paper.is_pressed:
            PlayerInput = "Paper"
        elif Scissors.is_pressed:
            PlayerInput = "Scissors"
        else:
            time.sleep(.05)
    return PlayerInput

    

def Game():
    PlayerName = input("What is your name?\n")
    PlayerName.title()
    Choices = ["Rock", "Paper", "Scissors"]
    PlayerChoice = ["Rock"]
    CPUwins = 0
    PlayerWins = 0
    X = 0
    while CPUwins < 5:
        P = len(PlayerChoice)-1
        CPU = PlayerChoice[random.randint(X,P)]
        if P > 5:
            X = len(PlayerChoice)-3
        Player = RPorS()
        if Player[0] == CPU[0]:
            print("It was a tie both players picked\n", CPU)
            print(PlayerName, ":", PlayerWins, "|| CPU :", CPUwins)
            if Player[0] == "R":
                PlayerChoice.append("Paper")
            elif Player[0] == "S":
                PlayerChoice.append("Rock")
            else:
                PlayerChoice.append("Scissors")
        elif (Player[0] == "R" and CPU[0] == "S") or (Player[0] == "S" and CPU[0] == "P") or (Player[0] == "P" and CPU[0] == "R"):
            print("You win, CPU picked", CPU)
            PlayerWins += 1
            print(PlayerName, ":", PlayerWins, "|| CPU :", CPUwins)
            if Player[0] == "R":
                PlayerChoice.append("Paper")
            elif Player[0] == "S":
                PlayerChoice.append("Rock")
            else:
                PlayerChoice.append("Scissors")
        else:
            print("You lose, CPU picked", CPU)
            CPUwins += 1
            print(PlayerName, ":", PlayerWins, "|| CPU :", CPUwins)
            if Player[0] == "R":
                PlayerChoice.append("Paper")
            elif Player[0] == "S":
                PlayerChoice.append("Rock")
            else:
                PlayerChoice.append("Scissors")
    
    File = open("ScoreBourd.txt","r")
    List = File.readlines()
    #List = ["1","2","3",'4','5','6','7','8','9','10']
    i = 0
    #for line in data:
        #List[i] = line
        #i = i + 1
    #List = File.split("$")
    if PlayerWins > 99:
        Playerscore = str(PlayerWins) + PlayerName + "\n"
    elif PlayerWins > 9:
        Playerscore = "0" + str(PlayerWins) + PlayerName + "\n"
    else:
        Playerscore = "00" + str(PlayerWins) + PlayerName + "\n"
    #List.append("000Nobody\n")
    List.append(Playerscore)
    File.close()
    file = open("ScoreBourd.txt","w")


    #Scoreboard goes off of total points
    # In case of ties it will put the name with the latest first letter in there name.(Z-a)
    List = sorted(List)
    List.reverse()
    print("Scoreboard\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
    i = 0
    while i < 10:
        print(List[i])
        i = i + 1
        time.sleep(.25)
    List = "".join(List)
    file.write (List)
    file.close()
    Player = input("Want to play again?\n")
    Player = Player.title()
    if Player[0] == "Y":
        Game()
Game()

