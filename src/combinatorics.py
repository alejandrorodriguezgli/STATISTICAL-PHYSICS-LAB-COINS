"""Combinatorics for a system of N coins (two-state elements).

Omega(N, k) is the number of microstates with exactly k heads.
"""
# First we import the math module, which provides mathematical functions and constants.
import math

# Now we define the function omega, which calculates the exact number of microstates with k heads among N coins.
# This function returns an integer value representing the number of microstates.
def omega(N: int, k: int) -> int:
   
    """Exact number of microstates with k heads among N coins.

    Uses the product formula
        C(N, k) = prod_{i=1}^{k} (N + 1 - i) / i
    so the huge factorials N!, k! and (N-k)! are never computed.
    """
    # First we check if k is less than 0 or greater than N.
    # If so, we return 0, as there are no valid microstates in that case.
    if k < 0 or k > N:
        return 0
    # We write k = min(k, N - k) since there are only two outcomes for each coin (heads or tails), and the number of microstates with k heads is the same as the number of microstates with N-k heads.
    # This reduces the number of loop steps needed to compute the result.
    k = min(k, N - k)  # symmetry C(N, k) = C(N, N-k): fewer loop steps
    result = 1
    # Now we use a loop to compute the product formula for C(N, k). 
    # We iterate from 1 to k (inclusive) and update the result by multiplying it with (N + 1 - i) and dividing it by i.
    # This gives omega(N, k) without computing large factorials directly.
    for i in range(1, k + 1):
        result = result * (N + 1 - i) // i
    return result

# Now we define the function log_omega, which calculates the natural logarithm of Omega(N, k) using the log-gamma function.
# This is useful for very large values of N, as it avoids overflow issues that can occur with direct factorial calculations.
def log_omega(N: int, k: int) -> float:
    """Natural logarithm of Omega(N, k), computed with log-gamma.

    Since Gamma(n + 1) = n!,
        ln C(N, k) = lnGamma(N+1) - lnGamma(k+1) - lnGamma(N-k+1).
    Never overflows, so it works for very large N.
    """
    # For impossible k there are 0 microstates, and the logarithm of 0 is negative infinity.
    # Therefore, if k is less than 0 or greater than N, we return negative infinity.
    if k < 0 or k > N:
        return float("-inf")
    return math.lgamma(N + 1) - math.lgamma(k + 1) - math.lgamma(N - k + 1) 
