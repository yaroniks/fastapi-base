import app.database.requests as req
import app.common.schemas as schemas
from fastapi import APIRouter, Request, Response, HTTPException, status

router = APIRouter(prefix='/example', tags=['Example'])


@router.get('/', summary='Пример', response_model=schemas.Response,
            responses={404: {'model': schemas.ErrorMessage}})
async def get_example():
    return {'success': True, 'message': 'Success.'}
