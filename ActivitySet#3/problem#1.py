def largestArea(arr1, n, arr2, m):
	
	
	end = 0
	start = 0
	i = 0
	j = 0

	
	arr1.sort(reverse = False)

	
	arr2.sort(reverse = False)

	
	while (i < n and j < m):
		
		
		if (arr1[i] == arr2[j]):
			
			
			if (start == 0):
				start = arr1[i]
			else:
				
				
				end = arr1[i]
				
			i += 1
			j += 1

		
		elif (arr1[i] > arr2[j]):
			j += 1
		else:
			i += 1

	
	if (end == 0 or start == 0):
		return 0
	else:
		
		
		return (end - start)


if __name__ == '__main__':
	
	
	arr1 = [ 1, 2, 4 ]

	
	N = len(arr1)

	
	arr2 = [ 1, 3, 4 ]

	
	M = len(arr2)

	print(largestArea(arr1, N, arr2, M))