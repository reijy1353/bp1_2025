"""
17.Despre studenții unei grupe care au cont în bancă se cunoaște următoarea informație:
numele, cont în bancă, grupa și suma pe care o dețin. Să se formeze un tabel cu
informații despre n (n<=100) studenți și să se afișeze:
	- lista alfabetică pe grupe a studenților și a sumelor pe care le dețin;
	- lista alfabetică a studenților care dețin suma maximă pe grupă.
"""

from dataclasses import dataclass
from typing import List, Dict
from collections import defaultdict


@dataclass
class BankStudent:
    name: str
    account: str
    group: str
    amount: float


def read_students() -> List[BankStudent]:
    print("How many students do you have?", end="")
    n = int(input())
    students = []
    for _ in range(n):
        parts = input().split()
        name = parts[0]
        account = parts[1]
        group = parts[2]
        amount = float(parts[3])
        students.append(BankStudent(name, account, group, amount))
    return students


def main() -> None:
    students = read_students()

    by_group: Dict[str, List[BankStudent]] = defaultdict(list)
    for s in students:
        by_group[s.group].append(s)
        
    print("\n")
    print("---List of students in increasing order--- (sorted)")
    for grp in sorted(by_group.keys()):
        for s in sorted(by_group[grp], key=lambda x: x.name.lower()):
            print(grp, s.name, s.account, f"{s.amount:.2f}")
    
    print("\n")
    print("---The richest students---")
    richest: List[BankStudent] = []
    for grp, members in by_group.items():
        max_amt = max(m.amount for m in members)
        richest.extend(s for s in members if s.amount == max_amt)
    for s in sorted(richest, key=lambda x: (x.group, x.name.lower())):
        print(s.group, s.name, s.account, f"{s.amount:.2f}")


if __name__ == "__main__":
    main()