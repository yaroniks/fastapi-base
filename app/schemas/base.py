from typing import Optional
from pydantic import BaseModel, Field


class Response(BaseModel):
    success: bool
    message: str


class ErrorMessage(BaseModel):
    detail: str
