from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    product_id: int
    quantity: int
    total_amount: float

class OrderResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_amount: float
    payment_status: str
    order_status: str

    class Config:
        orm_mode = True
class OrderUpdate(BaseModel):
    quantity: Optional[int]
    status: Optional[str]