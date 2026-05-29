from fastapi import HTTPException


class OrderService:
    def __init__(
        self,
        repository,
        discount_service,
        payment_gateway,
    ):
        self.repository = repository
        self.discount_service = discount_service
        self.payment_gateway = payment_gateway

    def process_order(self, purchase_request):

        product = self.repository.find_by_name(
            purchase_request.produto
        )

        if not product:
            raise HTTPException(
                status_code=404,
                detail="Produto não encontrado"
            )

        if product["estoque"] <= 0:
            raise HTTPException(
                status_code=400,
                detail="Sem estoque"
            )

        final_value = (
            self.discount_service.apply_discount(
                product["preco"],
                purchase_request.cupom,
            )
        )

        if final_value <= 0:
            raise HTTPException(
                status_code=400,
                detail="Valor inválido"
            )

        approved = self.payment_gateway.charge(
            purchase_request.cartao,
            final_value,
        )

        if not approved:
            raise HTTPException(
                status_code=400,
                detail="Pagamento recusado"
            )

        self.repository.decrease_stock(
            purchase_request.produto
        )

        return {
            "status": "sucesso",
            "mensagem": "Compra aprovada!",
            "valor_pago": final_value,
        }