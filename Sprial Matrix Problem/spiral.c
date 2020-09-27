#include <stdio.h>
#define r 4
#define c 4

void spiral(int m , int n , int a[r][c])
{
    int i,k = 0 ; l = 0;
    while(k < m && l < n)
    {
        for(i=l;i<n;++i)
        {
            printf("%d" , a[k][i]);
        }
        k++;
        for(i=k;i<m;++i)
        {
            printf("%d" , a[i][n-1]);
        }
        n--;
        if(k < m)
        {
            for(i = n - 1;i >= 1;--i)
            {
                printf("%d" , a[m-1][i]);
            }
            m--;
        }
        if(l < n)
        {
            for(i = m - 1;i >= k;--i)
            {
                printf("%d" , a[i][l]);
            }
            l++;
        }
    }
}
void main()
{
    int a[r][c] ={ {1,2,3,4},
                   {5,6,7,8},
                   {9,10,11,12},
                   {13,14,15,16} };
    spiral(r,c,a);
}
