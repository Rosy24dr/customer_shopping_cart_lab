
class Products_In_Cart:

    def __init__(self):
        self.list_of_products = []

    def adding_new_product(self,item):
        self.list_of_products.append(item)
        print(self.list_of_products)

    def total_products(self):
        product_amount = len(self.list_of_products)
        print(product_amount)
        
    def emptying_list(self):
        self.list_of_products.clear()
        print(self.list_of_products)
        
     

