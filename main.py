from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import Base, engine, get_database
from app.models.student import Students


app = FastAPI(
    title="API courses",
    description="API for student registration to courses and authentication (jwt)",
    version="1.0",
)

Base = Base.metadata.create_all(bind=engine)
CommonDepends = Annotated[Session, Depends(get_database)]


@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.get("/students")
async def get_students(db: CommonDepends):
    data = db.query(Students).all()
    return data