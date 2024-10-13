#Functionality of Addition
def add(num1,num2):
    add = num1 + num2
    return add
#FUnctionality of Subtraction
def sub(num1,num2):
    sub = num1 - num2
    return sub
#FUnctionality of Multiplication
def mul(num1,num2):
    mul = num1 * num2
    return mul
#FUnctionality of Division
def div(num1,num2):
    if num2 == 0:
        return  "Can't Divide with Zero!!"
    else:
        return num1 / num2

#using a while loop to constantly ask the for operation selection 
#until it exits
while True:
    print("""
Select Operation:
1.Addition(+)
2.Subtraction(-)
3.Multiplication(*)
4.Division(/)
5.Exit
""")
#Asking the Operation choice from user
    choice = input("Enter Operation Choice (1/2/3/4/5): ")
#If user selects 5 it will exit the program 
    if choice == '5':
        print("Exiting the Calculator. Bye!!")
        break
#If the choice not valid then it will exit the program
    if choice not in  ['1','2','3','4','5']:
        print("Invalid Operation")
        break
    else:    
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter Second number: "))

#Performing the operation user choosed
    if choice == '1':
        print(f"Addition of {n1} + {n2}: {add(n1,n2)}")
    elif choice == '2':
        print(f"Subtraction of {n1} - {n2}: {sub(n1,n2)}")
    elif choice == '3':
        print(f"Multiplication of {n1} * {n2}: {mul(n1,n2)}")
    elif choice == '4':
        print(f"Division of {n1} / {n2}: {div(n1,n2)}")
    else:
        print("Invalid Number")

