import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


from Database import Database


database = Database()

database.create()

while True:
    clear()
    print("1. Add DVD")
    print("2. Delete DVD")
    print("3. Update DVD")
    print("4. List DVD's")
    print("5. Add Actor")
    print("3. Add Character")
    print("7. Exit")
    option = input("Select an option: ")
    match option:
        case "1":
            clear()
            title = input("Title of DVD: ")
            release_date = input("Release date of DVD: ")
            language = input("Original language of DVD: ")
            barcode = input("Barcode of DVD (Optional): ")
            database.insertdvd(title, release_date, language, barcode)
        case "2":
            clear()
            title = input("Title of DVD: ")
            database.removedvd(title)
        case "3":
            clear()
            orgtitle = input("(old) Title of DVD: ")
            title = input("New Title of DVD (Optional): ")
            barcode = input("New Barcode of DVD (Optional): ")
            database.updatedvd(orgtitle, title, barcode)
        case "4":
            clear()
            database.listDVD()
            print()
            input("Press Enter to continue...")
        case "5":
            clear()
            name = input("Name of actor: ")
            title = input("Title of dvd: ")
            




