#Math Quiz
#11/18/21
#CTI 110 P5HW2 - Math Quiz
#Michael Smith
import random

number1 = random.randint(0, 250)
number2 = random.randint(0,250)



def menu():
    print("MAIN MENU")
    print("-"*10)
    print("1) Adding Random Numbers")
    print("2) Subtracting Random Numbers")
    print("3) Exit")
    choice = int(input("Please choose one of the menu options"))

    if choice == 1:
        option_one()
    elif choice ==2:
        option_two()
    elif choice == 3:
        option_three()
    else:
        print("Please enter a valid choice.")
    

def option_one():
    answer = number1 + number2
    print(number1)
    print("+", number2)
    guess = int(input("Enter the answer: "))
    if guess == answer:
        print("Congrats! You answered right!")
    else:
        print("Sorry, the answer is: ", answer)

def option_two():
    answer = number1 - number2

    print(number1)
    print("-", number2)

    guess = int(input("Enter the answer: "))

    if guess == answer:
        print("Congrats! You answered right!")
    else:
        print("Sorry, the answer is: ", answer)

def option_three():
    exit()


menu()
