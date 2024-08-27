from fastapi import FastAPI
from routers.auth import router_auth
from routers.order_router import order_router
from routers.product_router import product_router

app = FastAPI()
app.include_router(router_auth)
app.include_router(product_router)
app.include_router(order_router)


@app.get("/")
async def home():
    return {"message": "Assalomu Aleykum Home pagega xush kelibsiz!"}
