class Client:
    def __init__(self, name: str, address: str, email: str) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.cart = []

    def add_product_cart(self, product):
        self.cart.append(product)
    
    def remove_product_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)

    def show_products_cart(self):
      print(f"Carrinho de {self.name}")
      for product in self.cart:
        print(f"Produto: {product['name']}, Preço: R${product['price']}")