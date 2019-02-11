


print("Would you like to run or walk?")
user_input = input()
counter = 0
energy = 100


# The if statements in the while loop allow the user to continue to put in their user_input
# and also allows the counter to keep running

while (user_input == "walk" or user_input == "run"):
    if(user_input == "walk"):
        counter += 1
        energy += 1
        print("Distance from home is {}km".format(counter))
        print("Your energy:{}".format(energy))
        print("Would you like to run or walk?")
        user_input = input()
    elif(user_input == "run"):
        counter += 5
        energy -= 1
        print("Distance from home is {}km".format(counter))
        print("Your energy:{}".format(energy))
        print("Would you like to run or walk?")
        user_input = input()
    elif(user_input == "home"):
        print("You are going home")
    else:
        print("You are going home")
