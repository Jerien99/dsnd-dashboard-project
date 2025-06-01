from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
root = Path(__file__).parent
db_path = root / 'employee_events.db'


# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:

    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe

    def pandas_query(self, sql_query: str):

        """This function receives an SQL query as a string
        and returns the data as a pandas DataFrame"""

        # Establish SQLite Database connection
        con = connect(db_path)

        # Store the result as a pandas DataFrame
        df = pd.read_sql_query(sql_query, con)

        # Close the connection
        con.close()

        # Return the dataframe
        return df

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)

    def query(self, sql_query: str):

        """This function receives an SQL query as a string
        and returns the data as a list of tuples."""

        # Establish SQLite Database connection
        con = connect(db_path)
        cur = con.cursor()

        # Execute the query within the open connection
        res = cur.execute(sql_query).fetchall()

        # Close the connection
        con.close()

        # Return the result as a list of tuples
        return res

# Leave this code unchanged


def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result

    return run_query
