#Lists and stuff
#11/10/21
#CTI-110 P5HW1 - Lists and sets
#Michael Smith

def main():
    menu()
    choice()    
    #list1 = get_numbers()
    #set1, set_min, set_max, set_sum, set_avg = evaluator(list1)
    #display(set1, set_min, set_max, set_sum, set_avg, list1)
    

def get_numbers():
    numbers = []
    for i in range(3):
        number = int(input("Please enter number: "))
        numbers.append(number)
    #print(numbers)
    return numbers
    
    

def evaluator(list1):
    number_set = set(list1)
    set_min = min(list1)
    set_max = max(list1)
    set_sum = sum(list1)
    set_avg = sum(list1) / 10
    #xd = "something"

    return number_set, set_min, set_max, set_sum, set_avg


def display(set1, set_min, set_max, set_sum, set_avg, list1):
    #print("xd")
    print("Set: ", set1)
    print("Minimum Value: ", set_min)
    print("Maximum Value: ", set_max)
    print("Sum of Value: ", set_sum)
    print("Average of values: ", set_avg)
    print("List is: ",list1)

def menu():
    print("-----------MENU-------------")
    print("1) Create List")
    print("2) Display Results")
    print("3)Exit")
    print("----------------------------------")

    
def choice():
    choice = int(input("Please enter a choice: "))
    
    if choice == 1:
        list1 = get_numbers()
        menu()
        choice = int(input("Please enter another option: "))
    if choice == 2:
        if len(list1) == 0:
            print("please enter a list")
            menu()
            choice = int(input("Please enter another option: "))
        else:
            set1, set_min, set_max, set_sum, set_avg = evaluator(list1)
            display(set1, set_min, set_max, set_sum, set_avg, list1)
            
    

    
main()



#
