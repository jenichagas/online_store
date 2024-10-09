from product import Product
from client import Client
from store import Store

produto01 = Product("Blusa", 20, 7)
produto02 = Product("Calça", 30, 12)
produto03 = Product("Bermuda", 99, 10)
produto04 = Product("Tênis", 100, 122)
produto05 = Product("Moletom", 40, 140)
produto06 = Product("Meia", 19, 412)


client = Client("Jeniffer", "Rua da Travessia, 21", "jeni.c@gmail.com")
client2 = Client("Beatriz", "Alameda São João,21", "bea.ss@gmail.com")

client.add_product_cart(vars(produto01))
client.add_product_cart(vars(produto02))
client.add_product_cart(vars(produto03))
client.add_product_cart(vars(produto04))
client.add_product_cart(vars(produto05))
client.add_product_cart(vars(produto06))

client2.add_product_cart(vars(produto01))
client2.add_product_cart(vars(produto02))
client2.add_product_cart(vars(produto03))
client2.add_product_cart(vars(produto04))

client.remove_product_cart(produto01)
client.show_products_cart()

store = Store()

store.add_client(client)
store.add_client(client2)


store.process_order(client)
store.process_order(client2)





