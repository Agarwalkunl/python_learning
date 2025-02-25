from pydantic import BaseModel
from typing import Optional

# Pydantic schema for validation and structure
class UserSchema(BaseModel):
    name: str
    age: int
    email: Optional[str] = None
