from abc import ABC, abstractmethod

class StudentRepository(ABC):
    @abstractmethod
    def get_students(self):
        return NotImplementedError