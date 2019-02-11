# Ask the user to enter a number. Use an if statement to print "that's a big number!" if the number is 100 or more, or "why not dream a little bigger?" otherwise.


print("enter a number")
user_number = input()

if int(user_number) > 100:
    print("That's a big number")
elif int(user_number) < 100:
    print("why not dream a little bigger?")

# Ask the user to enter their age, and then display a message telling them how many years apart in age you are from them. If they enter a number larger than 105, print "I'm not sure I believe you".

print("Enter your age")
user_age = input()

years_apart = 25 - int(user_age)
if int(user_age) > 105:
    print("I don't believe you")
else:
     print("We are {} year/years apart".format(years_apart))


my_name = "Vikil"
print("Enter your name")
user_name = input()

if my_name == user_name:
    print("We have the same name!")
else:
    print("Hello {}, nice to meet you".format(user_name))


secert_number = 9;
print("Enter a number")
user_number1 = input()
if int(user_number1) == secert_number:
    print("You win!")
elif int(user_number1) - secert_number == 1 or -1:
    print("so close")
else:
    print("Try again")
