#To Find the Samllest among the three numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

#Logic begins here 
smallest = num1
if (num2 < num1) and (num2 < num3):
    smallest = num2
elif (num3 < num1):
    smallest = num3

#Display Result
print("The smallest number is", smallest)

#My Info
print("K.Jaswanth sai - 121910313044")
