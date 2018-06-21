# myFirstVariable = 'Hello World!'  # global variable because its outside the function
#
#
# def main():
#     print('Hi world')
#
#
# main()
#
#
# def hello_world(string):
#     print(string)
#
#
# hello_world(myFirstVariable)


def add(num1, num2):
    '''Returns num1 plus num2'''
    return num1 + num2


def sub(num1, num2):
    '''Returns num1 minus num2'''
    return num1 - num2


def mul(num1, num2):
    '''Returns num1 times num2'''
    return num1 * num2


def divide(num1, num2):
    '''returns num1 divided by num2'''
    return num1 / num2


def main():
    operation = input("What would you like to do (+, -, *, /): ")
    if (operation != '+' and operation != '-' and operation != '*' and operation != '/'):
        # Invalid operation
        print("Please enter a valid operation.")
    else:
        # Valid operation
        var1 = int(input('Please enter first number: '))
        var2 = int(input('Please enter your second number: '))
        if (operation == '+'):
            print(add(var1, var2))
        elif (operation == '-'):
            print(sub(var1, var2))
        elif (operation == '*'):
            print(mul(var1, var2))
        else:
            print(divide(var1, var2))


main()
