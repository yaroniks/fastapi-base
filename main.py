from app import limiter
from app.routers import *
from config import settings
from app.database.base import async_main
from app.database.redis import redis_service
from app.utils.rabbitmq import RabbitMQExample

import uvicorn
import aiohttp
from fastapi import FastAPI
from contextlib import asynccontextmanager
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run at startup
    await async_main()
    app.state.session = aiohttp.ClientSession()
    await redis_service.connect()
    yield
    # Run on shutdown
    await app.state.session.close()
    await redis_service.close()
    RabbitMQExample().close_rabbitmq()


app = FastAPI(title=settings.TITLE, version=settings.VERSION, root_path=settings.ROOT_PATH, lifespan=lifespan)  # , docs_url=None, redoc_url=None, openapi_url=None
app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
                   allow_methods=['*'],
                   allow_headers=['*'],
                   allow_credentials=True)
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.state.limiter = limiter


app.include_router(example_router)
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0')
