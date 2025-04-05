# CSVUtilities.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

import csv
import os

class CSVUtilities:
    """
    Useful utilities for processing CSV files
    """
    def load_csv_to_dict_list(self, filename):
        """
        Loads a CSV file into a list of dictionaries.
        @param filename String: The name of the CSV file. It must have a header row. 
        @return list: A list of dictionaries, where each dictionary represents a row in the CSV file.
        """
        """
        # Debugging the file path...
        print("******************")
        print("load_csv_to_dict_list(): Current directory:", os.getcwd())
        for filenameX in os.listdir():
            print(filenameX)
        print("******************")
        """
        try:
            with open(filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                data = [row for row in reader]
                return data
        except Exception as e: 
            print("CSVUtilities.load_csv_to_dict_list(): Error processing", filename)
            print(e)

# Example usage:
if __name__ == "__main__":
    csv_file = "your_data.csv"
    myCSVUtilities = CSVUtilities()
    data = myCSVUtilities.load_csv_to_dict_list(csv_file)
    print(data)
