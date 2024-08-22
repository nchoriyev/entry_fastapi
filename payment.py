from fastapi import APIRouter

router_payment = APIRouter(prefix="/payment", tags=["payment"])


@router_payment.get("/payment")
async def payment():
    return {"message": "Payment"}


@router_payment.get("/payment_status")
async def payment_status():
    return {"message": "Message about the status of payment"}


@router_payment.get("/payment_data")
async def payment_data():
    return {"message": "Payment data"}
