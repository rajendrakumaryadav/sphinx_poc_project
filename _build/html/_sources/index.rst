PoC Project: Exploring SQLite3, SQLModel, FastAPI, and Pydantic
===================================================================

**Overview**

This proof-of-concept (PoC) project serves as a testing ground for the seamless integration of several powerful Python modules:

* **SQLite3:** A lightweight, file-based relational database engine.
* **SQLModel:** An intuitive ORM (Object-Relational Mapper) that bridges the gap between Python objects and SQL databases.
* **FastAPI:** A high-performance web framework for building APIs with automatic interactive documentation.
* **Pydantic:** A data validation library that enforces type hints and provides user-friendly error messages.

**Project Structure**

* **`database.py`:** Handles database setup, creation, and interaction using SQLModel.
* **`models.py`:** Defines Pydantic models to represent data structures, ensuring type safety and validation.
* **`main.py`:** Implements FastAPI endpoints to create, read, update, and delete data through the database.

**Key Features**

* **CRUD Operations:** The project demonstrates basic Create, Read, Update, and Delete (CRUD) operations on a sample data model.
* **Data Validation:** Pydantic models guarantee that data entering and leaving the API adheres to predefined structures and types.
* **API Documentation:** FastAPI's built-in Swagger UI provides interactive API documentation, making it easy to explore and test endpoints.

**How to Run**

1. **Install Dependencies:**
   ```bash
   pip install fastapi sqlmodel uvicorn


Subpackages
-----------

.. toctree::
   :maxdepth: 4

   poc_project.data
   poc_project.models

Submodules
----------

app module
----------------------------------------

.. automodule:: poc_project.app
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: poc_project
   :members:
   :undoc-members:
   :show-inheritance:
