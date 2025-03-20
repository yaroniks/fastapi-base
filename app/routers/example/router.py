import app.database.requests as req
import app.common.schemas as schemas
from fastapi import APIRouter, Request, Response, HTTPException, status

router = APIRouter(prefix='/example', tags=['Example'])
