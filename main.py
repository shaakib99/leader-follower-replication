from fastapi import FastAPI, APIRouter
from common.middlewares.request_middleware import RequestMiddleware
async def lifespan(app):
    yield

app = FastAPI(lifespan=lifespan)

routers: list[APIRouter] = []
for router in routers:
    app.include_router(router)


app.add_middleware(RequestMiddleware, excluded_endpoints=["/metrics"])

@app.get("/")
async def root():
    return {"message": "Hello World"}