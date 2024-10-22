
# Fix the len() function so it has no more warnings or errors. e.g. len(12345)

len("12345")

# Write out 4 type checks to print all 4 data types

string = "Hello"
integer = 123
floating_point = 123.34
false = False

print(type(string))
print(type(integer))
print(type(floating_point))
print(type(false))


 # Make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))

print("Number of letters in your name: " +str( len(input("Enter your name"))))