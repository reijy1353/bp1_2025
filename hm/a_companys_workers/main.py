from dataclasses import dataclass
from typing import List


@dataclass
class Employee:
    nume: str
    prenume: str
    data_nasterii: str
    functie: str
    salariu_ora: float
    ore_luna: float

    @property
    def salariu_lunar(self) -> float:
        return self.salariu_ora * self.ore_luna


def citeste_int(prompt: str) -> int:
    while True:
        try:
            valoare = int(input(prompt))
            if valoare <= 0:
                raise ValueError
            return valoare
        except ValueError:
            print("Introduceți un număr întreg pozitiv.")


def citeste_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Introduceți un număr (folosiți punct pentru zecimale).")


def citeste_employee(index: int) -> Employee:
    print(f"\nDate pentru angajatul #{index + 1}:")
    nume = input("Nume: ").strip()
    prenume = input("Prenume: ").strip()
    data_nasterii = input("Data nașterii (zz.ll.aaaa): ").strip()
    functie = input("Funcția: ").strip()
    salariu_ora = citeste_float("Salariul pentru o oră de muncă: ")
    ore_luna = citeste_float("Numărul de ore lucrate într-o lună: ")

    return Employee(
        nume=nume,
        prenume=prenume,
        data_nasterii=data_nasterii,
        functie=functie,
        salariu_ora=salariu_ora,
        ore_luna=ore_luna,
    )


def afiseaza_rezultate(
    angajati: List[Employee], cos_minim: float, functie_de_cautat: str
) -> None:
    total_salarii = sum(angajat.salariu_lunar for angajat in angajati)
    salariu_maxim = max(angajat.salariu_lunar for angajat in angajati)
    functii_cu_maxim = {
        angajat.functie for angajat in angajati if angajat.salariu_lunar == salariu_maxim
    }
    exista_functia = any(
        angajat.functie.lower() == functie_de_cautat.lower() for angajat in angajati
    )
    angajati_sub_cos = sum(
        1 for angajat in angajati if angajat.salariu_lunar < cos_minim
    )

    print("\nRezultate:")
    print(f"Suma totală necesară pentru salarii: {total_salarii:.2f}")
    print(
        "Funcțiile angajaților cu salariul maxim: "
        + ", ".join(sorted(functii_cu_maxim))
    )
    if exista_functia:
        print(f"Funcția '{functie_de_cautat}' există în companie.")
    else:
        print(f"Funcția '{functie_de_cautat}' nu există în companie.")
    print(
        f"Numărul angajaților cu salariul lunar sub coșul minim ({cos_minim:.2f}): "
        f"{angajati_sub_cos}"
    )


def main() -> None:
    print("=== Evidența angajaților întreprinderii ===")
    nr_angajati = citeste_int("Introduceți numărul de angajați: ")
    angajati = [citeste_employee(i) for i in range(nr_angajati)]

    cos_minim = citeste_float("\nIntroduceți valoarea coșului minim de consum pe lună: ")
    functie_de_cautat = input("Introduceți funcția pe care doriți să o verificați: ").strip()

    afiseaza_rezultate(angajati, cos_minim, functie_de_cautat)


if __name__ == "__main__":
    main()

