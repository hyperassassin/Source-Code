# Python program to search an element in row-wise and column-wise sorted matrix 
def search_matrix(mat, n, x): 
	i = 0 
	j = n - 1
	while ( i < n and j >= 0 ): 
		if (mat[i][j] == x ): 
			print("Element found at :-","(",i,",",j,")") 
			return 1
		if (mat[i][j] > x ): 
			j -= 1
		else: 
			i += 1
	print("Element not found") 
	return 0
# Driver Code 
mat = [ [10, 20, 30, 40], 
              [15, 25, 35, 45],
              [27, 29, 37, 48],
              [31, 33, 39, 50] ] 
search_matrix(mat,4, 31)
