def factorial(n):
    if n < 0:
        return 0  # just a devised fail-safe return in this case

    if n == 0:
        return 1
    return n * factorial(n-1)
