
import math
from src.combinatorics import omega, probability

kB = 1.380649e-23


# probabilidad entre dos valores de k
def cumulative_probability(N, k1, k2):
    P_total = 0

    for k in range(k1, k2 + 1):
        P_total = P_total + probability(N, k)

    return P_total


# diferencia de entropia entre dos macroestados
def entropy_change(N, k1, k2):
    omega1 = omega(N, k1)
    omega2 = omega(N, k2)

    S1 = kB * math.log(omega1)
    S2 = kB * math.log(omega2)

    delta_S = S1 - S2

    return delta_S


# calculations for Part 2 (a-g)
if __name__ == "__main__":

    # Team values
    M = 4 / (1/46 + 1/13 + 1/28 + 1/6)

    # nearest even integer
    N = 114

    print("M =", M)
    print("N =", N)

    # Part a: probability of 30 heads
    print("a)", probability(N, 30))

    # Part b: probability of N/2 heads
    print("b)", probability(N, N//2))

    # Part c: between N/2 - 10 and N/2 + 10 heads
    print("c)", cumulative_probability(N, N//2 - 10, N//2 + 10))

    # Part d: between N/2 - 20 and N/2 + 20 tails
    print("d)", cumulative_probability(N, N//2 - 20, N//2 + 20))

    # Part e: entropy change
    print("e)", entropy_change(N, N//2 + 25, N//2), "J/K")

    # Part f: entropy change
    print("f)", entropy_change(N, N//2 + 10, N//2), "J/K")

    # Part g: entropy change
    print("g)", entropy_change(N, N//2, 20), "J/K")

# =============================================================================
# PART 2 (h)-(k): thermodynamic interpretation and the large-N limit (Member 4)
# =============================================================================
# These functions reuse log_omega and probability from combinatorics.py.
# We always work with logarithms because the numbers involved (2^N, 1/P_8, ...)
# are far too large to be stored as normal floats.
import math

from src.combinatorics import log_omega, omega

# Constants used to convert seconds into more intuitive time units.
SECONDS_PER_YEAR = 3.15576e7      # one Julian year in seconds
AGE_OF_UNIVERSE_S = 4.35e17       # about 13.8 thousand million years in seconds


# (h) Waiting time to obtain a highly ordered state.
# Each second we toss all N coins once. Every toss is an independent trial with
# success probability P_k, so the number of tosses until the first success follows
# a geometric distribution, whose mean is 1 / P_k.
# The result is returned as log10 of the time, because the time itself is huge.
def log10_waiting_time(N: int, k: int = 8) -> float:
    """log10 of the mean waiting time (in seconds) to obtain exactly k heads,
    tossing the N coins once per second:  t = 1 / P_k = 2^N / Omega(N, k)."""
    # ln t = ln(2^N) - ln Omega(N, k) = N ln 2 - ln Omega(N, k); divide by ln 10 for log10.
    return (N * math.log(2) - log_omega(N, k)) / math.log(10)


def waiting_time_summary(N: int, k: int = 8) -> dict[str, float]:
    """Waiting time for k heads expressed in seconds, years and ages of the Universe
    (all as base-10 logarithms)."""
    log10_t = log10_waiting_time(N, k)
    return {
        "log10_P": -log10_t,                                         # log10 of P_k
        "log10_seconds": log10_t,
        "log10_years": log10_t - math.log10(SECONDS_PER_YEAR),
        "log10_universe_ages": log10_t - math.log10(AGE_OF_UNIVERSE_S),
    }


# (i) Likelihood ratio between the most probable macrostate and N/2 +- 10 heads.
# P(N/2) / P(N/2 + d) = Omega(N, N/2) / Omega(N, N/2 + d), because the 2^N cancels.
# By symmetry Omega(N, N/2 + d) = Omega(N, N/2 - d), so "+" and "-" give the same ratio.
# If N is odd, N/2 is not an integer: we use N // 2 (k = (N-1)/2 and (N+1)/2 are
# equally probable and both are the maximum).
def likelihood_ratio(N: int, d: int = 10) -> float:
    """How many times more likely is k = N/2 than k = N/2 + d."""
    half = N // 2
    return math.exp(log_omega(N, half) - log_omega(N, half + d))


def likelihood_ratio_exact(N: int, d: int = 10) -> float:
    """Same ratio with exact integers (only for moderate N), used to check the log version."""
    half = N // 2
    return omega(N, half) / omega(N, half + d)


# (j) Second Law: probability of a spontaneous entropy decrease.
# Since S = k_B ln Omega, the ratio of probabilities of two macrostates is
#   P(k1) / P(k2) = Omega(k1) / Omega(k2) = exp(Delta S / k_B).
# So a state with lower entropy is not forbidden, just exponentially unlikely.
def relative_probability_from_entropy(delta_S_over_kB: float) -> float:
    """P(final)/P(initial) = exp(Delta S / k_B) for a change of entropy Delta S."""
    return math.exp(delta_S_over_kB)


# (k) Large N limit, N ~ 1e23.
# Here log_omega with math.lgamma is NOT accurate anymore: lgamma(1e23) ~ 5e24, and a
# float only keeps ~16 significant digits, so subtracting two such numbers destroys
# the small result we want. We therefore use two stable approximations instead.

def log_omega_small_k(N: float, k: int) -> float:
    """Stable ln Omega(N, k) when k is small compared with N (e.g. k = 8, 20, 30):
        Omega = N (N-1) ... (N-k+1) / k!
        ln Omega = k ln N + sum_j ln(1 - j/N) - ln k!
    log1p(x) = ln(1 + x) is accurate even when x is tiny."""
    return k * math.log(N) + sum(math.log1p(-j / N) for j in range(k)) - math.lgamma(k + 1)


def log_omega_gaussian(N: float, x: float) -> float:
    """Stirling (Gaussian) approximation of ln Omega(N, N/2 + x), valid for |x| << N:
        ln Omega ~ N ln 2 - (1/2) ln(pi N / 2) - 2 x^2 / N."""
    return N * math.log(2) - 0.5 * math.log(math.pi * N / 2) - 2 * x * x / N


def large_n_summary(N: float = 1e23) -> dict[str, float]:
    """Re-evaluate questions (a)-(i) for a macroscopic number of coins."""
    ln10 = math.log(10)
    sigma = math.sqrt(N) / 2                       # standard deviation of the number of heads
    return {
        "N": N,
        "sigma": sigma,
        "relative_width": 1 / math.sqrt(N),        # sigma / mu with mu = N/2
        # (a) and (h): P_30 and P_8 are of the form 10^(-huge); we return the exponent.
        "log10_P30": (log_omega_small_k(N, 30) - N * math.log(2)) / ln10,
        "log10_P8": (log_omega_small_k(N, 8) - N * math.log(2)) / ln10,
        # (b) height of the peak: sqrt(2 / (pi N)).
        "P_half": math.sqrt(2 / (math.pi * N)),
        # (c), (d) probability of a window of +-10 or +-20 heads around N/2 (Gaussian area).
        "P_window_10": math.erf(10.5 / (sigma * math.sqrt(2))),
        "P_window_20": math.erf(20.5 / (sigma * math.sqrt(2))),
        # (e), (f) entropy changes Delta S / k_B = -2 x^2 / N (tiny).
        "dS_e": -2 * 25**2 / N,
        "dS_f": -2 * 10**2 / N,
        # (g) maximum disorder vs only 20 heads: about N ln 2 (macroscopic).
        "dS_g": log_omega_gaussian(N, 0) - log_omega_small_k(N, 20),
        # (i) ratio P(N/2)/P(N/2 +- 10) minus 1: practically zero.
        "ratio_minus_1": math.expm1(2 * 10**2 / N),
    }
