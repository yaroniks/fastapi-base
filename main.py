from app.routers import *
from app.limiter import *
from config import settings
import app.database.requests as req
import app.common.schemas as schemas
from contextlib import asynccontextmanager

import uvicorn
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, Response, HTTPException, status
from starlette.responses import RedirectResponse, JSONResponse, HTMLResponse

from rabbitmq.services import RabbitMQExample


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run at startup
    yield
    # Run on shutdown
    await RabbitMQExample().close_rabbitmq()


app = FastAPI(title=settings.TITLE, version=settings.VERSION, root_path='/api/v1', lifespan=lifespan)
app.add_middleware(CORSMiddleware,
                   allow_origins=['*'],
                   allow_methods=['*'],
                   allow_headers=['*'],
                   allow_credentials=True)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.state.limiter = limiter


@app.get('/', summary='Документация', tags=['Docs'], response_class=HTMLResponse)
@limiter.limit('60/minute')
async def home(request: Request, response: Response):
    return RedirectResponse('/api/v1/docs/')


app.include_router(r1)
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
