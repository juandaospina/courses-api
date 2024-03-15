from typing import List

from app.models import Students
from app.students.domain import repository


class InMemoryStudentAdapter(repository.StudentRepository):
    students = []

    def get_students(self) -> List[Students]:
        return self.students