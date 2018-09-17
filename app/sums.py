def total_sum(numbers):
    total = 0

    index = 0
    while index < len(numbers):
        if isinstance(numbers[index], list):
            total += total_sum(numbers[index])
        else:
            total += numbers[index]

        index += 1
    return total


print(total_sum([1, 2, 7, 8, [5, 6, 10], 2, [6, 8]]))
