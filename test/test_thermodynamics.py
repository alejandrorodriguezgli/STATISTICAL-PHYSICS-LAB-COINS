
from src.thermodynamics import probability, cumulative_probability, entropy_change


# Test probability de una cara co dos monedas
def test_probability():
    assert probability(2, 1) == 0.5


# Test que salgan 0 caras con 2 monedas
def test_probability_zero():
    assert probability(2, 0) == 0.25


# Test de la probabilidad total es igual a uno
def test_total_probability():
    assert cumulative_probability(2, 0, 2) == 1


# Test de cambio de entropía entre equal states
def test_entropy_zero():
    assert entropy_change(4, 2, 2) == 0


# Test de un estado menos probable tiene menos entropía
def test_entropy_negative():
    assert entropy_change(4, 0, 2) < 0

