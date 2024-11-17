from sqlalchemy import Column, Integer, String, Float, ForeignKey
from order_service.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    quantity = Column(Integer, nullable=False)
    total_amount = Column(Float, nullable=False)
    payment_status = Column(String, nullable=False)
    order_status = Column(String, nullable=False, default="pending")
