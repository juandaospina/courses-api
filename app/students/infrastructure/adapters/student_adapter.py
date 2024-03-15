from typing import List

from sqlalchemy.orm import Session

from app.models import Students
from ...domain.repository import StudentRepository


class StudentAdapter(StudentRepository):
    def __init__(self, db: Session):
        self.database = db

    def get_students(self) -> List[Students]:
        data = self.database.query(Students).all()
        return data