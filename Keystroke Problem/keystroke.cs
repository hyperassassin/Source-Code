//C# Program to find maximum no of A's
using System;
class keystroke 
{
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
    public static void Main() 
    {
        int n = 7;
        Console.WriteLine("Maximum no with "+n+" keystroke is "+optimal(n));
    }
}