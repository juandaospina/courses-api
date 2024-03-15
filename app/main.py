from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.database import Base, engine
from .students.infrastructure.api.router import students_router


app = FastAPI(
    title="API courses",
    description="API for student registration to courses and authentication (jwt)",
    version="1.0",
)

Base = Base.metadata.create_all(bind=engine)

@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


app.include_router(students_router)