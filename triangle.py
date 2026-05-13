def classify_triangle(a: int, b: int, c: int) -> str:
    if not is_valid_triangle(a, b, c):
        return "não é triângulo"

    if a == b == c:
        return "equilátero"

    if a == b or a == c or b == c:
        return "isósceles"

    return "escaleno"


def is_valid_triangle(a: int, b: int, c: int) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False

    return a + b > c and a + c > b and b + c > a
