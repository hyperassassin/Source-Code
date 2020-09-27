//Java Program to find maximum no of A's
import java.io.*; 
class keystroke 
{ 
	static int findoptimal(int N) 
	{ 
		if (N <= 6) 
			return N; 
		int max = 0; 
		int b; 
		for (b = N - 3; b >= 1; b--) 
		{ 
			int curr = (N - b - 1) * findoptimal(b); 
			if (curr > max) 
				max = curr; 
		} 
		return max; 
	}  
	public static void main(String[] args) 
	{ 
		int N=7; 
		System.out.println("Maximum No with " +N+" keystrokes is "+findoptimal(N)); 
	} 
}