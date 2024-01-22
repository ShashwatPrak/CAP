from postgres import *
from config import *
import pandas as pd

config = Config()
psql_conn = PGConn(config)

df = pd.read_csv('Book2.csv')



for index, row in df.iterrows():
    # Define the INSERT SQL command
    
    insert_query = "INSERT INTO jnu(Sl_no, School, Sub_code_number, eligibility, NTA_code) VALUES (%s, %s, %s, %s, %s);"
    # Get the values from the current row as a list
    values = list(row)
    # Execute the SQL command with the values
    with psql_conn.connection().cursor() as curr:
        curr.execute(insert_query, values)



