import math

def euclidsGcd(a, b):
    a, b = b, a % b
    if b == 0:
        return a
    else:
        return euclidsGcd(a, b)

def main():
    # Exercise 2.1.1

    # Exercise 2.1.2
    # Check that gcd(e, phi(n)) = 1
    print("\nExercise 2.1.2")
    e, p, q = 3, 911, 491
    phi = (p - 1) * (q - 1)
    if euclidsGcd(e, phi) == 1:
        print(f"{e} is an allowed exponent!")
    else:
        print(f"{e} is NOT an allowed exponent!")


if __name__ == '__main__':
    main()