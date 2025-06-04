from app.routers import *
from app.limiter import *
from config import settings
from contextlib import asynccontextmanager

import uvicorn
from slowapi.errors import RateLimitExceeded
from fastapi import FastAPI, Request, Response
from slowapi import _rate_limit_exceeded_handler
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse, HTMLResponse

from app.database.base import async_main
from app.utils.rabbitmq import RabbitMQExample


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run at startup
    await async_main()
    yield
    # Run on shutdown
    RabbitMQExample().close_rabbitmq()


app = FastAPI(title=settings.TITLE, version=settings.VERSION, root_path=settings.ROOT_PATH, lifespan=lifespan)
app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
                   allow_methods=['*'],
                   allow_headers=['*'],
                   allow_credentials=True)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.state.limiter = limiter


@app.get('/', summary='Документация', tags=['Docs'], response_class=HTMLResponse)
@limiter.limit('60/minute')
async def home(request: Request, response: Response):
    return RedirectResponse(f'{settings.ROOT_PATH}/docs/')


app.include_router(example_router)
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
