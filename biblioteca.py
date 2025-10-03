from csv import reader, writer

def carica_da_file(file_path):
    """Carica i libri dal file"""
    try:
        with open(file_path, "r", encoding="utf-8") as lettura_file:
            lettura = reader(lettura_file, delimiter=",")
            numero_sezioni = int(next(lettura)[0])

            biblioteca = {}
            for sezione in range(1, numero_sezioni + 1):
                biblioteca[sezione] = []

            for riga in lettura:
                biblioteca[int(riga[4])].append([riga[0], riga[1], int(riga[2]), int(riga[3]), int(riga[4])])

            return biblioteca

    except FileNotFoundError:
        return None


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    if sezione not in biblioteca:
        return None

    for lista in biblioteca.values():
        for libro in lista:
            if libro[0] == titolo:
                return None

    nuovo = [titolo, autore, anno, pagine, sezione]
    biblioteca[sezione].append(nuovo)

    try:
        with open(file_path, "a", encoding="utf-8") as aggiunta_nuovo:
            aggiunta = writer(aggiunta_nuovo)
            aggiunta.writerow(nuovo)
    except FileNotFoundError:
        return None

    return nuovo


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    for lista in biblioteca.values():
        for libro in lista:
            if libro[0] == titolo:
                return f"{libro[0]}, {libro[1]}, {libro[2]}, {libro[3]}, {libro[4]}"
    return None


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    for s in biblioteca.keys():
        if s == sezione:
            titoli = []
            for libro in biblioteca[s]:
                titoli.append(libro[0])
            return sorted(titoli)
    return None


def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

