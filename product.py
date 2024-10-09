class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def product_information(self):
        print(f"{self.name}, R${self.price}, Quantidade:{self.stock}")
    
    def reduce_stock(self, quantity_sold: int):
        if quantity_sold <= self.stock:
            self.stock -= quantity_sold
        else:
            print("Produto indisponível no momento")

    
      