#!/usr/bin/python3

import sys
import time

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

def factorize_rsa(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and is_prime(i) and is_prime(n//i):
            return f"{n}={i}*{n//i}"
    return f"No factorization found within the time limit."

def main(file_path):
    with open(file_path, 'r') as file:
        number = int(file.readline().strip())

    result = factorize_rsa(number)
    print(result)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()
    main(file_path)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(f"\nreal    {elapsed_time//60:.0f}m{elapsed_time%60:.3f}s")
