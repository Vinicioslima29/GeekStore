from pydantic import BaseModel
from typing import Optional


class PurchaseRequest(BaseModel):
    produto: str
    cartao: str
    cupom: Optional[str] = ""