
# Quick sorting algorithm 
# 
# Worst Case time complexity: O(n^2)
# Average time complexity: O(nlogn)
# 
# Picks a pivot, sorts greater or lower compared to pivot
# Recursively sorts the greater and lower lists
def quick_sort(values):
    
    length = len(values)
    
    # return the list if length is 1 or sets pivot 
    if length <= 1:
        return values
    else:
        pivot = values.pop()
    
    lower = []
    greater = []

    # add greater values to the greater list and lower values to the lower list
    for value in values:
        if value > pivot:
            greater.append(value)
        else:
            lower.append(value)

    # sorts the lower list and greater list
    # concatonates the sorted pivot points together, other pivot point return recurively 
    return quick_sort(lower) + [pivot] + quick_sort(greater)

print(quick_sort([3,8,5,9,7,8,5,6,3,1]))