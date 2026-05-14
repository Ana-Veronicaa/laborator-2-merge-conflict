def salut():
    """Returneaza un mesaj de salut."""
    return "Salut din laboratorul 2!"

def aduna(a, b):
    """Aduna doua numere."""
    return a + b

if __name__ == "__main__":
    print(salut())
    print(f"2 + 3 = {aduna(2, 3)}")