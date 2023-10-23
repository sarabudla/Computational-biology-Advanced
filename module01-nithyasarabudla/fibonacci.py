# 1: population, which takes a day (integer, n, between 1 and 10000) and
# a reproduction rate (integer, k, between 1 and 10000) and returns the population size at day n.
# Then, create an if __name__ == "__main__" block. That block should allow the user to pass a day and reproduction rate.
# Then, it should print the population size at the given day.

def population(n, k):
    """population, which takes a day (integer, n, between 1 and 10000) and
    a reproduction rate (integer, k, between 1 and 10000) and returns the population size at day n."""
    pop = [0] * (n + 1)
    pop[0] = 1
    pop[1] = 1
    for i in range(2, n + 1):
        pop[i] = pop[i - 1] + pop[i - 2] * k
    # print(pop)
    return pop[n - 1]


if __name__ == "__main__":
    import sys

    days = int(sys.argv[1])
    reproduction_rate = int(sys.argv[2])

    print(population(days, reproduction_rate))
