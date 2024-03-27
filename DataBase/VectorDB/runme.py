from Scripts.database import DB


# initialize the DB instance

"""
make sure to change the path to the folder containing your json files
"""

x= DB(json_folder="Sample Files/json format")

# loop through all the json files
for json_file in x.json_files:
    x.process_json_file(json_file)

