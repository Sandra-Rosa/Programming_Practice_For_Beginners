# Simple calculator just taking assigning and if else statements for getting four basic operations such as Addition,Substraction,Multiplication and Division.
# Disadvantage:only two numbers can be operated.
# we can increase the number of inputs by little changes in the code
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# The user's inputs for the numbers and the operators
# Asks the operator user needs
Operator = input('Enter operator: ')
# Asks the number user need to operate
num1 = float(input('Enter your first number: '))
num2 = float(input('Enter your second number: '))

# if Operator is (+ | - | * | /) then  print out number 1 (+ | - | * | /) number 2
if Operator == '+':
    print(num1 + num2)
elif Operator == '-':
    print(num1 - num2)
elif Operator == '/':
    print(num1 / num2)
elif Operator == '*':
    print(num1 * num2)

# if the user didn't put an operator
else:
    print('Not a valid operator') 
