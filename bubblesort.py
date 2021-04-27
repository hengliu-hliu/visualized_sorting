# Buuble sorting algorithm 
# 
# Worst Case time complexity: O(n^2)
# Average time complexity: O(n^2)
# 
# Compares two adjacent terms and orders them greatest to lower
# Repeats above comparison steping over one adjacent element, puts largest element last
# Loops through entire sequence until sorted
def bubble_sort(sequence):

    # index one less than length of sequence
    index_length = len(sequence) - 1
    
    sorted = False

    # loop while list is not sorted
    while not sorted:
        sorted = True

        # loops through list 
        for i in range(index_length):
            
            # checks if values at current position of list is greater or less than value at the next position
            if sequence[i] > sequence[i+1]:
                # if true, this loop not last loop, sets sorted to false
                sorted = False
                sequence[i] , sequence[i+1] = sequence[i+1], sequence[i]

    return(sequence)


print(bubble_sort([3,8,5,9,7,8,5,6,3,1]))