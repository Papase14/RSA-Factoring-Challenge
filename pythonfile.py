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
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3

    i = 5
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        while n % (i + 2) == 0:
            factors.append(i + 2)
            n //= i + 2
        i += 6

    if n > 1:
        factors.append(n)

    factors.sort()
    return f"{n}={factors[0]}*{n//factors[0]}"

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
    user_time = time.process_time()
    system_time = (elapsed_time - user_time) * -1

    print(f"\nreal    {elapsed_time//60:.0f}m{elapsed_time%60:.3f}s")
    print(f"user    {user_time//60:.0f}m{user_time%60:.3f}s")
    print(f"sys     {system_time//60:.0f}m{system_time%60:.3f}s")
