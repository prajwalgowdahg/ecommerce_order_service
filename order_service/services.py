import httpx
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from order_service import schemas,models
import random

PRODUCT_SERVICE_URL = "http://localhost:8001"
PAYMENT_SERVICE_URL = "http://localhost:8000"

def create_order(order: schemas.OrderCreate, db: Session):
    # Check product availability
    with httpx.Client() as client:
        product_response = client.get(f"{PRODUCT_SERVICE_URL}/products/{order.product_id}")
        if product_response.status_code != 200:
            raise Exception("Product not available")
        
        product_data = product_response.json()
        if product_data["stock"] < order.quantity:
            raise Exception("Insufficient stock")

    # Reserve product stock
    with httpx.Client() as client:
        reserve_response = client.post(f"{PRODUCT_SERVICE_URL}/products/reserve", json={
            "product_id": order.product_id,
            "quantity": order.quantity
        })
        if reserve_response.status_code != 200:
            raise Exception("Failed to reserve product stock")

    # Process payment
    with httpx.Client() as client:
        random_integer = random.randint(1, 10000)
        payment_response = client.post(f"{PAYMENT_SERVICE_URL}/payments/", json={
            "order_id": str(random_integer),
            "amount": order.total_amount,
            "currency": "USD",
            "payment_status": "success"

        })
        print(payment_response,"why")
        if payment_response.status_code != 200:
            raise Exception("Payment failed")

        payment_data = payment_response.json()
        payment_status = payment_data["payment_status"]

    # Create order in the database
    new_order = models.Order(
        product_id=order.product_id,
        quantity=order.quantity,
        total_amount=order.total_amount,
        payment_status=payment_status,
        order_status="completed" if payment_status == "success" else "failed"
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order

def get_order_by_id(order_id: int, db: Session):
    result = db.execute(select(models.Order).where(models.Order.id == order_id))
    return result.scalar_one_or_none()

def update_order(order_id: int, order_update, db: Session):
    order = get_order_by_id(order_id, db)
    if not order:
        return None
    if order_update.quantity:
        order.quantity = order_update.quantity
    if order_update.status:
        order.status = order_update.status
    db.add(order)
    db.commit()
    db.refresh(order)
    return order

def delete_order(order_id: int, db: Session):
    order = get_order_by_id(order_id, db)
    if not order:
        return None
    db.delete(order)
    db.commit()
    return True
