import config
import uvicorn
from app.routers import *
import app.common.schemas as schemas
from contextlib import asynccontextmanager
from app.database.database import async_main
from fastapi import FastAPI, Request, Response
from starlette.responses import RedirectResponse, JSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run at startup
    await async_main()
    yield
    # Run on shutdown


app = FastAPI(title=config.TITLE, version=config.VERSION, root_path='/api/v1', lifespan=lifespan)


@app.get('/', summary='Документация', tags=['Docs'])
async def home(request: Request):
    return RedirectResponse('/api/v1/docs/')


app.include_router(r1)
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
