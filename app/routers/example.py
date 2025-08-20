import app.schemas as schemas
from app.limiter import limiter
from app.database.models import *
from fastapi import APIRouter, Request

router = APIRouter(prefix='/example', tags=['Example'])


@router.get('/', summary='Пример', response_model=schemas.Response,
            responses={429: {'model': schemas.ErrorMessage}})
@limiter.limit('60/minute')
async def get_example(request: Request):
    return {'success': True, 'message': 'Success.'}
