using System;
using System.Collections.Generic;

class positive_miss 
{
    static int positive(int []arr , int n)
    {
        int m = 1;
        HashSet<int> a = new HashSet<int>();
        for(int i=0;i<n;i++)
        {
            if(m < arr[i])
            {
                a.Add(arr[i]);
            }
            else if(m == arr[i])
            {
                m += 1;
                while(a.Contains(m))
                {
                    a.Remove(m);
                    m += 1;
                }
            }
        }
        return m;
    }
  public static void Main(String[]args) 
  {
      int []arr = {-4,-3,-2,-1,0,1,2,3,4,5,6,8};
      int n = arr.Length;
      Console.WriteLine("The First Positive Number is :- " + positive(arr,n));
      //Console.ReadLine();
  }
}