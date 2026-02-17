from fastapi import FastAPI
from app.controller.psych_proxy_api import router as psych_proxy_router

app = FastAPI(title="Digital Twin: Psychological Proxy Twin",)

app.include_router(psych_proxy_router)

@app.get("/")
def root():
    return {"status": "Psychological Proxy Twin API running"}
