class Order:
    def __init__(self, client, cart) -> None:
        self.client = client
        self.cart = cart
        self.status = "Pendente"
        self.total = 0

    def calculate_total(self):
        self.total = sum([product['price'] for product in self.cart])


    def finalize_order(self):
        self.calculate_total()
        self.status = "Concluido"
        print(f"Pedido finalizado {self.client.name}, total a pagar R${self.total}")


        