#Quick sort

def quicksort(enter):
	doQuicksort(enter,0,len(enter)-1)

#proces in the quick sort
def doQuicksort(enter,start,end):

	if(start< end): 

		pivot = partition(enter,start,end)		
		doQuicksort(enter,start,pivot-1)				#break into two from the pivot
		doQuicksort(enter,pivot+1,end)

	return enter
#function to partitioning the array

def partition(alist,low,high):

	right = high
	left = low+1	
	pivot_item = alist[low]			#selecting the 1st element as the pivot


	while(left < right):

		while alist[left]<= pivot_item:			#until getting an element bigger than pivot
			left= left+1

		while alist[right]>pivot_item:			#until getting an element smaller than pivot
			right = right-1

		if(left < right):							#after finishing , then swap the left and right elements
			swap(alist,left,right)
			
	alist[low] = alist[right]					#assign the value to 1st element since that is lower than pivot
	alist[right] = pivot_item					#assigning the pivot to the right

	return right								#return the position of the current pivot

#function to swap the elements
def swap(alist,i,j):

	alist[i],alist[j]=alist[j],alist[i]

array = [3,4,2,8,6]
print ("unsorted array")
print(array)

print("\nstarted sorting\n")
quicksort(array)
print("\nfinished sorting\n")
print("sorted array")
print(array)