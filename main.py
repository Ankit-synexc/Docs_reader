# main.py
from fastapi import FastAPI
from routers import docs_routes
import uvicorn

app = FastAPI()

app.include_router(docs_routes.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)