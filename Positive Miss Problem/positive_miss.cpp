#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

int positive_miss(int arr[] , int n)
{
    int m = 1;
    set<int> a;
    for(int i=0;i<n;i++)
    {
        if(m < arr[i])
        {
            a.insert(arr[i]);
        }
        else if (m == arr[i])
        {
            m = m + 1;
            while(a.count(m))
            {
                a.erase(m);
                m = m + 1;
            }
        }
    }
    return m;
}
int main()
{
    int arr[] = {-4,-3,-2,-1,0,1,2,3,4,5,6,8};
    int n = sizeof(arr)/sizeof(arr[0]);
    cout << "The First Positive Number is :- "<<positive_miss(arr,n);
    return 0;
}