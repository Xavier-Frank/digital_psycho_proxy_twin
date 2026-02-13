from fastapi import FastAPI
from app.psych_proxy.model import run_psych_proxy

app = FastAPI()

@app.post("/psych-proxy")
def psych_proxy(user_id: str, session: dict):
    return run_psych_proxy(user_id, session)
