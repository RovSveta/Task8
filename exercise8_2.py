from colorama import Fore, Back, Style
import random

random_num = random.randint(1,20)
print(random_num)
match = False

while not match:
    number = int(input(f"{Style.RESET_ALL}Guess the number (1-20):\n"))
    if number < random_num:
        print(f"{Back.BLUE} Too low")
        print(f"{Style.RESET_ALL}")
    if number > random_num:
        print(f"{Back.RED} Too high")
        print(f"{Style.RESET_ALL}")
    if number == random_num:
        print(f"{Back.GREEN} CONGRATULATIONS!")
        match = True
