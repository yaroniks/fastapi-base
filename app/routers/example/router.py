import app.common.schemas as schemas
import app.database.requests as req
from fastapi import APIRouter, Request, Response, HTTPException, status

router = APIRouter(prefix='/example', tags=['Example'])
