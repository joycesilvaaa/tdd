import pytest

from triangle import classify_triangle, is_valid_triangle


def test_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "escaleno"


def test_isosceles_triangle():
    assert classify_triangle(5, 5, 3) == "isósceles"


def test_equilateral_triangle():
    assert classify_triangle(6, 6, 6) == "equilátero"


def test_isosceles_permutations():
    assert classify_triangle(5, 3, 5) == "isósceles"
    assert classify_triangle(3, 5, 5) == "isósceles"
    assert classify_triangle(5, 5, 3) == "isósceles"


def test_zero_side():
    assert classify_triangle(0, 5, 5) == "não é triângulo"


def test_negative_side():
    assert classify_triangle(-1, 5, 5) == "não é triângulo"


def test_sum_equals_third_side_permutations():
    assert classify_triangle(1, 2, 3) == "não é triângulo"
    assert classify_triangle(2, 3, 1) == "não é triângulo"
    assert classify_triangle(3, 1, 2) == "não é triângulo"


def test_sum_less_than_third_side_permutations():
    assert classify_triangle(1, 2, 4) == "não é triângulo"
    assert classify_triangle(2, 4, 1) == "não é triângulo"
    assert classify_triangle(4, 1, 2) == "não é triângulo"


def test_all_zero_sides():
    assert classify_triangle(0, 0, 0) == "não é triângulo"


def test_triangle_validation():
    assert is_valid_triangle(3, 4, 5)
    assert not is_valid_triangle(0, 0, 0)
