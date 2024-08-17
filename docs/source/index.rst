PoC Project: Exploring SQLite3, SQLModel, FastAPI, and Pydantic
===================================================================

**Overview**

This proof-of-concept (PoC) project serves as a testing ground for the seamless integration of several powerful Python modules:

* **SQLite3:** A lightweight, file-based relational database engine.
* **SQLModel:** An intuitive ORM (Object-Relational Mapper) that bridges the gap between Python objects and SQL databases.
* **FastAPI:** A high-performance web framework for building APIs with automatic interactive documentation.
* **Pydantic:** A data validation library that enforces type hints and provides user-friendly error messages.

**Key Features**

* **CRUD Operations:** The project demonstrates basic Create, Read, Update, and Delete (CRUD) operations on a sample data model.
* **Data Validation:** Pydantic models guarantee that data entering and leaving the API adheres to predefined structures and types.
* **API Documentation:** FastAPI's built-in Swagger UI provides interactive API documentation, making it easy to explore and test endpoints.

**How to Run**

1. **Install Dependencies:**


.. code-block:: console

    $ pip install fastapi uvicorn sqlmodel click docutils



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules
   poc_project
   poc_project.data
   poc_project.models


Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
