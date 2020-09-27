def product_array(arr,n):
    if(n == 1):
        print(0)
        return
    i , temp = 1 , 1
    prod = [1 for i in range(n)]
    for i in range(n):
        prod[i] = temp
        temp = temp * arr[i]
    temp = 1
    for i in range(n-1,-1,-1):
        prod[i] = prod[i]*temp
        temp = temp * arr[i]
    for i in range(n):
        print(prod[i] , end = " ")
    return
    
arr = [1,2,3,4,5]
n = len(arr)
print("Product Array :- ")
product_array(arr,n)
     
