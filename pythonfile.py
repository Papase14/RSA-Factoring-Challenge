#!/usr/bin/python3

import sys

def factorize(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"{n}={i}*{n//i}"
    return f"{n} is a prime number"

def main(file_path):
    with open(file_path, 'r') as file:
        numbers = file.read().splitlines()

    for number in numbers:
        result = factorize(int(number))
        print(result)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
