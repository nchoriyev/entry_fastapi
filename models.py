from xmlrpc.client import Boolean

from database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    password = Column(Text, nullable=False)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f"User: {self.first_name} {self.last_name}"


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    price = Column(Integer)

    orders = relationship('Order', back_populates='product')

    def __repr__(self):
        return f"Product: {self.name}"


class Order(Base):
    __tablename__ = 'orders'

    OrderChoice = (
        ('PENDING', 'PENDING'),
        ('IN_PROGRESS', 'IN PROGRESS'),
        ('COMPLETED', 'COMPLETED')
    )

    id = Column(Integer, primary_key=True)
    count = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=OrderChoice), default='PENDING')
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))

    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')

    def __repr__(self):
        return f" Order status: {self.order_status}"
