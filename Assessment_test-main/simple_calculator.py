#Ask user to enter two numbers.
number1 = float(input("enter the first number: "))
number2 = float(input("enter the second number: "))

#Ask the user to choose an operation 
operation = input("add, subtract, multiply, divide")

#perform the selected operation and print the result
if operation == "add":
    result = number1 + number2
    print(f"the result of addition is: {result}")
