from typing import List

from ..domain.repository import StudentRepository
from app.models import Students


class StudentService:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def get_students(self) -> List[Students]:
        return self.repository.get_students()