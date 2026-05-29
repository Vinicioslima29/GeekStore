class ProductRepository:

    def __init__(self, database):
        self.database = database

    def list_all(self):

        connection = self.database.connect()

        products = connection.execute(
            """
            SELECT * FROM produtos
            """
        ).fetchall()

        connection.close()

        return [
            dict(product)
            for product in products
        ]

    def find_by_name(
        self,
        name: str
    ):

        connection = self.database.connect()

        product = connection.execute(
            """
            SELECT * FROM produtos
            WHERE nome = ?
            """,
            (name.lower(),)
        ).fetchone()

        connection.close()

        return product

    def decrease_stock(
        self,
        name: str
    ):

        connection = self.database.connect()

        connection.execute(
            """
            UPDATE produtos
            SET estoque = estoque - 1
            WHERE nome = ?
            """,
            (name.lower(),)
        )

        connection.commit()

        connection.close()