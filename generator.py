__author__ = 'admin'

# Basic implementation
def my_big_sum(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(sum(my_big_sum(10000000)))

# Generator implementation
def my_big_sum(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(my_big_sum(10000000)))