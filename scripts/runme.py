from pre_processing import Preprocssing
from csv_to_json import json

class runme:

    def __init__(self, file, abbr):
        self.file = file
        self.abbr = abbr
    
    def process(self):
        x= Preprocssing(self.file, self.abbr)
        processed_df = x.apply_processing()

        j = json(processed_df)
        j.csvToJson()
