import sqlite3
import csv

class export:

    def export_to_csv(self,table_name, csv_filename):

        conn = sqlite3.connect('DVDManager.db')
        cursor = conn.cursor()

        cursor.execute(f'SELECT * FROM {table_name}')
        rows = cursor.fetchall()

        if rows:

            column_names = [description[0] for description in cursor.description]

            with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)

                csv_writer.writerow(column_names)

                csv_writer.writerows(rows)

            print(f"Exported '{table_name}' to '{csv_filename}'.")
        else:
            print(f"No data found in '{table_name}'.")

        conn.close()


