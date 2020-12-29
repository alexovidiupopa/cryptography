import random

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
CHUNK_LENGTH = 3
ALPHABET_LENGTH = len(ALPHABET)+1


def validate(message):
    for char in message:
        if char not in ALPHABET:
            return False
    return True
import random

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
CHUNK_LENGTH = 3
ALPHABET_LENGTH = len(ALPHABET)+1


def sieve(bound):
    ans = []
    marked = [False for _ in range(bound + 1)]
    for i in range(2, bound + 1):
        if not marked[i]:
            ans.append(i)
            for j in range(i + i, bound + 1, i):
                marked[j] = True
    return ans[10000:]

import random

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
CHUNK_LENGTH = 3
ALPHABET_LENGTH = len(ALPHABET)+1


def get_random_prime(bound):
    primes = sieve(bound)
    return random.choice(primes)

import random

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
CHUNK_LENGTH = 3
ALPHABET_LENGTH = len(ALPHABET)+1


def get_int_less_than(p):
    return random.randint(1, p - 2)

import random

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
CHUNK_LENGTH = 3
ALPHABET_LENGTH = len(ALPHABET)+1


def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def generators(n):
    gens = []
    for g in range(2, n):
        if gcd(g, n) == 1:
            gens.append(g)
    return gens


def get_random_generator(n):
    return random.choice(generators(n))


def modular_exp(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    # bit shifting is safer for large numbers, when possible
    while y > 0:
        if (y & 1) == 1:
            res = res * x % p
        y = y >> 1  # y = y//2
        x = x * x % p

    return res


def keys_generator():
    p = get_random_prime(10 ** 7)
    print("generated prime is=" + str(p))
    g = get_random_generator(p)
    print("generator g is=" + str(g))
    a = get_int_less_than(p)  # private key
    ga = modular_exp(g, a, p)
    print("g^a is=" + str(ga))
    public_key = (p, g, ga)
    return public_key, a

import random

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
CHUNK_LENGTH = 3
ALPHABET_LENGTH = len(ALPHABET)+1


def convert_text_to_digits(text):
    result = 0
    power = 1
    for char in reversed(text):
        result += (ALPHABET.find(char) + 1) * power
        power *= ALPHABET_LENGTH
    return result


def convert_digits_to_text(digits):
    text = ""
    while digits:
        text = ALPHABET[digits % ALPHABET_LENGTH - 1] + text
        digits = digits // ALPHABET_LENGTH
        
    return text

import random

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'
CHUNK_LENGTH = 3
ALPHABET_LENGTH = len(ALPHABET)+1


def get_int_less_than(p):
    return random.randint(1, p - 2)


def modular_exp(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    # bit shifting is safer for large numbers, when possible
    while y > 0:
        if (y & 1) == 1:
            res = res * x % p
        y = y >> 1  # y = y//2
        x = x * x % p

    return res


def generate_random_text():
    tests = []
    lengths = [i for i in range(5, 11)]
    for i in range(10):
        length = random.choice(lengths)
        message = ""
        for _ in range(length):
            message += random.choice(ALPHABET)
        tests.append(message)
    return tests


def test():
    test_cases = generate_random_text()
    print(test_cases)
    public_key, private_key = keys_generator()
    print("public key=" + str(public_key))
    print("private key=" + str(private_key))
    p = public_key[0]
    g = public_key[1]
    ga = public_key[2]
    a = private_key
    for test_message in test_cases:

        decrypted_text = ""
        chunks = [test_message[i:i + CHUNK_LENGTH] for i in range(0, len(test_message), CHUNK_LENGTH)]
        for c in chunks:
            m = convert_text_to_digits(c)

            k = get_int_less_than(p)
            alpha = modular_exp(g, k, p)
            beta = m * modular_exp(ga, k, p) % p

            decrypted_digits = modular_exp(alpha, p - 1 - a, p) * beta % p
            decrypted_text += convert_digits_to_text(decrypted_digits)

        print(test_message, decrypted_text)
        assert decrypted_text == test_message

    print("el gamal tests passed")


def main():
    import sys
    args = sys.argv[1:]
    initial_message = ""
    if not args:
        initial_message = "alex"
    elif args[0] == "-m":
        initial_message = " ".join(args[1:])
    elif args[0] == "-t":
        print("el gamal tests will be run")
        test()
        return

    print("message:" + initial_message)

    if not validate(initial_message):
        print("Invalid characters in input message. Please only use lowercase alphabet and spaces.")
        assert False

    public_key, private_key = keys_generator()
    print("public key=" + str(public_key))
    print("private key=" + str(private_key))
    p = public_key[0]
    g = public_key[1]
    ga = public_key[2]
    a = private_key

    decrypted_text = ""
    chunks = [initial_message[i:i + CHUNK_LENGTH] for i in range(0, len(initial_message), CHUNK_LENGTH)]
    for c in chunks:
        m = convert_text_to_digits(c)
        k = get_int_less_than(p)
        alpha = modular_exp(g, k, p)
        beta = m * modular_exp(ga, k, p) % p

        decrypted_digits = modular_exp(alpha, p - 1 - a, p) * beta % p
        decrypted_text += convert_digits_to_text(decrypted_digits)

    print("decrypted message:" + decrypted_text)
    assert decrypted_text == initial_message

main()

