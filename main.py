from art import logo
print(logo)
def add(n1, n2):
    """ Adds two numbers"""
    return n1 + n2
def sub(n1,n2):
    """ Subtracts two numbers"""
    return n1-n2
def multiply(n1,n2):
    """ Multiplies two number"""
    return n1 * n2
def division(n1,n2):
    """ Divides two numbers"""
    return n1/n2
operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : division
}
def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number? : "))

    while should_accumulate:
        for key in operations:
            print(key)
        operation = input("Pick an operation: " )
        num2 = float(input("What's the next number? : "))
        result = operations[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {result}")

        choice=input(f"Type 'y' to continue calculating with {result} , or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()