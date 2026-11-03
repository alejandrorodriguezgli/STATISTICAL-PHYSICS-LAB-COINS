"""Unit tests for src/combinatorics.py."""

import math

import pytest

from src.combinatorics import omega, log_omega, distribution, probability
# We define the tests we're going to run. 
# First we check the distribution for N = 7, which should match the known values from the report.
def test_table_n7():
    """Distribution for N = 7 matches the table in the report."""
    assert distribution(7) == [1, 7, 21, 35, 35, 21, 7, 1]

# Next, we check if our omega function matches Python's built-in binomial coefficient for various values of N and k.
# The @pytest.mark.parametrize decorator allows us to run the same test with different values of N.
@pytest.mark.parametrize("N", [1, 5, 20, 100, 500])
def test_omega_matches_math_comb(N):
    """Our omega agrees with Python's built-in binomial coefficient."""
    for k in range(N + 1):
        assert omega(N, k) == math.comb(N, k)

# We also check if the sum of all microstates for a given N equals 2^N, which is the total number of possible outcomes when flipping N coins.
@pytest.mark.parametrize("N", [0, 1, 7, 50, 100])
def test_total_microstates(N):
    """Summing Omega over all k gives 2^N microstates."""
    assert sum(distribution(N)) == 2 ** N

# After that, we check the symmetry property of the omega function, which states that the number of microstates with k heads is equal to the number of microstates with N-k heads.
def test_symmetry():
    """k heads and k tails have the same number of microstates."""
    for k in range(101):
        assert omega(100, k) == omega(100, 100 - k)

# Next, we check that impossible values of k (less than 0 or greater than N) return 0 microstates and negative infinity for the logarithm of microstates.
def test_impossible_k():
    """Impossible numbers of heads give 0 microstates (ln -> -inf)."""
    assert omega(10, -1) == 0
    assert omega(10, 11) == 0
    assert log_omega(10, 11) == float("-inf")

# In addition, we check that the log-space result from log_omega matches the logarithm of the exact integer result from omega for various values of N and k.
# Floats from log_omega have tiny rounding errors, so we use pytest.approx to allow for a small relative error of 1e-10 in the comparison.
@pytest.mark.parametrize("N", [10, 100, 1000])
def test_log_omega_matches_exact(N):
    """log-space result agrees with the log of the exact integer."""
    for k in range(N + 1):
        assert log_omega(N, k) == pytest.approx(math.log(omega(N, k)), rel=1e-10)

# Finally, we check that all probabilities for a given N add up to 1 (some number of heads always happens).
@pytest.mark.parametrize("N", [1, 20, 100, 1000])
def test_probabilities_sum_to_one(N):
    """P_k summed over all k equals 1."""
    assert sum(probability(N, k) for k in range(N + 1)) == pytest.approx(1.0)