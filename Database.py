import sqlite3


class Database:

    def create(self):
        db = sqlite3.connect('DVDManager.db')
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS DVD (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                release_date TEXT,
                language TEXT,
                barcode INT
            )
        ''')
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Actor (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    dvd_id INTEGER NOT NULL,      
                    FOREIGN KEY (dvd_id) REFERENCES DVD (id)

                )
            ''')
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Character (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    actor_id INTEGER NOT NULL,
                    FOREIGN KEY (actor_id) REFERENCES Actor (id)
                )
            ''')
        db.commit()
        db.close()

class DVDMod:
    def insertdvd(self, title, release_date, language, barcode):
        db = sqlite3.connect('DVDManager.db')
        cursor = db.cursor()
        cursor.execute('SELECT title FROM DVD WHERE title = ?', (title,))
        existing_dvd = cursor.fetchone()
        if existing_dvd:
            print("DVD already added")
        else:
            if barcode == "":
                cursor.execute("INSERT INTO DVD (title, release_date, language) VALUES (?, ?, ?)",
                               (title, release_date, language))
            else:
                cursor.execute("INSERT INTO DVD (title, release_date, language,barcode) VALUES (?, ?, ?, ?)",
                               (title, release_date, language, barcode))
            db.commit()
            print("DVD Added")
        db.close()

    def readdvd(self, id):
        db = sqlite3.connect('DVDManager.db')
        cursor = db.cursor()
        cursor.execute('SELECT title,release_date,language FROM DVD WHERE id = ?', (id,))
        dvd = cursor.fetchone()
        return dvd

    def removedvd(self, title):
        db = sqlite3.connect('DVDManager.db')
        cursor = db.cursor()
        cursor.execute('SELECT id FROM DVD WHERE title = ?', (title,))
        existing_dvd = cursor.fetchone()
        if existing_dvd:
            cursor.execute('DELETE FROM DVD WHERE title = ?', (title,))
            db.commit()
            print("DVD Removed")
        else:
            print("DVD not found")
        db.close()

    def updatedvd(self, orgtitle, title, barcode):
        db = sqlite3.connect('DVDManager.db')
        cursor = db.cursor()
        cursor.execute('SELECT id FROM DVD WHERE title = ?', (orgtitle,))
        existing_dvd = cursor.fetchone()
        if existing_dvd:
            print("DVD found")
            time.sleep(2)
            cursor.execute('SELECT title,release_date,language,barcode FROM DVD WHERE title = ?', (orgtitle,))
            dvd = cursor.fetchone()
            cursor.execute('DELETE FROM DVD WHERE title = ?', (orgtitle,))
            print(dvd[0])
            if title == "":
                title = dvd[0]
            if barcode == "":
                barcode = dvd[3]
            if barcode == "":
                cursor.execute("INSERT INTO DVD (title, release_date, language) VALUES (?, ?, ?)",
                               (title, dvd[1], dvd[2]))
            else:
                cursor.execute("INSERT INTO DVD (title, release_date, language,barcode) VALUES (?, ?, ?, ?)",
                               (title, dvd[1], dvd[2], barcode))

            db.commit()
        db.close()

    def listDVD(self):
        db = sqlite3.connect('DVDManager.db')
        cursor = db.cursor()
        cursor.execute('SELECT * FROM DVD')
        dvd_records = cursor.fetchall()
        if dvd_records:
            # Print the header
            print("{:<5} {:<20} {:<15} {:<15} {:<10}".format("ID", "Title", "Release Date", "Language", "Barcode"))
            print("-" * 70)

            # Print each record
            for record in dvd_records:
                formatted_record = tuple('NULL' if value is None else value for value in record)

                print("{:<5} {:<20} {:<15} {:<15} {:<10}".format(*formatted_record))
        else:
            print("The 'DVD' table is empty.")
