def binary_search(list, target):
    first = 0               #Get the 1st element in the list
    last = len(list)-1      #Get the last element in the list

    while first <= last:
        midpoint = (first + last)//2 #calculate for the midpoint in the list

        if list[midpoint] == target:       #checks if midpoint is equal to the target
            return midpoint
        elif list[midpoint] < target:      #Reassigns the first value to the number after the midpoint and discard all the values before the midpoint in the list.
            first = midpoint + 1
        else:
            last = midpoint-1              #Midpoint will now be equal to the last value in the list

def verify(index):
	if index is not None:
		print("Target found at index ", index)
	else:
		print("Target not found in the list provided.")

numbers = [0,2,3,4,5,6,7,8]
result = binary_search(numbers, 3)
verify(result)

    
        