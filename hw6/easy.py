# dallin moore
# the algorithm is O(n) - it only loops once for every instance of the array

array = [3,1,4,1,5,9,2,6]

def calc_sum(array):
    total = 0
    for i in array:
        total += i
    return total

print(calc_sum(array))