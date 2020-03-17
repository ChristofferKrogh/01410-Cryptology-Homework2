import math
import numpy as np

def isPrime(candidate, primes):
    """
    Prime number test by trial division
    """
    for prime in primes:
        if prime > int(math.sqrt(candidate)):
            break
        if candidate % prime == 0:
            return False
    return True

def millerRabin(m):
    """
    The Miller-Rabin primality test
    m is the number that we check for primality

    The implementation follows Figure 4.4 in the book
    """
    # Base cases
    if m == 2:
        return True
    if m % 2 == 0 or m == 1: 
        return False

    # Step 1
    t = m - 1
    s = 0
    while t % 2 == 0:
        t = int(t / 2)
        s += 1

    # Step 2
    b = np.random.randint(1, m)

    # Step 3
    y = (b ** t) % m # TODO: maybe we should compute this more efficiently

    # Step 4
    if y % m == 1:
        return True
    
    # Step 5
    for _ in range(s):
        if y % m == -1 or y % m == m - 1:
            return True
        else:
            y = (y ** 2) % m # TODO: maybe we should compute this more efficiently
    
    # Step 6
    return False

def isPrimeMR(m, k):
    """
    Check the primality of m using k iterations of the Miller-Rabin algorithm
    """
    for _ in range(k):
        if not millerRabin(m):
            return False
    
    return True
    



# Exercise 2.2.a
print("\nExercise 2.2.a")
start = 25
end = 35000
primes = []

# Note: we check whether even numbers are primes even though all except 2 obviously aren't
for num in range(2, start):
    if isPrime(num, primes):
        primes.append(num)

num_primes_less_start = len(primes)

for num in range(start, end):
    if isPrime(num, primes):
        primes.append(num)

num_primes_in_interval = len(primes) - num_primes_less_start

print(f"Number of primes in the interval from {start} to {end} is: {num_primes_in_interval}")
print(f"Compare this to fact 4.3.1: {end} / log({end}) - {start} / log({start}) = {end / math.log(end) - start / math.log(start)}")


# Exercise 2.2.b
print("\nExercise 2.2.b")
# implement Miller-Rabin with k iterations
for i in range(14):
    print(f"{i} - {isPrimeMR(i, 3)}")

# Exercise 2.2.c
print("\nExercise 2.2.c")
num_primes_results = []
for k in range(1, 3):
    num_primes_MR = 0
    for m in range(start, end):
        if isPrimeMR(m, k):
            num_primes_MR += 1

    num_primes_results.append(num_primes_MR)

print(num_primes_results)
