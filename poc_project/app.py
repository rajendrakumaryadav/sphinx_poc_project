from .data.connection import connect

"""
This file contain code to connect with SQLite Database.
It is simple entrypoint for the application.
"""

conn = connect()

print(conn)
