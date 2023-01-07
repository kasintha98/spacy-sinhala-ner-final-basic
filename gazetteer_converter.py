import csv
import os

filename = "gazetteer.csv"
file_dir = 'D:/#CAMPUS/4th Year/Research/spacy-senhala-with-entity-ruler/raw-files'
gazetteer_csv = os.path.join(file_dir, filename)


class GazetteerConverter:

    @staticmethod
    def get_patterns():
        patterns = []

        with open(gazetteer_csv, 'r', encoding="utf8") as csvfile:
            csvfile = csv.reader(csvfile)

            for row in csvfile:
                for i in range(2, len(row)):
                    obj = {"label": row[0], "pattern": row[i], "id": row[1]}
                    patterns.append(obj)

        return patterns
