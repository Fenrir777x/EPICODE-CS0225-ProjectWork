import datetime

def mostra_menu():
    print("\nCosa vuoi sapere?")
    print("1. Data di oggi")
    print("2. Ora attuale")
    print("3. Come mi chiamo (domanda all'assistente)")
    print("4. Esci")

def data():
    oggi = datetime.date.today()
    return f"La data di oggi è {oggi.strftime('%d/%m/%Y')}"

def ora():
    ora = datetime.datetime.now().time()
    return f"L'ora attuale è {ora.strftime('%H:%M')}"

def nome():
    return "Mi chiamo Assistente Virtuale"

def main():
    while True:
        mostra_menu()
        scelta = input("Seleziona un'opzione (1-4): ")

        if scelta == "1":
            print(data())
        elif scelta == "2":
            print(ora())
        elif scelta == "3":
            print(nome())
        elif scelta == "4":
            print("Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()