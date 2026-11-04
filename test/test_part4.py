"""tests of Member 4 functions (Part 2 questions h-k)."""
import math

import pytest

from src.thermodynamics import (
    large_n_summary,
    likelihood_ratio,
    likelihood_ratio_exact,
    log10_waiting_time
)

def test_waiting_time_matches_exact_integers():
    N = 113
    exact = math.log10(2**N / omega(N, 8))
    assert log10_waiting_time(N, 8) == pytest.approx(exact, rel=1e-12)


def test_likelihood_ratio_log_vs_exact():
    for N in (100, 113, 150):
        assert likelihood_ratio(N, 10) == pytest.approx(likelihood_ratio_exact(N, 10), rel=1e-10)
        assert likelihood_ratio(N, 10) > 1

def test_large_N_limit():
    L = large_n_summary(1e23)
    assert L["relative_width"] == pytest.approx(1 / math.sqrt(1e23))
    assert L["P_window_10"] < 1e-9
    assert abs(L["dS_f"]) < 1e-20
    assert L["dS_g"] == pytest.approx(1e23 * math.log(2), rel=1e-9)
