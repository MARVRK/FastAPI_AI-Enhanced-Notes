from fastapi import FastAPI
from app.api.notes import router as api_router_notes
import uvicorn

app = FastAPI()

app.include_router(router=api_router_notes, prefix="/api")

if __name__ == '__main__':
    uvicorn.run("main:app")