import os
import fnmatch
import pandas as pd

path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

csv_files = []

for file in os.listdir(path):
    if fnmatch.fnmatch(file, '*.csv'):
        csv_files.append(file)


df_append = pd.DataFrame()
#append all files together
for file in csv_files:
            file_path = os.path.join(path, file)
            df_temp = pd.read_csv(file_path)
            df_append = df_append.append(df_temp, ignore_index=True)

print(df_append)


