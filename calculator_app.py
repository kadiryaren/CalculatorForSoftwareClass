# ---------  Calculator App Zero Division Error Scenario  ---------

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if(b == 0):
        return "Zero Division Error B can't be zero"
    return a/b



print("Select operation.")
while(True):
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    operation = input("5 for exit \nEnter operation: ")
    if(operation == "5"):
        break
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    
    

    if(operation == "1"):
        print("Result : ",add(n1,n2))
    elif(operation == "2"):
        print("Result : ",subtract(n1,n2))
    elif(operation == "3"):
        print("Result : ",multiply(n1,n2))
    elif(operation == "4"):
        print("Result : ",divide(n1,n2))
    elif(operation == "5"):
        exit()
    
