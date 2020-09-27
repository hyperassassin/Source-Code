//C Program to find maximum no of A's
#include <stdio.h>
static int optimal(int n)
{
    if(n<=6)
    {
        return n;
    }
    int max = 0,b;
    for(b = n-3;b>=1;b--)
    {
        int curr = (n-b-1)*optimal(b);
        if(curr > max)
        {
            max = curr;
        }
    }
    return max;
}
int main()
{
    int n = 7;
    printf("Maximum no with %d keystrokes is %d",n,optimal(n));
}
