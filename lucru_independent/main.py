"""
Despre țări se cunoaște următoarea informație: nume, capitala, continentul, suprafața țării, numărul de locuitori.
Să se construiască un fișier binar Tara.dat din datele cu  structura indicată, cu preluarea informațiilor dintr-un fișier
textual  "in.txt" și să se inscrie într-un fișier textual "out.txt: 
	1. Țara și continentul pentru o capitală dată de la tastatură;
	2. Țările cu cea mai mare suprafață;
	3. Să se ordoneze informația în ordine descrescătoare după numărul de locuitori.
Pentru alternativă se propun problemele formulate la sfârșitul unității didactice Tipul de date Fișier.
"""

import pickle
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Country:
    name: str
    capital: str
    continent: str
    area: float
    population: int


def read_countries_from_text(file: str) -> List[Country]:
    """Reads countries from the text file in.txt"""
    countries = []
    try:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                # Format: name|capital|continent|area|population
                parts = [p.strip() for p in line.split('|')]
                if len(parts) == 5:
                    countries.append(Country(
                        name=parts[0],
                        capital=parts[1],
                        continent=parts[2],
                        area=float(parts[3]),
                        population=int(parts[4])
                    ))
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    return countries


def write_countries_to_binary(countries: List[Country], file: str) -> None:
    """Writes countries to a binary file"""
    try:
        with open(file, 'wb') as f:
            pickle.dump(countries, f)
        print(f"Data has been written to binary file '{file}'.")
    except Exception as e:
        print(f"Error writing binary file: {e}")


def read_countries_from_binary(file: str) -> List[Country]:
    """Reads countries from the binary file"""
    try:
        with open(file, 'rb') as f:
            countries = pickle.load(f)
        return countries
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return []
    except Exception as e:
        print(f"Error reading binary file: {e}")
        return []


def find_country_by_capital(countries: List[Country], capital: str) -> Optional[Country]:
    """Finds country by capital"""
    for country in countries:
        if country.capital.lower() == capital.lower():
            return country
    return None


def find_countries_with_max_area(countries: List[Country]) -> List[Country]:
    """Finds countries with the largest area"""
    if not countries:
        return []
    max_area = max(country.area for country in countries)
    return [country for country in countries if country.area == max_area]


def sort_by_population_desc(countries: List[Country]) -> List[Country]:
    """Sorts countries by population in descending order"""
    return sorted(countries, key=lambda c: c.population, reverse=True)


def write_results_to_file(countries: List[Country], output_file: str, searched_capital: str) -> None:
    """Writes results to out.txt file"""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=" * 60 + "\n")
            f.write("RESULTS\n")
            f.write("=" * 60 + "\n\n")
            
            # 1. Country and continent for a given capital
            f.write("1. Search by capital:\n")
            f.write(f"   Searched capital: {searched_capital}\n")
            found_country = find_country_by_capital(countries, searched_capital)
            if found_country:
                f.write(f"   Country: {found_country.name}\n")
                f.write(f"   Continent: {found_country.continent}\n")
            else:
                f.write(f"   No country found with capital '{searched_capital}'.\n")
            f.write("\n")
            
            # 2. Countries with the largest area
            f.write("2. Countries with the largest area:\n")
            countries_max_area = find_countries_with_max_area(countries)
            if countries_max_area:
                max_area = countries_max_area[0].area
                f.write(f"   Maximum area: {max_area:,.2f} km²\n")
                f.write(f"   Countries:\n")
                for country in countries_max_area:
                    f.write(f"   - {country.name} ({country.capital}, {country.continent})\n")
            else:
                f.write("   No countries in database.\n")
            f.write("\n")
            
            # 3. Countries sorted by population (descending)
            f.write("3. Countries sorted by population (descending):\n")
            sorted_countries = sort_by_population_desc(countries)
            for i, country in enumerate(sorted_countries, 1):
                f.write(f"   {i}. {country.name} - {country.population:,} inhabitants "
                       f"({country.capital}, {country.continent}, {country.area:,.2f} km²)\n")
            
        print(f"Results have been written to file '{output_file}'.")
    except Exception as e:
        print(f"Error writing output file: {e}")


def main():
    input_file = "in.txt"
    binary_file = "Country.dat"
    output_file = "out.txt"
    
    # Read countries from text file
    print("Reading data from text file...")
    countries = read_countries_from_text(input_file)
    
    if not countries:
        print("No data found in input file.")
        return
    
    print(f"Read {len(countries)} countries.")
    
    # Write countries to binary file
    write_countries_to_binary(countries, binary_file)
    
    # Read from binary file (to demonstrate it works)
    countries_from_bin = read_countries_from_binary(binary_file)
    
    # Read capital from keyboard
    searched_capital = input("\nEnter capital to search for: ").strip()
    
    # Write results to output file
    write_results_to_file(countries_from_bin, output_file, searched_capital)
    
    print("\nProgram executed successfully!")


if __name__ == "__main__":
    main()
