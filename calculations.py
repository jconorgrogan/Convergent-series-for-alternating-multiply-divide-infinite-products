import math

def is_prime(num: int) -> bool:
    """Check if 'num' is a prime (simple trial-division)."""
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    limit = int(math.isqrt(num)) + 1
    for i in range(5, limit, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True

def get_first_n_primes(n: int) -> list[int]:
    """Generate a list of the first n primes."""
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

def euler_factor(p: int, s: float) -> float:
    """
    The Euler factor for the prime p in zeta(s):
      F(p) = (p^s) / (p^s - 1).
    """
    p_s = p**s
    return p_s / (p_s - 1.0)

def alt_multiply_divide(n: int, s: float) -> float:
    """
    Compute:
       F_1 * F_2 / F_3 * F_4 / F_5 * F_6 / F_7 ...
    up to n primes, where F_i is the Euler factor for
    the i-th prime.

    Returns the final floating-point value.
    """
    primes = get_first_n_primes(n)
    result = 1.0

    for i, p in enumerate(primes, start=1):
        factor = euler_factor(p, s)

        # Decide whether to multiply or divide this factor:
        #  - i=1,2 => multiply
        #  - i>=3: if i is odd => divide, if i is even => multiply
        if i == 1 or i == 2:
            # multiply
            result *= factor
            op = '*'
        else:
            if i % 2 == 1:
                # odd => divide
                result /= factor
                op = '/'
            else:
                # even => multiply
                result *= factor
                op = '*'

        print(f"Step {i:2d}: prime={p:2d}, factor={factor:.6f}, {op} => partial={result:.6f}")

    return result


if __name__ == "__main__":
    # Example usage:
    #  n = number of primes
    #  s = exponent for zeta(s)
    #
    # Change them as you like:
    n = 10000
    s = 1.0

    final_val = alt_multiply_divide(n, s)
    print("\nFinal result for first", n, "primes at s =", s, "=>", final_val)
