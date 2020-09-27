#Python Program to find maximum no of A's
def optimal(n):
    if n<=6:
        return n
    maxi = 0
    for b in range(n-3,0,-1):
        curr = (n-b-1)*optimal(b)
        if curr > maxi:
            maxi = curr
    return maxi

n = int(input("Enter no of keystrokes :- "))
print("Maximum no with ",n,"keystrokes is ",optimal(n))
