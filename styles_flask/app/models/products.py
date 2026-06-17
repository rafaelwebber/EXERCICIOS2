from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    prices: float
    description: Optional[str] = None
    stock: int
    sku: str