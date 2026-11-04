
import math

kB = 1.380649e-23


# probabilidad de las k caras 
def probability(N, k):
    omega = math.comb(N, k)
    P = omega / (2**N)
    return P


# probabilidad entre los dos valores de k
def cumulative_probability(N, k1, k2):
    P_total = 0

    for k in range(k1, k2 + 1):
        P_total = P_total + probability(N, k)

    return P_total


# diferencia en S de los dos macroestados
def entropy_change(N, k1, k2):
    omega1 = math.comb(N, k1)
    omega2 = math.comb(N, k2)

    S1 = kB * math.log(omega1)
    S2 = kB * math.log(omega2)

    delta_S = S1 - S2

    return delta_S


# Team values
M = 4 / (1/46 + 1/13 + 1/28 + 1/6)

# We use the nearest even integer
N = 114

print("M =", M)
print("N =", N)


# Part a: Probability of 30 heads
print("a)", probability(N, 30))


# Part b: Probability of N/2 heads
print("b)", probability(N, 57))


# Part c: Between 47 and 67 heads
print("c)", cumulative_probability(N, 47, 67))


# Part d: Between 37 and 77 tails
print("d)", cumulative_probability(N, 37, 77))


# Part e: Entropy change (82 and 57 heads)
print("e)", entropy_change(N, 82, 57), "J/K")


# Part f: Entropy change (67 and 57 heads)
print("f)", entropy_change(N, 67, 57), "J/K")


# Part g: Entropy change (57 and 20 heads)
print("g)", entropy_change(N, 57, 20), "J/K")
