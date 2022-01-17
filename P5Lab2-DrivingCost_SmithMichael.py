# Define your function here.
    
def driving_cost(driven_miles, miles_per_gallon, cost_per_gallon):
    gallons_used = driven_miles / miles_per_gallon
    cost = gallons_used * cost_per_gallon    
    return cost
    
    
if __name__ == '__main__':
    # Type your code here.
    driven_miles = float(input("Enter driven miles: "))
    miles_per_gallon = float(input("Enter the miles per gallon: "))
    cost_per_gallon = float(input("Enter the cost per gallon: "))
    
    cost1 = driving_cost(10, miles_per_gallon, cost_per_gallon)
    cost2 = driving_cost(50, miles_per_gallon, cost_per_gallon)
    cost3 = driving_cost(400, miles_per_gallon, cost_per_gallon)


    
    print('Cost for 10 miles: {:.2f}'.format(cost1))
    print('Cost for 50 miles: {:.2f}'.format(cost2))
    print('Cost for 400 miles: {:.2f}'.format(cost3))
    
    driven = driving_cost(driven_miles, miles_per_gallon, cost_per_gallon)
    
    #driving_cost(driven_miles, miles_per_gallon, cpg)
