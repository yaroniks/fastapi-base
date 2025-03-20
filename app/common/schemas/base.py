from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class Response(BaseModel):
    success: bool
    message: str
