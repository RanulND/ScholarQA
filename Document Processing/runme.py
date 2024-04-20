from Scripts.pre_processing import Preprocessing
from Scripts.csv_to_json import Json

class runme:
    
    def __init__(self, file, abbr):
        self.file = file
        self.abbr = abbr
    
    def process(self):
        x= Preprocessing(self.file, self.abbr)
        processed_df = x.apply_processing()

        j = Json(processed_df)
        j.csvToJson()

y = runme('Sample Files/raw data/llm.xlsx','Sample Files/abbreviations.txt')
y.process()
