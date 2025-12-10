"""
16. Se citește o matrice pătrată de dimensiune n*n cu elemente numere întregi. Scrieți
un program care:
	a) să afișeze numerele prime de pe diagonala principală;
	b) să formeze un vector cu elementele matricei parcurse în ordine pe coloane.
"""

from typing import List
import math


def is_prime(v: int) -> bool:
    if v < 2:
        return False
    if v in (2, 3):
        return True
    if v % 2 == 0 or v % 3 == 0:
        return False
    limit = int(math.isqrt(v))
    f = 5
    while f <= limit:
        if v % f == 0 or v % (f + 2) == 0:
            return False
        f += 6
    return True


def read_matrix() -> List[List[int]]:
    n = int(input())
    n = abs(n)
    
    return [list(map(int, input().split())) for _ in range(n)]


def primes_on_main_diagonal(matrix: List[List[int]]) -> List[int]:
    return [matrix[i][i] for i in range(len(matrix)) if is_prime(matrix[i][i])]


def column_major_vector(matrix: List[List[int]]) -> List[int]:
    if not matrix:
        return []
    n = len(matrix)
    # assumes square, so n columns
    return [matrix[r][c] for c in range(n) for r in range(n)]


def main() -> None:
    matrix = read_matrix()
    diag_primes = primes_on_main_diagonal(matrix)
    print("Primes on main diagonal: ")
    print(" ".join(map(str, diag_primes)) if diag_primes else "")
    
    vector = column_major_vector(matrix)
    print("Vector: ")
    print(" ".join(map(str, vector)))


if __name__ == "__main__":
    main()