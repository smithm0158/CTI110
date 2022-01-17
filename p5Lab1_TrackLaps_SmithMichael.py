LAPS_PER_MILE = 4
MILES_PER_LAP = .25

# Define your function here 
def miles_to_laps(user_miles):
    laps = user_miles * LAPS_PER_MILE
    print('{:.2f}'.format(laps))
    return laps

#print(miles)
if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    user_miles = float(input("Enter the number of miles ran: "))
    miles_to_laps(user_miles)
