"""Statistical Physics - Lab 1: Microstates of a system of coins.

Main script: it calls the functions written by every member of the team and
prints the answer to every question of the lab manual. The figures are saved
in report/figures/
"""

import math
import sys
import time
import tracemalloc
import warnings

# Save figures to files without opening windows (plt.show() does nothing then).
import matplotlib
matplotlib.use("Agg")
warnings.filterwarnings("ignore", message=".*non-interactive.*")

from src.combinatorics import omega, plot_distributions, plot_probabilities, probability
from src.microstates import count_heads, generate_microstates, group_by_heads
from src.thermodynamics import (
    cumulative_probability,
    entropy_change,
    kB,
    large_n_summary,
    likelihood_ratio,
    relative_probability_from_entropy,
    waiting_time_summary,
)


def benchmark(N: int) -> tuple[float, float]:
    """Part 1(b): time (s) and peak RAM (MB) of a full enumeration of the 2^N
    microstates with the generator generate_microstates (1 << N + yield).
    Each microstate is visited once and its number of heads is counted.
    Time and memory are measured in two separate runs, because tracemalloc
    slows the program down a lot and would spoil the timing."""
    counts = [0] * (N + 1)
    t0 = time.perf_counter()
    for microstate in generate_microstates(N):
        counts[microstate.count("H")] += 1
    elapsed = time.perf_counter() - t0
    assert sum(counts) == 2**N, "some microstates were lost"

    # memory does not depend on N (the generator holds one microstate at a time),
    # so a small run is enough to measure it
    tracemalloc.start()
    for microstate in generate_microstates(min(N, 16)):
        count_heads(microstate)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return elapsed, peak / 2**20


# -----------------------------------------------------------------------------
# Team parameter: N = 100 + M
# -----------------------------------------------------------------------------
NIAS = ["100551013", "100550928", "100553546", "100551006"]


def team_N(nias: list[str]) -> tuple[float, int]:
    """M = harmonic mean of the last two digits of each NIA.
    N = 100 + M rounded to the nearest EVEN integer, so that N/2 is a whole
    number of heads (the most probable macrostate exists and is unique)."""
    last_two = [int(nia[-2:]) for nia in nias]
    M = len(last_two) / sum(1 / x for x in last_two)
    N = 2 * round((100 + M) / 2)
    return M, N


def title(text: str) -> None:
    print("\n" + "=" * 70 + f"\n{text}\n" + "=" * 70)


def part1() -> None:
    # (a) all microstates for N = 7, grouped by number of heads
    title("PART 1(a): microstates for N = 7")
    groups = group_by_heads(generate_microstates(7))
    for k in range(7, -1, -1):
        print(f"k = {k} heads, {7 - k} tails: Omega = {len(groups[k]):2d}   {', '.join(groups[k])}")
    print(f"Total = {sum(len(g) for g in groups.values())} = 2^7")

    # (b) largest N that can be fully enumerated in 5 minutes
    title("PART 1(b): full enumeration benchmark")
    N = 16
    while True:
        t, mem = benchmark(N)
        print(f"N = {N:2d}: 2^N = {2**N:>13,d} microstates, time = {t:8.3f} s, peak RAM = {mem:.4f} MB")
        if t > 5 or N >= 30:     # stop the test after ~5 s (the full 5 min is extrapolated)
            break
        N += 1
    # time doubles with every extra coin: t(N') = t(N) * 2^(N'-N)
    N_max = N + math.log2(300 / t)
    print(f"Extrapolated maximum N in 5 minutes (300 s): N_max ~ {math.floor(N_max)}")

    # (c) distributions for N = 20, 50, 80, 100
    title("PART 1(c): macrostate distributions")
    for N in (20, 50, 80, 100):
        print(f"N = {N:3d}: Omega_max = Omega({N},{N // 2}) = {omega(N, N // 2):.4e}, total 2^N = {2**N:.4e}")
    plot_distributions()
    print("Figure saved: report/figures/omega_distributions.pdf")

    # (d) limits of the distribution calculation
    title("PART 1(d): maximum N for the distribution")
    n_fact = next(n for n in range(1, 400) if math.factorial(n) > sys.float_info.max)
    n_pow = next(n for n in range(1, 2000) if 2**n > sys.float_info.max)
    print(f"With normal floats: N! overflows at N = {n_fact}, 2^N at N = {n_pow}")
    print("With exact integers (omega) or logarithms (log_omega) there is no overflow;")
    print("the practical limit becomes computing time and memory for the N+1 values.")

    # (e) towards the thermodynamic limit
    title("PART 1(e): towards N ~ 1e23")
    for N in (20, 100, 1000, 10000, 1e23):
        print(f"N = {N:.0e}: relative width sigma/mu = 1/sqrt(N) = {1 / math.sqrt(N):.2e}")
    plot_probabilities()
    print("Figure saved: report/figures/probability_narrowing.pdf")


def part2(N: int) -> None:
    half = N // 2
    title(f"PART 2(a)-(g): N = {N}")
    print(f"(a) P(k=30)                 = {probability(N, 30):.4e}")
    print(f"(b) P(k={half})                 = {probability(N, half):.5f}")
    print(f"(c) P({half - 10} <= k <= {half + 10})    = {cumulative_probability(N, half - 10, half + 10):.5f}")
    print(f"(d) P({half - 20} <= k <= {half + 20})    = {cumulative_probability(N, half - 20, half + 20):.5f}")
    for label, k1, k2 in (("e", half + 25, half), ("f", half + 10, half), ("g", half, 20)):
        dS = entropy_change(N, k1, k2)
        print(f"({label}) S({k1}) - S({k2}) = {dS:.4e} J/K  =  {dS / kB:+.3f} k_B")

    title(f"PART 2(h)-(k): N = {N}")
    w = waiting_time_summary(N, 8)
    print(f"(h) P(k=8) = 10^{w['log10_P']:.2f}")
    print(f"    waiting time = 10^{w['log10_seconds']:.2f} s = 10^{w['log10_years']:.2f} years"
          f" = 10^{w['log10_universe_ages']:.2f} ages of the Universe")
    print(f"(i) P(N/2) / P(N/2 +- 10) = {likelihood_ratio(N, 10):.3f}")
    dS_g = entropy_change(N, half, 20) / kB
    print(f"(j) going back from N/2 to 20 heads: Delta S = {-dS_g:.2f} k_B ->"
          f" relative probability e^(Delta S/k_B) = {relative_probability_from_entropy(-dS_g):.2e}")

    L = large_n_summary(1e23)
    print("(k) N = 1e23:")
    print(f"    sigma = {L['sigma']:.2e} coins, sigma/mu = {L['relative_width']:.2e}")
    print(f"    P(k=30) = 10^({L['log10_P30']:.3e}),  P(k=8) = 10^({L['log10_P8']:.3e})")
    print(f"    P(N/2) = {L['P_half']:.2e},  P(N/2 +- 10) = {L['P_window_10']:.2e},  P(N/2 +- 20) = {L['P_window_20']:.2e}")
    print(f"    Delta S/k_B: (e) {L['dS_e']:.2e}, (f) {L['dS_f']:.2e}, (g) {L['dS_g']:.3e}")
    print(f"    P(N/2)/P(N/2 +- 10) - 1 = {L['ratio_minus_1']:.1e}")


if __name__ == "__main__":
    M, N = team_N(NIAS)
    title("TEAM PARAMETER")
    print(f"M = {M:.3f}  ->  N = 100 + M = {100 + M:.3f}  ->  nearest even integer N = {N}")
    part1()
    part2(N)
