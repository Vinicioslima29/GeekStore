from unittest.mock import Mock

from pytest_bdd import (
    scenarios,
    given,
    when,
    then,
)

from app.repositories.product_repository import (
    ProductRepository,
)

from app.services.discount_service import (
    DiscountService,
)

from app.services.order_service import (
    OrderService,
)

from app.models.purchase import (
    PurchaseRequest,
)

scenarios("../compra.feature")


@given(
    'que existe um produto "teclado"',
    target_fixture="context"
)
def context(test_database):

    repository = ProductRepository(
        test_database
    )

    discount_service = (
        DiscountService()
    )

    mock_gateway = Mock()

    mock_gateway.charge.return_value = (
        True
    )

    order_service = OrderService(
        repository,
        discount_service,
        mock_gateway,
    )

    request = PurchaseRequest(
        produto="teclado",
        cartao="123",
        cupom="GEEK20",
    )

    return {
        "service": order_service,
        "request": request,
    }


@when("eu realizo a compra")
def make_purchase(context):

    context["result"] = (
        context["service"]
        .process_order(
            context["request"]
        )
    )


@then("a compra deve ser aprovada")
def validate_purchase(context):

    assert (
        context["result"]["status"]
        == "sucesso"
    )