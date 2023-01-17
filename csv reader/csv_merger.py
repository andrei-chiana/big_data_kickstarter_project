import os
import fnmatch
import pandas as pd

path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

csv_files = []

for file in os.listdir(path):
    if fnmatch.fnmatch(file, '*.csv'):
        csv_files.append(file)

#make a list of dataframes for each csv file
df_list = []
for file in csv_files:
            file_path = os.path.join(path, file)
            df_temp = pd.read_csv(file_path)
            df_list.append(df_temp)
            
#merge all those dataframes into one            
df_concat = pd.concat(df_list, ignore_index=True)

#keep only the columns that are necessary
data = df_concat[["category","launched_at", "name", "state"]]

print(data)
