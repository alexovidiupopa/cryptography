from math import sqrt, floor


def fermat(n, b=5):
    result = None
    k = 1
    while result is None:
        t0 = floor(sqrt(k * n))
        for i in range(1, b + 1):
            t = t0 + i
            potential = t ** 2 - k * n
            if sqrt(potential) == floor(sqrt(potential)):
                result = k, t, sqrt(potential)
        k += 1
    return result


def main():
    n = 141467
    k, t, s = fermat(n)
    first = t - s
    second = t + s
    if first % k == 0:
        first /= k
    else:
        second /= k
    print(str(n) + "=" + str(int(first)) + "*" + str(int(second)))


main()
