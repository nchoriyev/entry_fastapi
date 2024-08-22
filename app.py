from fastapi import FastAPI, APIRouter

login_router = APIRouter(prefix="/auth", tags=["auth"])


@login_router.get("/login")
async def login():
    return {"message": "Welcome to login page"}


@login_router.get("/register")
async def register():
    return {"message": "Welcome to register"}


@login_router.post("/password_require")
async def password_require():
    return {"message": "Welcome to password require"}
