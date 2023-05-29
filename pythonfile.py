#!/usr/bin/python3

import sys
import time

def pollards_rho(n):
    if n % 2 == 0:
        return 2

    x = 2
    y = 2
    d = 1

    def f(x):
        return (x ** 2 + 1) % n

    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    return d

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def factorize(n):
    factors = []
    while n > 1:
        if is_prime(n):
            factors.append(n)
            break
        d = pollards_rho(n)
        factors.append(d)
        n //= d
    factors.sort()
    return f"{n}={factors[0]}*{n//factors[0]}"

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        try:
            result = factorize(int(number))
            print(result)
        except ValueError:
            print(f"Invalid input: {number}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()
    main(file_path)
    end_time = time.time()

    elapsed_time = end_time - start_time

    print(f"\nreal    {elapsed_time//60:.0f}m{elapsed_time%60:.3f}s")
    print(f"user    {time.process_time():.3f}s")
    print(f"sys     {elapsed_time - time.process_time():.3f}s")
