# dallin moore
# the algorithm is O(n) - it only has to loop through the list once, and there for increases in iterations linearly with the input 
# Prompts:
# write a function to compute the second largest number in an array without using any functions
# give me a variety of test cases for this problem to test the algorithm in a list of lists

lists = [
    # Basic case: Array with distinct numbers
    [3, 6, 2, 8, 4, 10],  # Expected output: 8

    # Array with duplicate numbers
    [10, 10, 8, 3, 5, 5, 2],  # Expected output: 8

    # Array with negative numbers
    [-5, -2, -8, -3, -10],  # Expected output: -3

    # Array with all negative numbers
    [-3, -6, -2, -8, -4, -10],  # Expected output: -3

    # Array with two elements
    [7, 4],  # Expected output: 4

    # Array with all identical elements
    [9, 9, 9, 9, 9],  # Expected output: 9
    [6]

]


array = [10,10,4,1,5,8,2,6]

def second_largest(array):
    try:
        largest = array[0]
        second_largest = array[1] 
    except:
        return "List of length 2 required."
    
    if second_largest>largest:
        second_largest, largest = largest, second_largest

    for num in array[2:]:
        if second_largest == largest:
            second_largest = num
        if num > largest:
            largest, second_largest = num, largest
        elif num > second_largest:
            second_largest = num
    return second_largest
    
for l in lists:
    print(second_largest(l))
