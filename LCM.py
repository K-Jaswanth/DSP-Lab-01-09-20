#L.C.M. of two numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Logic begins here
if(num1 > num2 ):
    greater= num1
else:
    greater= num2
while(True):
    if(greater % num1 == 0 and greater % num2 == 0):   
        lcm = greater
        break;
    greater += 1

#Dispaly result
print("The L.C.M is", lcm)

#My Info
print("K.Jaswanth sai - 121910313044")
