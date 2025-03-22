import uvicorn
from app.routers import *
from config import settings
import app.database.requests as req
import app.common.schemas as schemas
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Response, HTTPException, status
from starlette.responses import RedirectResponse, JSONResponse, HTMLResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run at startup
    yield
    # Run on shutdown


app = FastAPI(title=settings.TITLE, version=settings.VERSION, root_path='/api/v1', lifespan=lifespan)


@app.get('/', summary='Документация', tags=['Docs'], response_class=HTMLResponse)
async def home(request: Request, response: Response):
    return RedirectResponse('/api/v1/docs/')


app.include_router(r1)
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
