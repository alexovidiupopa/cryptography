import math
import random
from math import sqrt
import sys

characters = ' abcdefghijklmnopqrstuvwxyz'
max_length = 2


def sieve(bound):
    ans = []
    marked = [False for _ in range(bound + 1)]
    for i in range(2, bound + 1):
        if not marked[i]:
            ans.append(i)
            for j in range(i + i, bound + 1, i):
                marked[j] = True
    return ans


def gcd(a,b):
    while b:
        r = a % b
        a = b
        b = r
    return a


def getRandomPrime(bound):
    primes = sieve(bound)
    return random.choice(primes)


def generators(n):
    gens = []
    for g in range(2, n):
        if gcd(g, n) == 1:
            gens.append(g)
    return gens


def getRandomGenerator(n):
    return random.choice(generators(n))


def getRandomIntegerLessThan(p):
    return random.randint(1, p - 2)


# Modular exponentiation
def power(x, y, p):
    res = 1  #
    x = x % p
    if x == 0:
        return 0

    while y > 0:
        if (y & 1) == 1:
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


def messageToDigits(text):
    result = 0
    pow = 1
    for letter in reversed(text):
        result += characters.find(letter) * pow
        pow *= len(characters)
    return result


def digitsToMessage(digits):
    text = ""
    for i in range(len(str(digits))):
        text = characters[digits % len(characters)] + text
        digits = digits // len(characters)
    return text.strip()


def test():
    pass


def main():
    args = sys.argv[1:]
    message = ""
    if not args:
        message = "alex"
    elif args[0] == "-m":
        message = " ".join(args[1:])
    elif args[0] == "-t":
        test()
        return

    print(message)
    p = getRandomPrime(10 ** 7)
    print(p)
    g = getRandomGenerator(p)
    a = getRandomIntegerLessThan(p)
    ga = power(g, a, p)
    publicKey = (p, g, ga)
    m = messageToDigits(message)
    print(m)
    k = getRandomIntegerLessThan(p)
    alpha = power(g, k, p)
    beta = m * power(ga, k, p) % p
    ciphertext = (alpha, beta)

    decryptedDigits = power(alpha, p - 1 - a, p) * beta % p
    decryptedMessage = digitsToMessage(decryptedDigits)

    print(decryptedMessage)
    assert decryptedMessage == message


main()
