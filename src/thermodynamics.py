
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
