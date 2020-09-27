#include <stdio.h> 
int search(int mat[4][4], int n, int x) 
{ 
   int i=0,j=n-1;
   while(i < n && j >= 0)
   {
       if(mat[i][j] == x)
       {
           printf("\n Element Found at :- %d , %d",i,j);
           return 1;
       }
       if(mat[i][j] > x)
       {
           j--;
       }
       else
       {
           i++;
       }
   }
   printf("Element Not Found");
   return 0;
} 
int main() 
{ 
    int mat[4][4] = { 
        { 10, 20, 30, 40 }, 
        { 15, 25, 35, 45 }, 
        { 27, 29, 37, 48 }, 
        { 32, 33, 39, 50 }, 
    }; 
    search(mat, 4, 25); 
    return 0; 
}