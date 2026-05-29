from fastapi import APIRouter

router = APIRouter()


@router.post("/api/comprar")
def buy_product(request, order_service):
    return order_service.process_order(request)