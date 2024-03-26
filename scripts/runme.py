from pre_processing import Preprocessing
from csv_to_json import Json

class runme:
    
    def __init__(self, file, abbr):
        self.file = file
        self.abbr = abbr
    
    def process(self):
        x= Preprocessing(self.file, self.abbr)
        processed_df = x.apply_processing()

        j = Json(processed_df)
        j.csvToJson()

y = runme('data/raw_abstracts.xlsx','data/abbreviations.txt')
y.process()
