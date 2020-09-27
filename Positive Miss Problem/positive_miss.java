import java.util.*;

class positive_miss
{
static int positive(int arr[], int n)
{
int m = 1;
HashSet<Integer> a = new HashSet<Integer>();
for(int i=0;i<n;i++)
{
if(m < arr[i])
{
a.add(arr[i]);
}
else if(m == arr[i])
{
m = m + 1;
while(a.contains(m))
{
a.remove(m);
m += 1;
}
}
}
return m;
}
public static void main(String[]args)
{
int arr[] = {-4,-3,-2,-1,0,1,2,3,4,5,6,8};
int n = arr.length;
System.out.println("The First Positive Number is :- " + positive(arr,n));
}
}
