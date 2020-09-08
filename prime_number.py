#Prime numbers upto a limit

print("Jaswanth sai - 121910313044")


lower = int(input("Enter the lower limit:"))
higher = int(input("Enter the higher limit:"))

#logic begins here

for a in range(lower,higher):
    if a>1:
        for i in range(2,a):
            if(a%i==0):

                break

            else:

                print(a)
