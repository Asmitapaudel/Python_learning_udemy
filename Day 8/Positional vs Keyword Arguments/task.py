# Functions with input
# Create a function with multiple inputs
def greet_with_name(greeting,name):
    print(f"{greeting} {name}")
    print(f"How do you do {name}?")


greet_with_name("Hello","Jack Bauer")


# Call the greet_with() function using keyword arguments.
def greet_with(greeting,name):
    print(f"{greeting} {name}")
greet_with(name="Jack",greeting="Hello")
