
import pandas as pd
import csv, json
data = pd.read_csv("input_csv_file_name.csv")
print(data)
print("Convert JSON file below :")
print(json.dumps(list(csv.reader(open("input_csv_file_name.csv")))))


