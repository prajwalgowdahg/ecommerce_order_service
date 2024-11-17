from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session  # Importing synchronous Session
from order_service.database import get_db
from order_service.schemas import OrderCreate, OrderResponse, OrderUpdate
from order_service.services import create_order, get_order_by_id, update_order, delete_order
from order_service import models, database

app = FastAPI()

# Create the tables in the database
models.Base.metadata.create_all(bind=database.engine)

@app.post("/orders", response_model=OrderResponse)
def create_new_order(order: OrderCreate, db: Session = Depends(get_db)):
    print("HELLO HERE")
    """API to create a new order."""
    try:
        new_order = create_order(order, db)  # Calling synchronous service function
        return new_order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    """API to retrieve an order by its ID."""
    try:
        order = get_order_by_id(order_id, db)  # Calling synchronous service function
        if not order:
            raise HTTPException(status_code=404, detail="Order not found")
        return order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/orders/{order_id}", response_model=OrderResponse)
def update_existing_order(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    """API to update an existing order."""
    try:
        updated_order = update_order(order_id, order_update, db)  # Calling synchronous service function
        if not updated_order:
            raise HTTPException(status_code=404, detail="Order not found")
        return updated_order
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/orders/{order_id}")
def cancel_order(order_id: int, db: Session = Depends(get_db)):
    """API to cancel an order."""
    try:
        result = delete_order(order_id, db)  # Calling synchronous service function
        if not result:
            raise HTTPException(status_code=404, detail="Order not found")
        return {"status": "success", "message": "Order cancelled successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
