# a number is said to be a prime number, only and only if it is not divisible by
# all the numbers before it. In otherwords, it can only be divided by itself

# For a number to be considered a prime number, it has to have exactly 2
# positive divisors, that is, 1 and itself

# A prime number(or a prime) is a natural number greater than 1 that cannot be
# formed by multiplying two smaller natural numbers.
#
# A natural number greater than 1 that is not prime is called a composite number.
# For example, 5 is prime because the only ways of writing it as a product,
#  1 × 5 or 5 × 1, involve 5 itself.


# This solution is not optimised for numbers above 10,000
#  Its far too slow even for the best machines.


def is_prime(number):
    if number < 2:
        return False

    for x in range(2, number-1):
        if number % x == 0:
            return False

    return True
