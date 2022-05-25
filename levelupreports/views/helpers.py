
# function that takes the output from db_cursor.fetchall function 
# and returns a list of dictionaries
def dict_fetch_all(cursor):
    """Return all rows from a cursor as a list of dictionaries"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
