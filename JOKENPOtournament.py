from random import randint
from time import sleep

TotalRounds = int(input("HOW MANY ROUNDS DO YOU WANT TO PLAY?:  "))
ActualRounds = 1
draw = 0
PlayerWin = 0
MachineWin = 0

while ActualRounds <= TotalRounds:
    print("=-=-=-==-==-=-=-=-=-=-=-=-=-=-=-=\n"
          "                 JOKENPO         \n"
          f"         MATCH No.{ActualRounds}\n"
          "===================================\n"
          "[ 1 ] FOR ROCK\n"
          "[ 2 ] FOR PAPER\n"
          "[ 3 ] FOR SCISSORS\n"
          "===================================")
    player = int(input("CHOOSE YOUR WEAPON:  "))
    print("==================================")
    machine = randint(1, 3)
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PO")
    sleep(0.5)
    print("==================================")
    if player == machine:
        print("DRAW!")
        if player == 1:
            print("BOTH THREW ROCKS")
        elif player == 2:
            print("BOTH THREW PAPERS")
        elif player == 3:
            print("BOTH THREW SCISSORS")
        draw += 1
    elif player == 3 and machine == 2:
        print("MACHINE THREW PAPER")
        print("PLAYER THREW SCISSORS")
        print("\033[0:32:32mYOU WON!\033[m")
        PlayerWin += 1
    elif player == 3 and machine == 1:
        print("MACHINE THREW ROCKS")
        print("PLAYER THREW SCISSORS")
        print("\033[0:31:31mYOU LOST!\033[m")
        MachineWin += 1
    elif player == 2 and machine == 3:
        print("MACHINE THREW SCISSORS")
        print("PLAYER THREW PAPER")
        print("\033[0:31:31mYOU LOST!\033[m")
        MachineWin += 1
    elif player == 2 and machine == 1:
        print("MACHINE THREW ROCKS")
        print("PLAYER THREW PAPER")
        print("\033[0:32:32mYOU WON!\033[m")
        PlayerWin += 1
    elif player == 1 and machine == 2:
        print("MACHINE THREW PAPER")
        print("PLAYER THREW ROCKS")
        print("\033[0:31:31mYOU LOST!\033[m")
        MachineWin += 1
    elif player == 1 and machine == 3:
        print("MACHINE THREW SCISSORS")
        print("PLAYER THREW ROCKS")
        print("\033[0:32:32mYOU WON!\033[m")
        PlayerWin += 1
        print("============================")
    sleep(2)
    ActualRounds += 1

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("    TOURNAMENT RESULTS.        ")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
if PlayerWin > MachineWin:
    print("\033[0:32:32mYOU WON THE TOURNAMENT!\033[m")
    print(f"PLAYER {PlayerWin} x {MachineWin} MACHINE")
    print(f"{draw} TIES")
elif PlayerWin < MachineWin:
    print("\033[0:31:31mMACHINE WON THE TOURNAMENT!\033[m")
    print(f"PLAYER {PlayerWin} x {MachineWin} MACHINE")
    print(f"{draw} TIES")
elif PlayerWin == MachineWin:
    print("IT'S A TIE!")
    print(f"PLAYER {PlayerWin} x {MachineWin} MACHINE")
    print(f"{draw} TIES")

