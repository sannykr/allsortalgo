def bubblesort(data):
    """Bubble sort algorithm for a python list """
    n = len(data)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data            


def insertionsort(data):
    """
    Insertion sort algorithm for a python list
    """	
    n = len(data)
    for i in range(1, n):
    	key = data[i]
    	j = i-1
    	while j >=0 and key < data[j]:
    		data[j+1] = data[j]
    		j -= 1
    	data[j+1] = key
    return data
    	

def mergesort(data):
    """merge sort algorithm for a python list """
    if len(data) > 1:
        mid = len(data)/2
     	left = data[:mid]
     	right = data[mid:]
     	mergesort(left)
        mergesort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
	        if left[i] < right[j]:
	            data[k] = left[i]
	            i += 1
	        else:
	            data[k] = right[j]
	            j += 1
	        k += 1
        while i < len(left):
            data[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            data[k] = right[j]
            j = j + 1
            k = k + 1     
    return data

 # def selectionsort(data):
 #     """
 #     selection sort algorithm for a python list
 #     """


 # def quicksort(data):
 #     """
 #     selection sort algorithn for a python list
 #     """

 # def heapsort(data):
 #     """
 #     heapsort implementation for a python list           