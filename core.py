from fastapi import FastAPI
from routers.auth import router_auth

app = FastAPI()
app.include_router(router_auth)


@app.get("/")
async def home():
    return {"message": "Assalomu Aleykum Home pagega xush kelibsiz!"}
