import pandas as pd
from datetime import datetime
import json
import os

class Json:
    """
    
    this class is defined to convert the records into individual json files.

    input
    a datframe that contains all the pre-processed abstracts
    output
    json file for eahch record

    """
    def __init__(self, df):
        self.df = df

    def csvToJson(self):

        current_directory = os.getcwd()
        output_path = current_directory + '/data/json/' # path to store json

        for index, row in self.df.iterrows():
            row_dict = row.to_dict()

            title = row_dict['Title']
        
            json_file_name = f"{output_path}{title}.json"

            with open(json_file_name, 'w') as json_file:
                json.dump(row_dict, json_file)

            print(f"JSON file '{json_file_name}' created.")