#Perfect Number

print("Jaswanth sai - 121910313044")


a = int(input("Enter the number:"))
s = 0
for i in range(1,a):
    if(a% i == 0):
        s = s+i

#Logic begins
    if(a == s):
        print(a,'is a perfect number')
    else:
        print(a,'is not a perfect number')
