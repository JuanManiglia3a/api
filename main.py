from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.blobs import blob_routes
# from routes.containers import container_routes

app = FastAPI()

@app.get("/")
def home():
    return RedirectResponse('/docs')


app.include_router(blob_routes, prefix="/storage/blob")
# app.include_router(container_routes, prefix="/storage/container")