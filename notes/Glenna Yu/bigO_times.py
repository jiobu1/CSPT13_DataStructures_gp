import datetime
from random import random
import matplotlib.pyplot as plt

def time_func(f, n:int):
    arr = [random() * 10] * n
    start = datetime.datetime.now()
    f(arr)
    total_time = datetime.datetime.now() - start
    print(str(n) + "\t" + str(total_time))
    return total_time.total_seconds()

def compare_funcs(funcs, input_sizes):
    all_runtimes = {}
    for f in funcs:
        print(f"-----, {f.__name__}, ----")
        function_runtimes = []
        for n in input_sizes:
            function_runtimes.append((n, time_func(f, n)))
        all_runtimes[f.__name__] = function_runtimes
    return all_runtimes

def plot_runtimes(runtimes, max_y=None):
    print(runtimes)
    all_ys = []
    for name, runtime_pairs in runtimes.items():
        xs, ys = zip(*runtime_pairs)
        plt.plot(xs, ys, label = name)
        all_ys.append(ys)
    if not max_y:
        max_y = max([max(ys) for ys in all_ys])
    plt.xlabel('input sizes')
    plt.ylabel('runtime')
    axes = plt.gca()
    axes.set_ylim([0, max_y])
    plt.show()

from typing import List
from time import sleep

def constant1(nums:List):
    return nums[0]

# runtimes = compare_funcs([constant1], input_sizes=[10, 100, 1000, 10000, 100000])
# plot_runtimes(runtimes)

def linear1(nums:List):
    s = 0
    for n in nums:
        s += n

# runtimes = compare_funcs([constant1, linear1], input_sizes=[10**2, 10**3, 10**4, 10**5, 10**6])
# plot_runtimes(runtimes)

def quadratic1(nums: List):
    combinations = []
    for i in nums:
        for j in nums:
            combinations.append((i, j))

# runtimes = compare_funcs([constant1, linear1, quadratic1], input_sizes=[10**2, 10**3, 10**4, 10**5])
runtimes = compare_funcs([constant1, linear1, quadratic1], input_sizes=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
plot_runtimes(runtimes)


# What's the complexity fo the following code?

# Overall O(2n^2 + n + 3) --> O(n^2)
def foo(n):
    a = 5 # O(1)
    b = 6
    s = 0
    # the code in the for loops wil be run 2*n*n times --> 0(n^2)
    for i in range(n): # runs for n iterations
        for j in range(2*n): # this loop runs for 2*n iterations --> / O(n)
            for k in range(n):# --> this would make it O(n^3) but still represented as O(n^2) --> quadratic
                s += (i, j) # O(1)

    for k in range(n):
        w = a * k # O(n)

foo(10)

# Look for what has the highest impact and that will determine the Big O 0f the algorithm

def bar(n):
    i = 0 # constant
    while i < n:
        i++ # constant
        print("Walalbies") # constant
        j = 5000 # constant
        for x range(j):
            print("something")
#Linear because this not a nested loop but it does increase as the size of the loop increases

def bar2(n):
    # Overall: O(n^2)
    i = 0 # constant
    while i < n: # runs for n iterations --> O(n)
        i++ # constant
        print("Walalbies") # constant
        j = 0 # constant
        while j <n/2: # will run for n/2 iterations --> O(n)
            print("Kangaroos") # constant
            j++  # constant

