from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from ..database import get_database

DBDependency = Annotated[Session, Depends(get_database)]