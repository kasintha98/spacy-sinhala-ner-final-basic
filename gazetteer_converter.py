import csv
import os


file_dir = 'C:/Users/SysAdminModule/Desktop/Research/spacy-sinhala-ner-final-basic/raw-files'

filename_location = "gazetteer_location.csv"
gazetteer_csv_location = os.path.join(file_dir, filename_location)

filename_date = "gazetteer_date.csv"
gazetteer_csv_date = os.path.join(file_dir, filename_date)


class GazetteerConverter:

    @staticmethod
    def get_patterns():
        patterns = []

        with open(gazetteer_csv_location, 'r', encoding="utf8") as csvfile:
            csvfile = csv.reader(csvfile)
            for row in csvfile:
                for i in range(2, len(row)):
                    obj = {"label": row[0], "pattern": row[i], "id": row[1]}
                    patterns.append(obj)

        with open(gazetteer_csv_date, 'r', encoding="utf8") as csvfile:
            csvfile = csv.reader(csvfile)
            for row in csvfile:
                for i in range(2, len(row)):
                    obj = {"label": row[0], "pattern": row[i], "id": row[1]}
                    patterns.append(obj)

        return patterns
