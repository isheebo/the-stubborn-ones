def powers(base, exponent):
    if exponent == 0:
        return 1

    if exponent < 0:
        return 1 / base * powers(base, exponent + 1)
    return base * powers(base, exponent - 1)
