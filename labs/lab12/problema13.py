"""
13.Despre sportivii unui concurs se cunoaște următoarea informație: nume, prenume,
vârsta, țara, vechime, nota. Să se formeze un tabel cu informații despre n (n<=100)
sportivi și:
	- să se afișeze lista sportivilor în funcție de notele obținute în ordine descrescătoare;
	- să se afișeze toți sportivii care provin din țară X (citită de la tastatură).
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Athlete:
    last: str
    first: str
    age: int
    country: str
    experience: int
    score: float


def read_athletes() -> tuple[List[Athlete], str]:
    print("How many athletes there are? ", end="")
    n = int(input())
    athletes = []
    for i in range(n):
        print(f"{i+1} ", end="")
        parts = input().split()
        last, first = parts[0], parts[1]
        age = int(parts[2])
        country = parts[3]
        experience = int(parts[4])
        score = float(parts[5])
        athletes.append(Athlete(last, first, age, country, experience, score))
        
    print("The target country is: ", end="")
    target_country = input().strip()
    return athletes, target_country


def main() -> None:
    athletes, target = read_athletes()

    by_score = sorted(athletes, key=lambda a: a.score, reverse=True)
    from_country = [a for a in athletes if a.country.lower() == target.lower()]

    print("\n")    
    print("---Athletes by score---")
    for a in by_score:
        print(a.last, a.first, a.age, a.country, a.experience, a.score)
        
    print("\n")
    print("---Athletes from the target country---")
    for a in from_country:
        print(a.last, a.first, a.age, a.country, a.experience, a.score)


if __name__ == "__main__":
    main()