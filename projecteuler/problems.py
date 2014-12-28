import datetime
import math

__author__ = 'markns'


def multiples(num, limit):
    return [num * n for n in range(1, limit / num + 1)]


def is_factor(x, y):
    if y % x == 0:
        return True
    return False


def prime_factors(num):
    fctrs = []
    for p in primes(limit=int(math.sqrt(num))):
        if is_factor(p, num):
            fctrs.append(p)
            sub = prime_factors(num / p)
            if sub:
                fctrs.extend(sub)
                break
            else:
                fctrs.append(num / p)
    return fctrs


def factors(num):
    fctrs = []
    for x in range(1, num / 2):
        if is_factor(x, num):
            if x > num / x:
                break
            fctrs.append((x, num / x))
    return fctrs


def fibonacci(limit):
    fib = [1, 2]
    while sum(fib[-2:]) < limit:
        fib.append(sum(fib[-2:]))
    return fib


def primes(limit=1000):
    # Based on Sieve of Erastothenes

    # Increment by one for zero indexing
    bitarr = [1] * (limit + 1)
    for i in range(2, limit):
        if bitarr[i]:
            for mul in multiples(i, limit)[1:]:
                bitarr[mul] = 0
    return [x for x, y in enumerate(bitarr) if bitarr[x] and x > 1]


def problem1():
    # If we list all the natural numbers below 10 that are multiples
    # of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    #
    # Find the sum of all the multiples of 3 or 5 below 1000.

    muls3 = multiples(3, 999)
    muls5 = multiples(5, 999)

    print sum(set(muls3).union(muls5))


def problem2():
    # Each new term in the Fibonacci sequence is generated by adding
    # the previous two terms. By starting with 1 and 2, the first 10
    # terms will be:
    #
    # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
    #
    # By considering the terms in the Fibonacci sequence whose values
    # do not exceed four million, find the sum of the even-valued terms.
    print sum([x for x in fibonacci(4000000) if x % 2 == 0])


def problem3():
    # The prime factors of 13195 are 5, 7, 13 and 29.
    # What is the largest prime factor of the number 600851475143 ?
    y = 600851475143
    print datetime.datetime.now()
    print prime_factors(y)
    print datetime.datetime.now()


def make_palindromes(start, end):
    palindromes = []
    for x in range(start, end):
        a = x / 1
        b = x / 10
        c = x / 100
        print x, a, b, c
        break
    pass


def problem4():
    make_palindromes(100, 999)
    # print factors(90)


# problem1()
# problem2()
# problem3()
problem4()

# roots = []
# product = 1
# x = 2
# number = input("number?: ")
# y = number
# while product != number:
# while (y % x == 0):
# roots.append(x)
# y /= x
# product *= roots[-1]
# x += 1
# print roots