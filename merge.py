#Merge sort

def mergeSort(enter):
	
	if(len(enter)>1):
		half = len(enter)/2
		mergeSort(enter[:half])
		mergeSort(enter[half:])
		print (enter)


array = [3,4,2,8,6,9]
print ("unsorted array")
print(array)

print("\nstarted sorting\n")
mergeSort(array)
print("\nfinished sorting\n")
print("sorted array")
print(array)


print ("\n\ntesting\n")
A = [1,2,3,4,5,6]
B = A[:len(A)/2]
C = A[len(A)/2:]
D = B[:len(B)/2]
E = B[len(B)/2:]
print B
print C
print D
print E