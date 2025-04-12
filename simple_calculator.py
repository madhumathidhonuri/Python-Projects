import math
from statistics import mean,mode,median
calculate='''
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulous
6. Exponentiation
7. Floor Division
8. Square of a number
9. Cube of a number
10. Factorial
11. Mean
12. Mode
13. Median
14. Square Root of a number
15. Cube Root of a number
'''
print(calculate)

def Addition(nums):
    result=0
    for i in nums:
        result+=i
    print("Addition of given numbers is: ",result)
    
def Subtraction(nums):
    result=nums[0]
    for i in nums[1:]:
        result-=i
    print("Subtraction of given numbers is: ",result)
    
def Multiplication(nums):
    result=nums[0]
    for i in nums[1:]:
        result*=i
    print("Multiplication of given numbers is: ",result)
    
def Division(nums):
    try:
        result=nums[0]
        for i in nums[1:]:
            if i==0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result/=i
        print("Division of given numbers is: ",result)
    except ZeroDivisionError as e:
        print(e)
    
def Modulous(nums):
    try:
        result=nums[0]
        for i in nums[1:]:
            if i==0:
                raise ZeroDivisionError("Cannot calculate modulus by zero.")
            result%=i
        print("Modulous of given numbers is: ",result)
    except ZeroDivisionError as e:
        print(e)  

def Exponentiation(nums):
    result=nums[0]
    for i in nums[1:]:
        result**=i
    print("Exponentiation of given numbers is: ",result)
    
def FloorDivision(nums):
    result=nums[0]
    for i in nums[1:]:
        result//=i
    print("Floor division of given numbers is: ",result)
    
def SquareOfNumber(nums):
    for i in nums:
        print(f"Square of {i} is {i**2}")
    
def CubeOfNumber(nums):
    for i in nums:
        print(f"Cube of {i} is {i**3}")
        
def Factorial(nums):
    if nums[0]<0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {nums[0]} is {math.factorial(nums[0])}")
        
def Mean(nums):
    print("Mean of given numbers is: ",mean(nums))
    
def Mode(nums):
    try:
        print("Mode of given numbers is: ", mode(nums))
    except:
        print("No unique mode found or invalid data.")

def Median(nums):
    print("Median of given numbers is: ",median(nums))
    
def SquareRoot(nums):
    for i in nums:
        print(f"Square root of {i} is {math.sqrt(i):.2f}")
        
def CubeRoot(nums):
    for i in nums:
        print(f"Cube root of {i} is {i**(1/3):.2f}")
    
while True:
    option=int(input("Enter the option: "))
    nums=list(map(int,input("Enter numbers separated by spaces: ").split()))
    if option==1:
        Addition(nums)
    elif option==2:
        Subtraction(nums)
    elif option==3:
        Multiplication(nums)
    elif option==4:
        Division(nums)
    elif option==5:
        Modulous(nums)
    elif option==6:
        Exponentiation(nums)
    elif option==7:
        FloorDivision(nums)
    elif option==8:
        SquareOfNumber(nums)
    elif option==9:
        CubeOfNumber(nums)
    elif option==10:
        Factorial(nums)
    elif option==11:
        Mean(nums)
    elif option==12:
        Mode(nums)
    elif option==13:
        Median(nums)
    elif option==14:
        SquareRoot(nums)
    elif option==15:
        CubeRoot(nums)
    else:
        print("Invalid Option")
    cont = input("Do you want to perform another operation? (yes/no): ").lower()
    if cont != 'yes':
        print("Thank you for using the calculator!")
        break