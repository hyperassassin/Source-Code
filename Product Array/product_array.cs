using System;
class product_array 
{
    static void product(int[] arr, int n)
    {
        int i,temp = 1;
        int[] prod = new int[n];
        if(n == 1)
        {
            Console.WriteLine("0");
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
            Console.Write(prod[i] +" ");
        }
        return;
    }
  public static void Main() 
  {
      int[] arr = {1,2,3,4,5};
      int n = arr.Length;
      Console.WriteLine("Product Array :- ");
      product(arr,n);
  }
}