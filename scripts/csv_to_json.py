import pandas as pd
from datetime import datetime
import json

class json:
    def __init__(self, df):
        self.df = df

    def csvToJson(self):
        output_path = "/content/drive/MyDrive/FYP/Code Base/Q&A/json/"

        for index, row in self.df.iterrows():
            row_dict = row.to_dict()

            json_file_name = f"{output_path}paper_{index + 1}.json"

            with open(json_file_name, 'w') as json_file:
                json.dump(row_dict, json_file)

            print(f"JSON file '{json_file_name}' created.")