print("-------------------------")
print("Welcome to my calculator!")
print("-------------------------")
print()

again = True

while again:
    #The user chooses his values
    x = (input("Enter the first number here: "))
    y = (input("Enter the second number here: "))
    z = input("Select an operator of your choice [+, -, *, /]: ")

    #Checking the values you just entered
    if not (x.isdigit() and y.isdigit() and (z == "+" or z == "-" or z == "*" or z == "/")):
        #The data are not correct
        print("You entered incorrect data! Double check")
        continue;

    #Cast
    x = int(x)
    y = int(y)

    #Data are correct
    if z == "+":
        print("The result is:",x+y)
    if z == "-":
        print("The result is:",x-y)
    if z == "*":
        print("The result is:",x*y)
    if z == "/":
        print("The result is:",x/y)

    print("--------------------------")
    cont = input("Do you want to continue? (Type 'y' to do it)\n")
    again = cont == "y"
   
print("Calculator off, bye!")