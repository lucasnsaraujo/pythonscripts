from random import randint
from time import sleep
LotteryResults = list()
UserGuess = list()
CorrectNumbers = 0
for item in range(0,6): # GENERATE THE LOTTERY RESULTS
    while True:
        number = randint(1, 12)
        if number not in LotteryResults:
            LotteryResults.append(number)
            break
print('=-'* 30)
print('LOTTERY SIMULATOR by. lucasnsaraujo')
print('=-'* 30)
for i in range(0,6): # READS LOTTERY GUESS FROM USER
    while True:
        guess = int(input(f"Write the {i + 1}. number: "))
        if guess not in UserGuess:
            UserGuess.append(guess)
            break
LotteryResults.sort()
UserGuess.sort()
for t in range(0,6):
    if LotteryResults[t] in UserGuess:
        CorrectNumbers += 1
print(f'Your guess was : {UserGuess}')
sleep(1)
print(f'The lottery result is : {LotteryResults}')
if CorrectNumbers == 6:
    print('CONGRATULATIONS! YOU WON THE LOTTERY!')
