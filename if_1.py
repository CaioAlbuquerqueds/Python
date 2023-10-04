from os import system

system('clear')

number = int(input("type a number: ")) 

if number >= 0:
    print(f"{number} is a positive number")
else:
    print(f"{number} is a negative number")    