from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    first_number = float(input("Enter first number?: "))
    should_accumulated=True
    while should_accumulated:
        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("Enter second number?: "))
        value=operation[operation_symbol](first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {value}")

        option=input(f"Type 'y' to continue calculating with {value} ,or type 'n' to start a new calculation: ").lower()
        if option=="y":
            option = 'y'
            first_number =float(value)
        elif option=="n":
            should_accumulated=False
            print("\n"*100)
            calculator()

calculator()