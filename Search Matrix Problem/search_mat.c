using System;
class search_matrix 
{
    static void search(int[,]mat , int n ,int x)
    {
        int i=0,j=n-1;
        while(i < n && j >= 0)
        {
            if(mat[i,j] == x)
            {
                Console.WriteLine("\n Element Found at :- "+i+","+j);
                return;
            }
            if(mat[i,j] > x)
            {
                j--;
            }
            else
            { 
                i++;
            }
        }
        Console.WriteLine("\n Element Not Found");
        return;
    }
public static void Main() 
{
    int[,]mat = {{10, 20, 30, 40}, 
			     {15, 25, 35, 45}, 
			     {27, 29, 37, 48}, 
			     {31, 33, 39, 50}};
	search(mat,4,29);
}
}