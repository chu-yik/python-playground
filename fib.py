def fib(n, lookup):

    if n == 0 or n == 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

    return lookup[n]
#end fib

def main():
    n = 34
    lookup = [None]*101 # empty array

    print('Fibonacci Number is {0}'.format(fib(n, lookup)))
#end main

if __name__ == "__main__":
    main()