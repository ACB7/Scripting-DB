
# Hier is een Python-code voor een kassasysteem dat de producten uit een CSV-bestand haalt en de prijs berekent op basis van de gebruikersinvoer (in de vorm van tekst). Het gebruikt ten minste één def-functie en elke opdracht is uitgelegd met een comment.

import csv

# Lees de producten uit het CSV-bestand
def lees_producten(bestandsnaam):
    """
    Lees de producten uit het CSV-bestand en retourneer ze als een dictionary
    met de productnaam als sleutel en de prijs als waarde.
    """
    producten = {}
    with open(bestandsnaam, 'r') as bestand:
        reader = csv.reader(bestand)
        next(reader)  # Sla de koptekstrij over
        for rij in reader:
            producten[rij[0]] = float(rij[1])
    return producten

# Bereken de totale prijs op basis van de gebruikersinvoer
def bereken_totaal(producten):
    """
    Vraag de gebruiker om producten in te voeren en bereken de totale prijs.
    """
    totaal = 0
    while True:
        product = input("Voer een product in (of 'stop' om te stoppen): ").lower()
        if product == "stop":
            break
        if product in producten:
            prijs = producten[product]
            print(f"{product.capitalize()} kost ${prijs:.2f}")
            totaal += prijs
        else:
            print(f"'{product}' is geen geldig product.")
    print(f"Het totaalbedrag is: ${totaal:.2f}")

# Hoofdfunctie
def main():
    bestandsnaam = "producten.csv"
    producten = lees_producten(bestandsnaam)
    bereken_totaal(producten)

if __name__ == "__main__":
    main()
```

# Uitleg van de code:

# 1. De `import csv` regel importeert de CSV-module, die we nodig hebben om met CSV-bestanden te werken.

# 2. De functie `lees_producten(bestandsnaam)` leest de producten uit het CSV-bestand en retourneert 
# ze als een dictionary met de productnaam als sleutel en de prijs als waarde. 
# De functie opent het CSV-bestand, slaat de koptekstrij over en voegt elke rij toe aan de dictionary met 
# de productnaam als sleutel en de prijs (omgezet naar een float) als waarde.

# 3. De functie `bereken_totaal(producten)` vraagt de gebruiker om producten in te voeren en berekent de totale prijs. 
# De functie blijft vragen om producten tot de gebruiker "stop" invoert. 
# Voor elk ingevoerd product controleert de functie of het product in de dictionary met producten voorkomt. 
# Als dat het geval is, wordt de prijs van het product opgeteld bij het totaal en wordt de prijs van het product getoond. 
# Als het product niet in de dictionary voorkomt, wordt een foutmelding weergegeven. Aan het einde wordt het totaalbedrag getoond.

# 4. De functie `main()` is de hoofdfunctie van het programma. 
# Deze functie roept eerst de `lees_producten` functie aan om de producten uit het CSV-bestand te laden en slaat ze op 
# in de `producten` dictionary. Vervolgens roept de functie de `bereken_totaal` functie aan met de `producten` dictionary als argument.

# 5. De `if __name__ == "__main__":` regel zorgt ervoor dat de `main()` functie alleen wordt uitgevoerd als het script direct wordt uitgevoerd en 
# niet wanneer het als module wordt geïmporteerd.

# Opmerking: Dit programma gaat ervan uit dat het CSV-bestand "producten.csv" in dezelfde directory staat als het Python-script. 
# Je kunt de naam en locatie van het CSV-bestand aanpassen door de waarde van de `bestandsnaam` variabele in de `main()` functie te wijzigen.


