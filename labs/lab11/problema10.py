"""
10. Se citește un tablou bidimensional A cu n linii și m coloane (m<=30, n<=30) cu
elemente numere întregi. Scrieți un program care afișează tabloul după ștergerea
coloanelor care conțin numere negative.
"""

from typing import List


def read_matrix() -> List[List[int]]:
    """Read n, m and the matrix values from stdin."""
    print("Well get the row/column sizes:")
    n, m = map(int, input().split())
    if n >= 30 or m >= 30:
        return None
    
    n, m = abs(n), abs(m)
    
    print("\nNow the elements in the matrix:")
    matrix = [list(map(int, input().split())) for _ in range(n)]
    return matrix


def delete_negative_columns(matrix: List[List[int]]) -> List[List[int]]:
    """Remove columns that contain any negative number."""
    if not matrix:
        return matrix

    rows, cols = len(matrix), len(matrix[0])

    # Determine which columns are safe (no negatives anywhere in the column)
    safe_columns = []
    for c in range(cols):
        column_has_negative = any(matrix[r][c] < 0 for r in range(rows))
        if not column_has_negative:
            safe_columns.append(c)

    # Build new matrix keeping only safe columns
    return [[row[c] for c in safe_columns] for row in matrix]


def print_matrix(matrix: List[List[int]]) -> None:
    """Print matrix rows space-separated; print empty line if no columns remain."""
    if not matrix or not matrix[0]:
        # No columns left; print nothing or an empty line (choose empty line for visibility).
        print()
        return
    
    print("\nHere's your matrix: ")
    for row in matrix:
        print(" ".join(map(str, row)))


def main() -> None:
    matrix = read_matrix()
    result = delete_negative_columns(matrix)
    print_matrix(result)


if __name__ == "__main__":
    main()