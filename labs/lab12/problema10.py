"""
10.Despre studenții unei grupe se cunoaște următoarea informație: numele, grupa,
reușita (3 note). Să se formeze un tabel cu informații despre n (n<=100) studenți și
să se afișeze:
	- informația despre studenții care au cel puțin o notă mai mică ca 5;
	- informația despre studenții cu media mai mare ca 7.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    name: str
    group: str
    grades: List[float]

    @property
    def avg(self) -> float:
        return sum(self.grades) / len(self.grades)


def read_students() -> List[Student]:
    print("How many students do you have? ", end="")
    n = int(input())
    students = []
    for i in range(n):
        print(f"{i+1}: ", end="")
        parts = input().split()
        name, group = parts[0], parts[1]
        g1, g2, g3 = map(float, parts[2:5])
        students.append(Student(name, group, [g1, g2, g3]))
    return students


def main() -> None:
    students = read_students()

    low_grade = [s for s in students if any(g < 5 for g in s.grades)]
    high_avg = [s for s in students if s.avg > 7]
    
    print("\n")
    print("---People with low grades---")
    for s in low_grade:
        print(s.name, s.group, *s.grades, f"{s.avg:.2f}")
    print("---People with high grades---")
    for s in high_avg:
        print(s.name, s.group, *s.grades, f"{s.avg:.2f}")


if __name__ == "__main__":
    main()