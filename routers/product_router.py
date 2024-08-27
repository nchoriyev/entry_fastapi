from fastapi import APIRouter, status
from models import Product
from database import Session, ENGINE
from routers.auth import session
from fastapi.exceptions import HTTPException
from schemas import ProductListModel, ProductCreateModel

product_router = APIRouter(prefix="/products", tags=["products"])

session = Session(bind=ENGINE)


@product_router.get("/")
async def products():
    products = session.query(Product).all()
    return products


@product_router.post("/")
async def create_product(product: ProductCreateModel):
    check_id = session.query(Product).filter(Product.id == product.id).first()
    if check_id is None:
        return {"message": "Product id is exist"}
    new_product = Product(
        id=product.id,
        name=product.name,
        price=product.price

    )
    session.add(new_product)
    session.commit()
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="Product created successfully")


