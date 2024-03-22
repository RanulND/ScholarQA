import pandas as pd
from datetime import datetime
import json

def csvToJson():
    file_path = "/content/drive/MyDrive/FYP/Code Base/Q&A/DataSet_1.csv"

    df = pd.read_csv(file_path)
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    # df['Pub Date'][1] = "17-Jun-23"

    df['Authors'] = df['Authors'].apply(stringsToList)
    df['Key Words'] = df['Key Words'].apply(stringsToList)
    df['Abstract'] = df['Abstract'].str.lower()
    df['Pub Date'] = df['Pub Date'].apply(dateFormatter)

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