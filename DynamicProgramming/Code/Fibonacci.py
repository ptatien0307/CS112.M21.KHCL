def fibo_recursion(n):
    if n <= 1:
        return n
    return fibo_recursion(n - 1) + fibo_recursion(n - 2)

def fibo_memoize(n, lookup):
    if n <= 1:
        lookup[n] = n
 
    if lookup[n] is None:
        lookup[n] = fibo_memoize(n-1, lookup) + fibo_memoize(n-2, lookup)
 
    return lookup[n]

def fibo_tabulate(n):
    f = [0] * (n + 1)
 
    f[1] = 1
 
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]

def main():
    import time
    # n = 38
    n = 900
    # Recursion
    # start = time.time()
    # x = fibo_recursion(n)
    # end = time.time()
    # print(f'{x} - time: {end-start}')

    # Top - Down
    start = time.time()
    lookup = [None] * 10001
    x = fibo_memoize(n, lookup)
    end = time.time()
    print(f'{x} - time: {end-start}')

    # Bottom - Up
    start = time.time()
    x = fibo_tabulate(n)
    end = time.time()
    print(f'{x} - time: {end-start}')
    
main()
    