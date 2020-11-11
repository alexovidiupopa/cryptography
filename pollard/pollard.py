def gcd(x, y):
    while y:
        r = x % y
        x = y
        y = r
    return x

def funcall(f, val):
    coeff = f.replace('[','').replace(']','').split(',')
    s = 0
    for i in range(len(coeff)):
        s+=int(coeff[i])*(val**i)
    return s

def pollard(n, x0, f):
    x = [x0]
    j = 1
    while True:
        xj = funcall(f, x[-1]) % n
        x.append(xj)
        xj = funcall(f, x[-1]) % n
        x.append(xj)
        d = gcd(abs(x[2 * j] - x[j]), n)
        if 1 < d < n:
            return d
        elif d == n:
            return None
        j += 1

def pollardRunner(n, f):
    x0 = 2
    while True:
        result = pollard(n, x0, f)
        if result is not None:
            return result
        x0 += 1

import sys 

def main():
    n = 7031
    f = '[1,0,1]'
    params = sys.argv[1:]
    if len(params) == 4 and params[0] == "-n" and params[2] == "-f":
        n = int(params[1])
        f = params[3]
    elif len(params) == 2 and params[0] == "-n":
        n = int(params[1])
    print("Running Pollard with n={} and f={}".format(n, f))
    print(pollardRunner(n, f))


main()


