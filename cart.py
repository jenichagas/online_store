class ShopCart:

  def __init__(self) -> None:
      self.products = []

  def add_products(self, product):
      self.products.append(product)
  
  def remove_products(self, product):
      if product in self.products:
        self.products.remove(product)
  
  def total_value(self):
      return sum([product.price for product in self.products])
  
  def show_product_cart(self):
      for product in self.cart:
        product.product_information()
  