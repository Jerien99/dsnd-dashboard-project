from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

root = Path(__file__).parent
db_path = root / 'employee_events.db'

# Establish SQLite Database connection
con = connect(db_path)
cur = con.cursor()

# Execute the query within the open connection
res = cur.execute("SELECT * FROM employee").fetchall()

# Close the connection
con.close()

# Return the result as a list of tuples (which the fetchall method does automatically)

print(res)


