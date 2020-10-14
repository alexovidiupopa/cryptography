from copy import deepcopy
from timeit import default_timer


class BigInteger:
    def __init__(self, x):
        self.__read(x)

    def __str__(self):
        cpy = deepcopy(self)
        cpy.vec.reverse()
        result = ""
        for digit in cpy.vec:
            result += str(digit)
        return result

    def __add__(self, other):
        result = BigInteger("0")
        result.vec = []
        carry = 0
        i = 0
        while i < len(self.vec) and i < len(other.vec):
            digit = self.vec[i] + other.vec[i] + carry
            result.vec.append(digit % 10)
            carry = digit // 10
            i += 1
        while i < len(self.vec):
            digit = self.vec[i] + carry
            result.vec.append(digit % 10)
            carry = digit // 10
            i += 1
        while i < len(other.vec):
            digit = other.vec[i] + carry
            result.vec.append(digit % 10)
            carry = digit // 10
            i += 1
        if carry:
            result.vec.append(carry)

        return result

    def __sub__(self, other):
        result = deepcopy(self)
        i = 0
        carry = 0
        while i < len(other.vec) or carry:
            if i < len(other.vec):
                result.vec[i] = result.vec[i] - other.vec[i] - carry
            else:
                result.vec[i] -= carry
            if result.vec[i] < 0:
                carry = 1
                result.vec[i] += 10
            else:
                carry = 0
            i += 1

        while result.vec[-1] == 0 and len(result.vec) > 1:
            result.vec.pop()

        return result

    def __mul__(self, other):
        result = BigInteger("0")
        result.vec = [0] * (len(self.vec) + len(other.vec))
        i1 = 0

        for digit1 in self.vec:
            carry = 0
            i2 = 0
            for digit2 in other.vec:
                summ = digit1 * digit2 + result.vec[i1 + i2] + carry
                carry = summ // 10
                result.vec[i1 + i2] = summ % 10
                i2 += 1

            if carry > 0:
                result.vec[i1 + i2] += carry
            i1 += 1

        while result.vec[-1] == 0 and len(result.vec) > 1:
            result.vec.pop()

        return result

    def __floordiv__(self, other):
        cnt = BigInteger("0")
        cpy = deepcopy(self)
        while cpy > other:
            cpy = cpy - other
            cnt = cnt + BigInteger("1")
        if cpy == other:
            cnt = cnt + BigInteger("1")
        return cnt

    def __mod__(self, other):
        divd = deepcopy(self) // deepcopy(other)
        return self - (divd * other)

    def __gt__(self, other):
        if len(self.vec) > len(other.vec):
            return True
        if len(self.vec) < len(other.vec):
            return False
        for i in range(len(self.vec) - 1, -1, -1):
            if self.vec[i] > other.vec[i]:
                return True
            elif self.vec[i] < other.vec[i]:
                return False
        return True

    def __lt__(self, other):
        return not self > other

    def __le__(self, other):
        return self == other or self < other

    def __ne__(self, other):
        return self.vec != other.vec

    def __eq__(self, other):
        return self.vec == other.vec

    def __read(self, x):
        self.vec = []
        for char in x:
            self.vec.append(ord(char) - ord('0'))
        self.vec.reverse()



def gcd_subtract(x, y):
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
    zero = BigInteger("0")
    if x == zero:
        return y
    if y == zero:
        return x
    while y != zero:
        r = x % y
        x = y
        y = r
    return x


def gcd_basic(x, y):
    if x > y:
        min = y
    else:
        min = x
    zero = BigInteger("0")
    if x % min == zero and y % min == zero:
        return min
    i = min // BigInteger("2")
    while i >= BigInteger("2"):
        if x % i == zero and y % i == zero:
            return i
        i = i - BigInteger("1")
    return BigInteger("1")


def main():
    tests = [("18", "12"), ("30", "11"), ("4137524", "1227244"), ("9427097152", "25719608"),
             ("737319582759902", "130030194834914"), ("2183651267535555", "85765424658761005"),
             ("9876542316549876542361978", "4478954814555567000102"),
             ("73498174143914", "13245125243635476"),
             ("98653287946511232000007777845156", "987987546213134654876546540480984"),
             ("1285497153615581795397428674243824621432424572421437927424242424258923463862",
              "21312314614141414143426463464574000000789798987893213215446546549808900024")]
    for test in tests:
        print("\n\nStarting test a={},b={}".format(test[0], test[1]))
        start = default_timer()
        x = BigInteger(test[0])
        y = BigInteger(test[1])

        #gcd = gcd_euclidean(x, y)
        #gcd = gcd_subtract(x, y)
        gcd = gcd_basic(x,y)

        end = default_timer()
        print("Time elapsed {} seconds".format(end - start))
        print("Gcd is {}\n\n".format(gcd))


main()
