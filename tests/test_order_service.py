from unittest.mock import Mock

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


def test_successful_purchase(
    test_database
):

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

    result = (
        order_service.process_order(
            request
        )
    )

    assert result["status"] == (
        "sucesso"
    )

    assert (
        result["valor_pago"]
        == 160.0
    )

    mock_gateway.charge.assert_called_once()