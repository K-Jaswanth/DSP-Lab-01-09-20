#Implement linear search
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['j','a','s','w','a','n','t','h']
x = 'n'
print("element found at index "+str(linearsearch(arr,x)))
