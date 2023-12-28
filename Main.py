import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


from Database import Database
from Database import DVDMod
from Database import ActorMod
from Database import CharacterMod
from Export import export

database = Database()
dvd = DVDMod()
actor = ActorMod()
character = CharacterMod()
export = export()

database.create()

while True:
    clear()
    print("1. Add DVD")
    print("2. Delete DVD")
    print("3. Update DVD")
    print("4. List DVD's")
    print("5. Add Actor")
    print("6. List Actors")
    print("7. Add Character")
    print("8. List Characters")
    print("9. Export to csv")
    print("10. Exit")
    option = input("Select an option: ")
    match option:
        case "1":
            clear()
            title = input("Title of DVD: ")
            release_date = input("Release date of DVD: ")
            language = input("Original language of DVD: ")
            barcode = input("Barcode of DVD (Optional): ")
            dvd.insertdvd(title, release_date, language, barcode)
        case "2":
            clear()
            title = input("Title of DVD: ")
            dvd.removedvd(title)
        case "3":
            clear()
            orgtitle = input("(old) Title of DVD: ")
            title = input("New Title of DVD (Optional): ")
            barcode = input("New Barcode of DVD (Optional): ")
            dvd.updatedvd(orgtitle, title, barcode)
        case "4":
            clear()
            dvd.listDVD()
            print()
            input("Press Enter to continue...")
        case "5":
            clear()
            name = input("Name of actor: ")
            title = input("Title of dvd: ")
            actor.addActor(name,title)
        case "6":
            clear()
            actor.listActor()
            print()
            input("Press Enter to continue...")

        case "7":
            clear()
            name = input("Name of character: ")
            actorname = input("Name of Actor: ")
            character.addCharacter(name,actorname)
        case "8":
            clear()
            character.listCharacters()
            print()
            input("Press Enter to continue...")
        case "9":
            clear()
            print("1. DVD Table")
            print("2. Actor Table")
            print("3. Character Table")
            option2 = input("Select an option: ")
            match option2:
                case "1":
                    export.export_to_csv('DVD', 'dvd_data.csv')
                case "2":
                    export.export_to_csv('Actor', 'actor_data.csv')
                case "3":
                    export.export_to_csv('Character', 'character_data.csv')
            input("Press Enter to continue...")
        case "10":
            break


            




