from pydantic import BaseModel


class StudentModel(BaseModel):
    """
    Student model class responsible for creating `pydantic` schema. which can be later used by
    `SQLModel` library to make the SQL related operations and `FastAPI` to perform activities around it.
    """

    id: int
