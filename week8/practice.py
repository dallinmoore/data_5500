import time

def sum_recursive(n):
    if n == 1: return 1
    return n + sum_recursive(n-1)

def sum_numbers(n):
    total = 0
    for i in range(1,1+n):
        total += i
    return total


start_time = time.time()
print(sum_recursive(250))
print("Elapsed Time:",time.time()-start_time)
start_time = time.time()
print(sum_numbers(250))
print("Elapsed Time:",time.time()-start_time)


def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)

print(factorial(5))
