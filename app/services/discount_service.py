class DiscountService:
    def apply_discount(
        self,
        value: float,
        coupon: str
    ) -> float:

        if coupon == "GEEK20":
            return value * 0.8

        return value