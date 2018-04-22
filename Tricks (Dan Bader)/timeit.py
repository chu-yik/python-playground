# measure execution time by timeit
# for small piece of code

# !!!
# Run the following in terminal:
# !!!
import timeit

timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# >>> ~ 0.24

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# >>> ~ 0.2

timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# >>> ~ 0.16
