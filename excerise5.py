


print("Would you like to run or walk?")
user_input = input()
counter = 0

while (user_input == "walk" or user_input == "run"):
    if(user_input == "walk"):
        counter += 1
        print("Distance from home is {}km".format(counter))
        print("Would you like to run or walk?")
        user_input = input()
    elif(user_input == "run"):
        counter += 5
        print("Distance from home is {}km".format(counter))
        print("Would you like to run or walk?")
        user_input = input()


# while user_input == "run":
#     counter += 5
#     print("Distance from home is {}km".format(counter))
#     print("Would you like to run or walk?")
#
