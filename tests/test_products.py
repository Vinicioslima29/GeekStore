from app.repositories.product_repository import (
    ProductRepository,
)


def test_list_products(
    test_database
):

    repository = ProductRepository(
        test_database
    )

    products = repository.list_all()

    assert len(products) > 0

    assert products[0]["nome"] == (
        "teclado"
    )