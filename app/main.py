from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.core.database import (
    Database,
    DatabaseInitializer,
)

from app.repositories.product_repository import (
    ProductRepository,
)

from app.services.discount_service import (
    DiscountService,
)

from app.services.payment_service import (
    PaymentGateway,
)

from app.services.order_service import (
    OrderService,
)

from app.models.purchase import (
    PurchaseRequest,
)

app = FastAPI()


database = Database()

initializer = DatabaseInitializer(database)

repository = ProductRepository(database)

discount_service = DiscountService()

payment_gateway = PaymentGateway()

order_service = OrderService(
    repository,
    discount_service,
    payment_gateway,
)


@app.on_event("startup")
def startup_event():
    initializer.initialize()


@app.get("/api/produtos")
def get_products():
    return repository.list_all()


@app.post("/api/comprar")
def purchase_product(
    request: PurchaseRequest
):
    return order_service.process_order(
        request
    )


@app.get(
    "/",
    response_class=HTMLResponse
)
def home_page():

    with open(
        "app/static/index.html",
        encoding="utf-8",
    ) as file:

        return file.read()