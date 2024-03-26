import pandas as pd
from datetime import datetime
import json
import os

class json:
    def __init__(self, df):
        self.df = df

    def csvToJson(self):
        current_directory = os.getcwd()
        output_path = current_directory + '/data/json/'

        for index, row in self.df.iterrows():
            row_dict = row.to_dict()

            json_file_name = f"{output_path}paper_{index + 1}.json"

            with open(json_file_name, 'w') as json_file:
                json.dump(row_dict, json_file)

            print(f"JSON file '{json_file_name}' created.")