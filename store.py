from order import Order

class Store:
    def __init__(self) -> None:
        self.products = []
        self.client = []
        self.orders = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def add_client(self, client):
        self.client.append(client)

    def process_order(self, client):
        order = Order(client, client.cart)
        self.orders.append(order)
        order.finalize_order()

    
        








