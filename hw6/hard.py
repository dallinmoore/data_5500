# dallin moore
# the algorithm is O(n) - it only has to loop through the list once, and there for increases in iterations linearly with the input 
# ai prompt:
# now provide me a list of lists for a function solving this question: Write a function that takes an array of integers as input and returns the maximum difference between any two numbers in the array.

test_cases = [
    # Basic case: Array with distinct numbers
    [3, 6, 2, 8, 4, 77],  # Expected output: 8

    # Array with duplicate numbers
    [10, 10, 8, 3, 5, 5, 2],  # Expected output: 8

    # Array with negative numbers
    [-5, -2, -8, -3, -10],  # Expected output: 8

    # Array with all negative numbers
    [-3, -6, -2, -8, -4, -10],  # Expected output: 8

    # Array with one element
    [7],  # Expected output: 0

    # Array with two elements
    [7, 4],  # Expected output: 3

    # Array with all identical elements
    [9, 9, 9, 9, 9],  # Expected output: 0

    # Large array with randomly generated integers
    # Expected output: the maximum difference between any two numbers in the array
    # Not specifically provided as it's a large randomly generated array
]


def max_difference(array):
    try:
        min_num = array[0]
        max_num = array[1]
    except:
        return 0
    if min_num > max_num:
        min_num, max_num = max_num, min_num
    for num in array[2:]:
        min_num = num if num < min_num else min_num
        max_num = num if num > max_num else max_num
    return max_num - min_num
    
for l in test_cases:
    print(max_difference(l))