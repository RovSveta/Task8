from colorama import Fore
from datetime import datetime

years_list = []

for i in range(5):
    year = int(input(f"Give the birth year of person {i + 1}:\n"))
    years_list.append(year)

print("Let's process all birth years...")
for year in years_list:
    current_year = datetime.now().year
    age = current_year - year
    if 0 < age <= 125:
        print(f"{Fore.LIGHTGREEN_EX}{age} years old, age OK!")
    else:
        print(f"{Fore.RED}{age} years old, incorrect age.")
print("All done!")
