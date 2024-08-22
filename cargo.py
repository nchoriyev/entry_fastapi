from fastapi import APIRouter

router_cargo = APIRouter(prefix="/cargo", tags=["cargo"])


@router_cargo.post("/delivery")
async def delivery():
    return {"message": "Delivery cargo"}


@router_cargo.get("/orders")
async def orders():
    return {"message": "all orders"}


@router_cargo.get("/order_story")
async def order_story():
    return {"message": "Stories of orders"}