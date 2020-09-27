#include <stdio.h>

void product(int arr[] ,int n)
{
    int i,temp = 1;
    int prod[n];
    if(n == 1)
    {
        printf("0");
        return;
    }
    for(int j=0;j<n;j++)
    {
        prod[j] = 1;
    }
    for(i=0;i<n;i++)
    {
        prod[i] = temp;
        temp = temp * arr[i];
    }
    temp = 1;
    for(i=n-1;i>=0;i--)
    {
        prod[i] = prod[i] * temp;
        temp = temp * arr[i];
    }
    for(i=0;i<n;i++)
    {
        printf("%d \t",prod[i]);
    }
    return;
}
void main()
{
    int arr[] = {1,2,3,4,5};
    int n = sizeof arr / sizeof arr[0];
    printf("Product Array :- ");
    product(arr,n);
    
}