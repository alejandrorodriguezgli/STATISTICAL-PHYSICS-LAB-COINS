

import math

from src.thermodynamics import probability, cumulative_probability, entropy_change


# Test probabilidad de una cara con dos monedas
def test_probability():
    assert math.isclose(probability(2, 1), 0.5)


# Test que salgan 0 caras con 2 monedas
def test_probability_zero():
    assert math.isclose(probability(2, 0), 0.25)


# Test de que la probabilidad total es igual a uno
def test_total_probability():
    assert math.isclose(cumulative_probability(2, 0, 2), 1)


# Test de cambio de entropia entre estados iguales
def test_entropy_zero():
    assert entropy_change(4, 2, 2) == 0


# Test de que un estado menos probable tiene menos entropia
def test_entropy_negative():
    assert entropy_change(4, 0, 2) < 0
