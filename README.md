# test-code-review
def second_largest(nums):
    largest = 0
    second = 0

    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second:
            second = n

    return second


print(second_largest([-10, -5, -2, -1]))
print(second_largest([5, 5, 3]))
print(second_largest([42]))
