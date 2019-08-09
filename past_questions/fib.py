def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

calc = {}

def better_fib(n):
    if n <= 1:
        return n
    elif n-1 not in calc:
        calc[n-1] = better_fib(n-1)
        return better_fib(n-1) + better_fib(n-2)
    else:
        return calc[n-1] + better_fib(n-2)

if __name__ == '__main__':
    print(fib(5))
    print(better_fib(50))
