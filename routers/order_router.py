from fastapi import APIRouter, status
from more_itertools.recipes import quantify

from models import Order, User, Product
from database import Session, ENGINE
from schemas import OrderCreateModel, OrderListModel
from fastapi.exceptions import HTTPException

order_router = APIRouter(prefix="/orders", tags=["orders"])

session = Session(bind=ENGINE)


@order_router.get("/")
async def orders():
    orders = session.query(Order).all()
    return orders


@order_router.get("/")
async def order_user(user_id: int):
    check_user = session.query(User).filter(User.id == user_id).first()
    if check_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    user_orders = session.query(Order).filter_by(user_id=user_id).all()
    return user_orders


@order_router.post("/")
async def order_create(order: OrderCreateModel):
    check_id = session.query(Order).filter_by(Order.id == order.id).first()
    if check_id is None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order already exists")

    check_user_id = session.query(User).filter_by(User.id == order.user_id).first()
    if check_user_id is None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User does not exist")

    product_check_id = session.query(Product).filter_by(Product.id == order.product_id).first()
    if product_check_id is None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Product does not exist")

    new_order = Order(
        id=order.id,
        count=order.count,
        user_id=order.user_id,
        product_id=order.product_id,

    )
    session.add(new_order)
    session.commit()
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="Order created successfully")
