# CHALLENGE 1: TWIN PRIMES


""" A twin prime is a prime number that is either 2 less or 2 more than another prime number—for example, either member of the twin prime pair (41, 43). 
In other words, a twin prime is a prime that has a prime gap of two. Sometimes the term twin prime is used for a pair of twin primes; 
an alternative name for this is prime twin or prime pair. (from wiki https://en.wikipedia.org/wiki/Twin_prime)
Your mission, should you choose to accept it, is to write a function that counts the number of sets of twin primes from 1 to n.
If n is wrapped by twin primes (n-1 == prime && n+1 == prime) then that should also count even though n+1 is outside the range.

Ex n = 10

Twin Primes are (3,5) (5,7) so your function should return 2! """

import numpy


def find_factors(x):
    return len([num for num in list(range(1, x)) if x % num == 0])


def twin_prime(n):
    num_list = list(range(2, n+2))
    fac_list = [find_factors(num) for num in num_list]
    fac_dict = dict(zip(num_list, fac_list))
    primes = []
    for key, value in fac_dict.items():
        if value <= 1:
            primes.append(key)

    dif = list(numpy.diff(primes))

    prime_dif_dict = dict(zip(primes, dif))

    twin_primes = []

    for key, value in prime_dif_dict.items():
        if value == 2:
            twin_primes.append(key)

    return len(twin_primes)


# print(find_factors())
print(twin_prime(12))
# should return 2

# print(twin_prime(12))
# should return 3


# find all the prime numbers in a given range
