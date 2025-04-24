import csv
import os

class CSVLoader:
    def __init__(self, csv_folder='CSVs'):
        self.csv_folder = csv_folder

    def load_all_csvs(self):
        all_data = []
        for filename in os.listdir(self.csv_folder):
            if filename.endswith('.csv'):
                file_path = os.path.join(self.csv_folder, filename)
                with open(file_path, newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        all_data.append(row)

        return all_data
