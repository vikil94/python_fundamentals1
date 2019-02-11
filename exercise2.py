# Creating a good tip amount for a $55 dollar bill

tip_amount = 55 * 0.15

print(tip_amount)

total = 55 + tip_amount

print("This is the total for the bill ${}".format(total))

# Try adding a string and an integer with the + operator. What happens? Find a way to convert the integer into a string first and use print to print the result.
# by adding int() infront of the string it parses it to an int
price = 22 + int("3")
print(price)


# Try outputting the result of 45628 multiplied by 7839 in a sentence by using string interpolation.

print("45628 multiplied by 7839 equals {}".format(45628 * 7839))

# What's the value of the expression (10 < 20 and 30 < 20) or not(10 == 11)? Try figuring it out on your own before typing it in.
# output should be true because false or false = true

# the first expression will be false
print((10 < 20 and 30 < 20))
# this expression is also false
print(10 == 11)
# therefore this statement should be true because false or false = true
print((10 < 20 and 30 < 20) or not(10 == 11))
