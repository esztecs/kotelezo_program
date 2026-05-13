
import json

FILE = "konyvek.json"


def load_books():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []



def save_books(books):
    with open(FILE, "w") as f:
        json.dump(books, f)



def add_book(books):
    print("\nPéldául így adj meg egy könyvet: J.K. Rowling: Harry Potter és a bölcsek köve")

    title = input("Könyv szerzője és címe ")

    book = {
        "title": title
    }

    books.append(book)
    save_books(books)

    print("A könyv elmentve.:)")



def list_books(books):
    print("\nEzeket a könyveket találtam a listában:")
    for i, book in enumerate(books):
        print(i + 1, "-", book["title"])



def search_book(books):
    word = input("\nKeress rá egy könyvre: ")

    found = False

    for book in books:
        if word.lower() in book["title"].lower():
            print(book["title"])
            found = True

    if not found:
        print("Nincs ilyen könyv a listában.:(")



books = load_books()

while True:
    print("\n1: Adj hozzá könyvet!")
    print("2: Könyvek listázása")
    print("3: Keress könyvet")
    print("4: Kilépés")

    choice = input("Válassz számot: ")

    if choice == "1":
        add_book(books)

    elif choice == "2":
        list_books(books)

    elif choice == "3":
        search_book(books)

    elif choice == "4":
        break

    else:
        print("Valamit nem jól adtál meg, próbáld újra!:)")