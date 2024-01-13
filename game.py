import random
import sys
import time
from colorama import Fore

doc = """ 


NOTE : THIS IS JUST A COMPUTER SCIENCE FUNNY GAME

CODED_BY : ~JUPITER~,
PROGRAM_HEADER : GAME,
CODE_STATUS : NORMAL



        #########
    ###############
    ##
    ##
    ##        #########   ############   ########    #######     #########   
    ##         ######   ###         ##   ########   ########   #############
    ##          ####    ###         ##   ###   #######   ###  ###          ###
    #####       ####    ###         ##   ###   #######   ###  ###############
     ###########        ###############  ###             ###  ####
        #######                    ####  ###             ###   ##############
        #######                    ####  ###             ###      #############

The game consists of two modes of play: ONLINE and OFFLINE
ONLINE : One participant and the computer
OFFLINE : Two or more participants . The  Player's name is not compulsory for the offline players


"""
print(Fore.YELLOW + doc)
participant = input(Fore.GREEN + "Player's Name: ")
mode = input("mode :online/offline $")
_game = input("Select game to proceed : rand_num/cal $")


# <<<<<<<<<<<<<<<<<<<<<<<<<< Play <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def play(*args, **kwargs):
    _play = input("Play : yes/no $")

    for element in range(50):
        print('.', end='')
        if element == 0:
            print("Starting game", end='')
        if element == 49:
            if (((_play == 'y' or _play == 'yes') and mode=='online') or ((_play == 'y' or _play == 'yes') and mode=='offline')):
                print("successful")
            elif (((_play == 'n' or _play == 'no') and mode=='online') or ((_play == 'n' or _play == 'no') and mode=='offline')):
                print('terminating')
                time.sleep(5)
            else:
                print('failed')
        time.sleep(.15)

    if (_play == 'yes' or _play == 'y') and mode == 'online':
        on.select_game()
    elif (_play == 'yes' or _play == 'y') and mode == 'offline':
        off.select_game()


# <<<<<<<<<<<<<<<<<<<<<<<<<<    ONLINE  <<<<<<<<<<<<<<<<<<<<<<<<<<

class online:
    def select_game(self,*args, **kwargs):
        numberOfGames = int(input("Number of cycles to play: "))

        for number in range(numberOfGames):
            print(f"Game {number + 1}".center(50, '*'))
            time.sleep(5)
            try:
                if mode == "online":
                    if _game == 'rand_num':
                        on.randomNumbers()
                    elif _game == 'cal':
                        on.calculation()
                elif mode == "offline":
                    if _game == 'rand_num':
                        off.randomNumbers()
                    elif _game == 'cal':
                        off.calculation()

            except Exception as kerr:
                print(f'Something went wrong : {kerr}')

            # <<<<<<<<<<<<<< randomNumbers<<<<<<<<<<<<<<<<<<<<<<<<<<

    def randomNumbers(self):

        global num, participant, p_score, c_score

        print(f" {participant} selected Random numbers game ...Let the challenge begin!")

        luckNumber = int(input(f"Luck number for {participant} Or Type a key to quit: "))

        if luckNumber != 'quit' or luckNumber != 'q':
            num = luckNumber

            computer = random.randint(0, num + 1)

            print(f"Lucky number : {computer}")

            print(f"{participant} selected: {luckNumber}")

            # <<<<<<<<<<<<<< winner <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

            if luckNumber == computer:

                print(f"Congratulation! {participant}, You won!".center(50, " "))

            else:

                print(f"Sorry {participant}, you lose".center(50, " "))



        else:
            sys.exit(1)

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<calculations <<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def calculation(self):
        number = random.randint(0, 128)
        quest = input(f" Give the binary for the decimal {number} $")
        base = 1
        _bin = 0
        while number != 0:
            remainder = int(number % 2)
            number /= 2
            _bin += remainder * base
            base *= 10

        print(f"Computer solution {_bin}")
        print(f"Your solution {quest}")

        if int(quest) == _bin:
            print(f"Player's Name :{participant}\n Game Status : You won!".center(50, ' '))
        else:
            print(f"Player's Name :{participant}\n Game Status : You lose!".center(50, ' '))


# <<<<<<<<<<<<<<<<<<<<<<    OFFLINE <<<<<<<<<<<<<<<<<<<<<<<<<< 

class offline:
    def select_game(self,*args, **kwargs):
        numberOfGames = int(input("Number of cycles to play: "))

        for number in range(numberOfGames):
            print(f"Game {number + 1}".center(50, '*'))
            time.sleep(.05)
            try:
                if mode == "online":
                    if _game == 'rand_num':
                        on.randomNumbers()
                    elif _game == 'cal':
                        on.calculation()
                elif mode == "offline":
                    if _game == 'rand_num':
                        off.randomNumbers()
                    elif _game == 'cal':
                        off.calculation()

            except Exception as kerr:
                print(f'Something went wrong : {kerr}')

    def randomNumbers(self):
        numberOfPlayers = int(input("number of players :"))
        print("Each player should give their luckNumber :")
        total = 0
        for digit in range(numberOfPlayers):
            numbers = int(input(f"Player {digit + 1}  :"))
            total += numbers
            luckNumber = random.randint(0, total)
            if luckNumber == numbers:
                print(f"Player {digit + 1} won with  LuckNumber : {numbers}")
            else:
                print("No winner for the game!")

    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<calculations <<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def calculation(self):
        numberOfPlayers = int(input("number of players :"))
        print("Each player should give their luckNumber :")
        total = 0
        for digit in range(numberOfPlayers):
            numbers = int(input(f"Player {digit + 1}  :"))
            total += numbers
        number = random.randint(0, total)
        quest = input(f" Give the binary for the decimal {number} $")
        base = 1
        _bin = 0
        while number != 0:
            remainder = int(number % 2)
            number /= 2
            _bin += remainder * base
            base *= 10

        print(f"Computer solution {_bin}")
        print(f"Your solution {quest}")

        if int(quest) == _bin:
            print(f"Player's Name :{participant}\n Game Status : You won!".center(50, ' '))
        else:
            print(f"Player's Name :{participant}\n Game Status : You lose!".center(50, ' '))


on = online()

off = offline()

play()
