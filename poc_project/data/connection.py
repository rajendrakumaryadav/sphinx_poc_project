"""
This application file is responsible to provide the complete connection related activities around database.
"""

import pathlib
import sqlite3

_db_path = pathlib.Path(__file__).parent.parent.parent.resolve() / "miscs"


def get_connection_path() -> pathlib.Path:
    """
    This function return the SQLite3 Path.
    """
    return _db_path


def connect(file_name: str = "db.sqlite3") -> sqlite3.Connection:
    """
    Establishes a connection to a SQLite database.

    Parameters
    ----------
    file_name : str, optional
        The name of the SQLite database file. Default is "db.sqlite3".

    Returns
    -------
    sqlite3.Connection
        A connection object representing the established connection to the
        SQLite database.

    Notes
    -----
    * The connection is configured with `autocommit=True`, meaning changes are
      automatically committed to the database.
    * The `check_same_thread=False` setting allows the connection to be used
      across multiple threads.
    """
    conn = sqlite3.connect(
        _db_path / file_name, autocommit=True, check_same_thread=False
    )
    return conn
