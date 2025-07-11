#!/usr/bin/env python3
"""
Crypto Toolkit - A beginner-friendly Python script to work with large numbers
and basic cryptographic operations using Python's built-in big integer support.

Author: Efren Rios
GitHub: https://github.com/5354er/Crypto
"""

import math

# --------------------------------------------
# 1. Modular Exponentiation (Efficient for RSA)
# --------------------------------------------
def mod_exp(base, exponent, modulus):
    """Efficiently computes (base^exponent) % modulus using Python's pow()."""
    return pow(base, exponent, modulus)

# --------------------------------------------
# 2. Greatest Common Divisor
# --------------------------------------------
def gcd(a, b):
    """Returns the greatest common divisor of a and b."""
    return math.gcd(a, b)

# --------------------------------------------
# 3. Extended Euclidean Algorithm
# --------------------------------------------
def extended_gcd(a, b):
    """Returns (gcd, x, y) such that a*x + b*y = gcd."""
    if a == 0:
        return b, 0, 1
    else:
        gcd_, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_, x, y

# --------------------------------------------
# 4. Modular Inverse
# --------------------------------------------
def mod_inverse(a, m):
    """Finds the modular inverse of a under modulus m."""
    gcd_, x, _ = extended_gcd(a, m)
    if gcd_ != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

# --------------------------------------------
# 5. Primality Test (Miller-Rabin)
# --------------------------------------------
import random

def is_probable_prime(n, k=5):
    """Checks if a number is probably prime using the Miller-Rabin test."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# --------------------------------------------
# 6. Generate Large Prime Number
# --------------------------------------------
def generate_large_prime(bits=512):
    """Generates a large prime number of specified bit length."""
    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << bits - 1) | 1  # ensure it's odd and of correct bit size
        if is_probable_prime(candidate):
            return candidate

#---------------------------------------------------------
# 7. XOR operator
#------------------------------------------------------------------

def xor_binary(a_str, b_str):
    """Performs bitwise XOR on two binary strings."""
    a = int(a_str, 2)
    b = int(b_str, 2)
    result = a ^ b
    return format(result, 'b').zfill(max(len(a_str), len(b_str)))

# --------------------------------------------
# Example Usage (if run directly)
# --------------------------------------------
if __name__ == "__main__":
    print("Crypto Toolkit Demo:")
    a = 7
    b = 128
    m = 19

    print(f"mod_exp({a}, {b}, {m}) =", mod_exp(a, b, m))
    print(f"gcd({a}, {m}) =", gcd(a, m))
    print(f"mod_inverse({a}, {m}) =", mod_inverse(a, m))

    prime = generate_large_prime(bits=256)
    print(f"Generated 256-bit prime: {prime}")
