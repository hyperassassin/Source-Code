class product_array
{
void product(int arr[] , int n)
{
	int i,temp=1;
	int prod[] = new int[n];
	if(n == 1)
	{
		System.out.println("0");
		return;
	}
	for(int j=0;j<n;j++)
	{
		prod[j] = 1;
	}
	for(i=0;i<n;i++)
	{
		prod[i] = temp;
		temp *= arr[i];
	}
	temp = 1;
	for(i=n-1;i>=0;i--)
	{
		prod[i] *= temp;
		temp *= arr[i];
	}
	for(i=0;i<n;i++)
	{
		System.out.print(prod[i] + " ");
	}
	return;
}
public static void main(String[]args)
{
product_array p = new product_array();
int arr[] = {1,2,3,4,5};
int n = arr.length;
System.out.println("Array :- ");
p.product(arr,n);
}
}