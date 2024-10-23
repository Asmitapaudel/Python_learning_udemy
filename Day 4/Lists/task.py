states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[0])#Accessing 1st Items in Lists
print(states_of_america[-1])#Accessing last Items in Lists


fruits = ["Cherry", "Apple", "Pear"]
# Modifying Items
fruits[0] = "Orange"# ['Orange', 'Apple', 'Pear']

#Adding Items
fruits.append("Banana")
fruits.extend(["Grapes", "Banana", "Pear"])# adding a bunch of data to the list

print(fruits)


# https://docs.python.org/3/tutorial/datastructures.html