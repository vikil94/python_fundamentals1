#
# print("What is your name")
# user_name = input()
# print("Hello {}".format(user_name))
#
#
# secret_password = "please"
# print("What is the password")
# password_attempt = input()
#
# # this is a boolean if the password is corrent it will return true
# # if the password is wrong it will return false
# correct_or_not = (password_attempt == secret_password)
#
# print("That's {}!".format(correct_or_not))
#
print("How many cookies have been eaten?")
eaten = input()

# convert user input to integer and subtract it from 12
remaining_cookies = 12 - int(eaten)

print("There are {} cookies left.".format(remaining_cookies))

# ask the user how old they are and have the program output what year they were born

print("How old are you?")
user_age = input()

year_born = 2019 - int(user_age)

print("You were born in the year {}".format(year_born))
