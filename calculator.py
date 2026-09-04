num1= float(input("Enter the first number : "))
operation = input("choose an operation (+, -, *, / ) :")
num2= float(input("Enter the second number :"))



if operation == "+" : 
    print("Result: " , num1 + num2)

elif operation == "-":
    print("Result: " , num1 - num2)

elif operation =="*" :
    print("Result: " , num1 * num2)

elif operation == "/" :
    if num2 == 0 :
         print("you cannot divide by zero")
    else :
        print("Result: ", num1 / num2 )
       

else :
    print("invilid operation.")