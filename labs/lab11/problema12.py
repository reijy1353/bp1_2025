"""
12. Se citește o matrice A cu n linii și m coloane (m<=30, n<=30) cu elemente numere
întregi. Scrieți un program care verifică, dacă elementele de pe coloana X sunt
ordonate crescător
"""

from typing import List


def read_matrix() -> tuple[List[List[int]], int]:
    print("Well get the row/column sizes:")
    n, m = map(int, input().split())
    if n >= 30 or m >= 30:
        return None
    
    n, m = abs(n), abs(m)
    
    print("\nNow the elements in the matrix:")
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    print("And the x: ", end="")
    x = int(input())
    
    return matrix, x


def is_column_increasing(matrix: List[List[int]], col: int) -> bool:
    if not matrix:
        return True
    # Ensure column exists
    if col < 0 or col >= len(matrix[0]):
        raise ValueError("Column index out of range")
    return all(matrix[i][col] <= matrix[i + 1][col] for i in range(len(matrix) - 1))


def main() -> None:
    matrix, col = read_matrix()
    result = is_column_increasing(matrix, col)
    print("YES" if result else "NO")


if __name__ == "__main__":
    main()