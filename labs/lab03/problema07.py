"""
7. Se introduce de la tastieră un număr întreg din diapazonul 100..999. Să se afișeze
un șir de caractere care descrie verbal numărul, de exemplu: 250 - „două sute
cincizeci”.
"""

# Define dicts (instead of using switch case as we know in C++)
first_pos_dict = {
    1: "o sută",
    2: "două sute",
    3: "trei sute",
    4: "patru sute",
    5: "cinci sute",
    6: "șase sute",
    7: "șapte sute",
    8: "opt sute",
    9: "nouă sute",
}

second_one_pos_dict = {
    1: "un",
    2: "doi",
    3: "trei",
    4: "pai",
    5: "cin",
    6: "șai",
    7: "șapte",
    8: "opt",
    9: "nouă",
}

second_two_pos_dict = {
    1: "",
    2: "două",
    3: "trei",
    4: "patru",
    5: "cinci",
    6: "șai",
    7: "șapte",
    8: "opt",
    9: "nouă",
}

last_pos_dict = {
    0: "",
    1: "unu",
    2: "doi",
    3: "trei",
    4: "patru",
    5: "cinci",
    6: "șase",
    7: "șapte",
    8: "opt",
    9: "nouă",
}

# Function to transform ints in the interval 100...999 to string form (verbal form)
def int_to_string_form(n):
    # Gathering the data needed
    first_pos, second_pos = divmod(n, 100)
    second_pos, last_pos = divmod(second_pos, 10)
    empty_string = ""
    empty_string += first_pos_dict[first_pos] + " "

    # * METHOD 1 (using ifs)
    # if second_pos == 1 and last_pos != 0:
    #     empty_string += second_one_pos_dict[last_pos] + "sprezece "
    # elif second_pos == 0:
    #     empty_string += last_pos_dict[last_pos]
    # else:
    #     if last_pos == 0:
    #         empty_string += second_two_pos_dict[second_pos] + "zece"
    #     else:
    #         empty_string += second_two_pos_dict[second_pos] + "zeci și " + last_pos_dict[last_pos]
                
    # * METHOD 2 (only using MATCH-CASE)
    match second_pos:
        case 1:
            match last_pos:
                case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
                    empty_string += second_one_pos_dict[last_pos] + "sprezece "

        case 0:
           empty_string += last_pos_dict[last_pos] 

        case 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
            match last_pos:
                case 0:
                    empty_string += second_two_pos_dict[second_pos] + "zece"
                case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
                   empty_string += second_two_pos_dict[second_pos] + "zeci și " + last_pos_dict[last_pos] 
    
    # Print the result
    print(f"Your numer is: {empty_string}")

# Main function, where we fetch variable data from the user
def main():
    n = int(input("Type a number in the interval 100...999: "))
    if not (n < 100 or n > 999): int_to_string_form(n)
    else: print("Can't do that, 'n' ins't in the specified interval...")

# Run the main() function
if __name__ == "__main__":
    main()