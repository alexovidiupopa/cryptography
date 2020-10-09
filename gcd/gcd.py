from copy import deepcopy
from timeit import default_timer
TESTS = 1

class BigInteger:
    def __init__(self, x):
        self.__read(x)

    def __str__(self) -> str:
        cpy = deepcopy(self)
        cpy.vec.reverse()
        result = ""
        for digit in self.vec:
            result+=str(digit)
        return result

    def __add__(self, other):
        result = BigInteger("0")
        result.vec = []
        carry = 0
        i = 0
        while i<len(self.vec) and i<len(other.vec):
            digit = self.vec[i] + other.vec[i] + carry
            result.vec.append(digit%10)
            carry = digit//10
            i+=1
        while i<len(self.vec):
            digit = self.vec[i] + carry
            result.vec.append(digit%10)
            carry = digit//10
            i+=1
        while i<len(other.vec):
            digit = other.vec[i] + carry
            result.vec.append(digit%10)
            carry = digit//10
            i+=1
        if carry:
            result.vec.append(carry)
        return result

    def __sub__(self, other):
        result = self
        i = 0
        while i < len(self.vec) and i < len(other.vec):
            result.vec[i] -= other.vec[i]
            if result.vec[i]<0:
                result.vec[i+1]-=1
                result.vec[i]+=10
            i+=1
        while result.vec[-1]==0:
            result.vec.pop()
        return result
    def __mul__(self, other):
        return None

    def __divmod__(self, other):
        return None, None

    def __gt__(self, other):
        if len(self.vec) > len(other.vec):
            return True
        if len(self.vec) < len(other.vec):
            return False
        for i in range (len(self.vec)-1,-1,-1):
            if self.vec[i] > other.vec[i]:
                return True
            elif self.vec[i] < other.vec[i]:
                return False
        return True

    def __ne__(self, other) :
        return self.vec != other.vec

    def __eq__(self, other):
        return self.vec == other.vec

    def __read(self, x:str):
        self.vec = []
        self.sign = 1
        for char in x:
            self.vec.append(ord(char)-ord('0'))
        self.vec.reverse()


def gcd_substract(x, y):
    if x == BigInteger("0"):
        return y
    if y == BigInteger("0"):
        return x
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x


def gcd_euclidean(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    while y:
        r = x % y
        x = y
        y = r
    return x


def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    d = 2
    while d*d<=x:
        if x % d == 0:
            return False
        d = d+2
    return True


def gcd_prime_factors(x, y):
    prime = 2
    gcd = 1
    while prime * prime <= x and prime * prime <= y:
        while x % prime == 0 and y % prime == 0:
            x = x / prime
            y = y / prime
            gcd = gcd * prime
        prime += 1
        while not is_prime(prime):
            prime += 1
    return gcd


def main():
    TESTS = [("18","12"),("30","11"),("4137523", "1227241"),("9427097151","2571923608"), ("737319582759902", "130030194834914")]
    for test in TESTS:
        print("Starting test a={},b={}".format(test[0],test[1]))
        start = default_timer()
        x = BigInteger(test[0])
        y = BigInteger(test[1])
        #gcd = gcd_euclidean(x, y)
        gcd = gcd_substract(x, y)
        #gcd = gcd_prime_factors(x, y)
        end = default_timer()
        print("Time elapsed {} seconds".format(end-start))
        print("Gcd is {}".format(gcd))


main()
