def recurssive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2

    if list[midpoint] == target:
        return True
    else:
        if list[midpoint] < target:
            return recurssive_binary_search(list[midpoint+1:], target)
        else:
            return recurssive_binary_search(list[:midpoint], target)
        
def verify(index):
    print("Target found: ", index)

numbers = [1,2,3,4,5,6,7,8,9,10]
results = recurssive_binary_search(numbers, 6)
verify(results)

results = recurssive_binary_search(numbers, 12)
verify(results)