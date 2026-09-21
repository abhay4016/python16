
def find_max():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return max(num1, num2) 


print("The maximum of the two numbers is:", find_max()) 






def find_max_without_max():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if num1 > num2:
        return num1
    else:
        return num2
