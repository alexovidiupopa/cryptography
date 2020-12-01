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
        x.append(funcall(f, x[-1]) % n) # tortoise
        x.append(funcall(f, x[-1]) % n) # hare
        d = gcd(abs(x[2 * j] - x[j]), n)
        if 1 < d < n:
            return d
        elif d == n:
            return None
        j += 1


from math import sqrt
def prime(x):
    if x<2 or (x>2 and x%2==0):
        return False 
    for d in range(3, int(sqrt(x)+1),2):
        if x%d==0:
            return False 
    return True
def pollardRunner(n, f):
    if prime(n):
        return None, None
    x0 = 2
    result = pollard(n, x0, f)
    while result is None:
        x0+=1
        result = pollard(n, x0, f)

    return result, x0-1

def testBigNumber():
    n=10967535067
    f='[1,0,1]'
    factors = [104723, 104729]
    return pollardRunner(n, f)[0] in factors

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
        x.append(funcall(f, x[-1]) % n) # tortoise
        x.append(funcall(f, x[-1]) % n) # hare
        d = gcd(abs(x[2 * j] - x[j]), n)
        if 1 < d < n:
            return d
        elif d == n:
            return None
        j += 1


from math import sqrt
def prime(x):
    if x<2 or (x>2 and x%2==0):
        return False 
    for d in range(3, int(sqrt(x)+1),2):
        if x%d==0:
            return False 
    return True
def pollardRunner(n, f):
    if prime(n):
        return None, None
    x0 = 2
    result = pollard(n, x0, f)
    while result is None:
        x0+=1
        result = pollard(n, x0, f)

    return result, x0-1
TESTS = {
        50262:[2, 3, 6, 8377, 16754, 25131], 
        50294:[2, 25147], 
        50303: [11, 17, 187, 269, 2959, 4573], 
        50589: [3, 7, 9, 11, 21, 33, 63, 73, 77, 99, 219, 231, 511, 657, 693, 803, 1533, 2409, 4599, 5621, 7227, 16863], 
        50595: [3, 5, 15, 3373, 10119, 16865],
        50638: [2, 7, 14, 3617, 7234, 25319],
        50645: [5, 7, 35, 1447, 7235, 10129],
        50807: [23, 47, 1081, 2209],
        50900: [2, 4, 5, 10, 20, 25, 50, 100, 509, 1018, 2036, 2545, 5090, 10180, 12725, 25450],
        50967: [3, 7, 9, 21, 63, 809, 2427, 5663, 7281, 16989]
        }
def testSmallNumbers():
    f='[1,0,1]' 
    result = True
    for k in TESTS.keys():
        result = result and (pollardRunner(k,f)[0] in TESTS[k])
    return result
   
      
def runTests():
    assert testBigNumber() and testSmallNumbers()
    print("TESTS PASSED")
import matplotlib.pylab as plt
from math import log
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
        x.append(funcall(f, x[-1]) % n) # tortoise
        x.append(funcall(f, x[-1]) % n) # hare
        d = gcd(abs(x[2 * j] - x[j]), n)
        if 1 < d < n:
            return d
        elif d == n:
            return None
        j += 1


from math import sqrt
def prime(x):
    if x<2 or (x>2 and x%2==0):
        return False 
    for d in range(3, int(sqrt(x)+1),2):
        if x%d==0:
            return False 
    return True
def pollardRunner(n, f):
    if prime(n):
        return None, None
    x0 = 2
    result = pollard(n, x0, f)
    while result is None:
        x0+=1
        result = pollard(n, x0, f)

    return result, x0-1

def plot(x=1000, y=100000, f='[1,0,1]'):
    data = {}
    for i in range(x,y): 
        factor, it = pollardRunner(i, f)
        if factor is not None: 
            data[it] = int(log(factor, 2))
    result = data.items()
    xAxis = [pair[0] for pair in result]
    yAxis = [pair[1] for pair in result]
    plt.title('iterations v factor size (bits)')
    plt.xlabel('iterations')
    plt.ylabel('sizeof factor (bits)')
    plt.scatter(xAxis,yAxis, color='red')
    plt.show()
import sys 

def main():
    n = 7031
    f = '[1,0,1]'
    args = sys.argv[1:]
    if len(args) == 4 and args[0] == "-nr" and args[2] == "-func":
        n = int(args[1])
        f = args[3]
    elif len(args) == 2 and args[0] == "-nr":
        n = int(args[1])
    print("Running Pollard with n={} and f={}".format(n, f))
    result, iters = pollardRunner(n, f)
    print("Result is {}, reached in {} iterations".format(result, iters))


main()
runTests()
plot()
