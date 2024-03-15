from fastapi import APIRouter, Depends

from ...application.service import StudentService
from ...domain.repository import StudentRepository
from ..adapters.in_memory_adapter import InMemoryStudentAdapter
from ..adapters.student_adapter import StudentAdapter 
from app.database import get_database


students_router = APIRouter(
    prefix="/students",
    tags=["students"]
)

def get_repository():
    db = next(get_database())
    return StudentService(StudentAdapter(db))
    # return StudentService(InMemoryStudentAdapter())


@students_router.get("")
async def get_students(service: StudentRepository = Depends(get_repository)):
    data = service.get_students()
    return data