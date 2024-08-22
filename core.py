from fastapi import FastAPI
from app import login_router
from cargo import router_cargo
from payment import router_payment

app = FastAPI()
app.include_router(login_router)
app.include_router(router_cargo)
app.include_router(router_payment)


@app.get("/")
async def home():
    return {"message": "Assalomu Aleykum Home pagega xush kelibsiz!"}


@app.get("/userinfo")
async def userinfo():
    return {"username": "Mustafo", "email": "gmail.com", "password": "1234"}


