"""
1. De la tastieră se introduce un caracter ch. Să se precizeze și afișeze felul
caracterului (literă, cifră, operator). În caz dacă nu este nici unul din cele
enumerate, să se afișeze „Caracter necunoscut”.
"""

# Use a dict, instead of SWITCH CASE method
knows_characters = {
    "letter" : "qwertyuiopasdfghjklzxcvbnm",
    "number": "1234567890",
    "symbol": "!#\"$%&\'()*+,-./:;<=>?@[]^_`{|}~'"
}

# Here's will be the main logic of the program
def main():
    character = input("Character: ")
    if not character:
        print("Caracter necunoscut.")
        return

    ch = character[0]

    if ch in knows_characters["letter"]: print('It is a letter')
    elif ch in knows_characters["number"]: print("It is a number")
    elif ch in knows_characters["symbol"]: print("It is a symbol")
    else: print("Caracter necunoscut")
    
# Run the program
if __name__ == "__main__":
    main()