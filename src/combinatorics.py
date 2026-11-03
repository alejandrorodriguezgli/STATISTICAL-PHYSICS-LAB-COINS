"""Combinatorics for a system of N coins (two-state elements).

Omega(N, k) is the number of microstates with exactly k heads.
"""
# First we import the math module, which provides mathematical functions and constants.
import math
# pathlib handles file paths, we use Path to create the output folder for figures.
from pathlib import Path
# matplotlib.pyplot is the plotting library; "plt" is the standard short name for it.
import matplotlib.pyplot as plt

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

# Next, we define the function distribution.
# This function returns a list of integers representing the number of microstates for every possible number of heads (k) from 0 to N.
def distribution(N: int) -> list[int]:
    """Omega(N, k) for every k = 0, 1, ..., N."""
    return [omega(N, k) for k in range(N + 1)]

# Now we define the function plot_distributions, which plots Omega(N, k) versus k for several values of N in one figure.
# Ns = (20, 50, 80, 100) is a default value for when the function is called without arguments.
# The filename sets where the PDF will be saved. The function does not return any value, but it saves the plot as a PDF file and displays it.
def plot_distributions(Ns=(20, 50, 80, 100),
                       filename="report/figures/omega_distributions.pdf") -> None:
    """Plot Omega(N, k) versus k for several N in one figure (log y-axis)."""
    # We create an empty figure and axes for the plot using plt.subplots.
    fig, ax = plt.subplots(figsize=(7, 4.5))
    # We loop through each value of N in Ns.
    for N in Ns:
        ax.plot(range(N + 1), distribution(N), marker="o", markersize=3, label=f"N = {N}")
    # We set a logarithmic scale for the y-axis to better visualize the distribution of microstates, especially for larger values of N.
    ax.set_yscale("log")
    # We set the axis labels to describe what is being shown.
    ax.set_xlabel("Number of heads, k")
    ax.set_ylabel(r"Number of microstates, $\Omega(N, k)$")
    # Legend is added to the plot to identify which line corresponds to which value of N and a faint grid. 
    ax.legend()
    ax.grid(True, alpha=0.3)
    # We adjust the margins of the plot so that the labels fit nicely within the figure.
    fig.tight_layout()
    # We use Path from the pathlib module to create the output folder for the figure if it does not already exist.
    Path(filename).parent.mkdir(parents=True, exist_ok=True)  # create folder if missing
    fig.savefig(filename)
    # Finally, we display the plot using plt.show(), which opens a window with the figure.
    plt.show()
