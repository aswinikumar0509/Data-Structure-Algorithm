def bucketSort(arr, noOfBuckets):
	max_ele = max(arr)
	min_ele = min(arr)


	rnge = (max_ele - min_ele) / noOfBuckets

	temp = []


	for i in range(noOfBuckets):
		temp.append([])


	for i in range(len(arr)):
		diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)


		if(diff == 0 and arr[i] != min_ele):
			temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])

		else:
			temp[int((arr[i] - min_ele) / rnge)].append(arr[i])


	for i in range(len(temp)):
		if len(temp[i]) != 0:
			temp[i].sort()

	k = 0
	for lst in temp:
		if lst:
			for i in lst:
				arr[k] = i
				k = k+1


# Driver Code
arr = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
noOfBuckets = 5
bucketSort(arr, noOfBuckets)
print("Sorted array: ", arr)