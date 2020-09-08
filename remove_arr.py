# Python code to remove duplicate elements 
print("Jaswanth sai - 121910313044")
n = int(input('enter the number of elements in the array: '))
print ('Enter the elements of the array')
arr1 = []
arr2 = []
#Taking the user input
for i in range(0,n):
    i =  int(input())
    arr1.append(i)
print(f'The original array = {arr1}')
# Deleting the repeated elements by using "not in" 
for i in arr1:
    if i not in arr2:
        arr2.append(i)

print(f'Array without the repeated elements = {arr2}')
