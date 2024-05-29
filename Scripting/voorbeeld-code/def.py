

# Een functie definieert een herbruikbare blok code
# die taken kan uitvoeren en waarden kan retourneren.
# Het gebruiken van functies helpt je code te organiseren
# en maakt het gemakkelijker om je code te onderhouden en opnieuw te gebruiken.

# Deze functie voegt twee getallen samen en retourneert het resultaat
def som(a, b):
    """
    Deze functie neemt twee getallen als invoer en retourneert hun som.
    
    Parameters:
    a (int of float): Het eerste getal.
    b (int of float): Het tweede getal.
    
    Returns:
    int of float: De som van de twee getallen.
    """
    resultaat = a + b
    return resultaat

# Om een functie aan te roepen, gebruik je de functienaam
# gevolgd door haakjes met eventuele argumenten ertussen.
print(som(2, 3))  # Output: 5
print(som(4.5, 2.7))  # Output: 7.2

# Je kunt functies ook parameters geven met standaardwaarden,
# zodat je optionele argumenten kunt meegeven.
def begroeting(naam, formeel=False):
    """
    Deze functie begroet iemand.
    
    Parameters:
    naam (str): De naam van de persoon die begroet wordt.
    formeel (bool): Indien True, wordt een formele begroeting gebruikt.
    """
    if formeel:
        print(f"Goedendag, {naam}.")
    else:
        print(f"Hallo, {naam}!")

begroeting("Alice")  # Output: Hallo, Alice!
begroeting("Bob", formeel=True)  # Output: Goedendag, Bob.

# Functies kunnen ook andere functies aanroepen en retourneren.
def grootste(a, b):
    """
    Deze functie retourneert het grootste van twee getallen.
    """
    if a > b:
        return a
    else:
        return b

def kleinste(a, b):
    """
    Deze functie retourneert het kleinste van twee getallen.
    """
    return som(a, b) - grootste(a, b)

print(grootste(5, 8))  # Output: 8
print(kleinste(5, 8))  # Output: 5


