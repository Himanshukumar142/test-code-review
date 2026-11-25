# test-code-review
def calculate_positive_average(numbers, count_offset=0):
    total = 0
    count = 0

    for i in range(len(numbers)):
        num = numbers[i]
        if num > 0:
            total += num
            count += 1

    # Bug 1: ZeroDivisionError if there are no positive numbers (or if count + count_offset == 0)
    average = total / (count + count_offset)

    # Bug 2: Mutating a default argument list if used in a helper/cache pattern,
    # or off-by-one / type issues in formatting
    return f"Average of {count} numbers is: {average:.2f}"


def get_top_k(items, k):
    # Bug 3: Sorts in-place, mutating the caller's original list unexpectedly
    items.sort(reverse=True)
    # Bug 4: If k <= 0, items[:-k] or items[:k] behaves unexpectedly when k is negative
    return items[:k]


scores = [10, -5, 20, 0, -2]
print(calculate_positive_average(scores, count_offset=-2))
print("Top 2:", get_top_k(scores, -1))
print("Original scores after get_top_k:", scores)
