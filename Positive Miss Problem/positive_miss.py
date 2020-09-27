#Finding The Positive Missing Number

def findpositive(arr,n):
    m = 1
    a = []
    for i in range(n):
        if(m < arr[i]):
            a.append(arr[i])
        elif(m == arr[i]):
            m += 1
            while(a.count(m)):
                a.remove(m)
                m += 1
    return m

arr = [-4,-3,-2,-1,0,2,3,4,5,6,8]
n = len(arr)
print("The First Positive Number is :- " , findpositive(arr,n))
  
