import os
import csv
import pandas as pd
import sqlite3
import sqlalchemy

#For Windows, create absolute paht of Kickstarter.csv file

path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

file_path = os.path.join(path, 'Kickstarter.csv')

#Using Pandas read the file

data = pd.read_csv(file_path, delimiter= ',')

#Through Pandas clean the data

data = data[["category","launched_at", "name", "state"]]

print(data)

#On Windows database file will be found in C:\Users\user_name\
#Create connection to database using SQLAlchemy

dbEngine = sqlalchemy.create_engine('sqlite:///kickstarter.db')

#Connect to database
# we are using .connect() method in order to satisfy SQLAlchemy 2.0 requirements for future usage

with dbEngine.connect() as connection:
    #Write data to SQL Database, do not provide an index for now
    data.to_sql('projects', con=connection, if_exists='replace', index=False)

#This SQL Query found below will need to be implemented once we add all the datasets into SQL Database
# in order to convert time from UNIX Epoch format to human readable format

#UPDATE projects SET launched_at = datetime(launched_at, 'unixepoch', 'localtime')

#types of state:                   
