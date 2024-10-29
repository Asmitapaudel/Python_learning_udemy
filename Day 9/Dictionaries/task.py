programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
programming_dictionary["loop"]="A piece of code that you can easily call" # if key not in my_empty_dictionary then add otherwise edit
print(programming_dictionary["loop"])
print(programming_dictionary)
my_empty_dictionary = {}
print(my_empty_dictionary)

# loop through a dictionaries
for key in programming_dictionary:
    print(key) #only key
    print(programming_dictionary[key]) #only value of the key