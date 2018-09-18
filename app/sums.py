def recursive_sum(numbers):
    total = 0

    for index in range(len(numbers)):
        if isinstance(numbers[index], list):
            total += recursive_sum(numbers[index])
        else:
            total += numbers[index]
    return total
