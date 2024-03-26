import pandas as pd
from datetime import datetime
import json

def csvToJson(df):
    output_path = "/content/drive/MyDrive/FYP/Code Base/Q&A/json/"

    for index, row in df.iterrows():
        row_dict = row.to_dict()

        json_file_name = f"{output_path}paper_{index + 1}.json"

        with open(json_file_name, 'w') as json_file:
            json.dump(row_dict, json_file)

        print(f"JSON file '{json_file_name}' created.")

def stringsToList(author):
    return [s.lower().strip() for s in author.split(";")]

def dateFormatter(date):
    date_obj = datetime.strptime(date, '%d-%b-%y')
    formatted_date = date_obj.strftime('%Y-%m-%d')
    return formatted_date