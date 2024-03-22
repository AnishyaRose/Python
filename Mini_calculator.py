Num1 = int(input("Number1:"))
Num2 = int(input("Number2:"))
operation = input("add/sub/mul/div:")
if(operation =="add"):
    sum = Num1 + Num2
    print("Sum is:",sum)
elif(operation == "sub"):
    sub = Num1 - Num2
    print("Sub is:",sub)
elif(operation =="mul"):
    mul = Num1 * Num2
    print("mul is:",mul)
elif(operation =="div"):
    div = Num1 % Num2
    print("div is:",div)
else:
    print("Invalid operation")