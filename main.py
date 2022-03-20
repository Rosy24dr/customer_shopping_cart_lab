from shopping_cart import Products_In_Cart
from customer import Customer

customer_shopping = Products_In_Cart()

customer_shopping.adding_new_product('Baby food')
customer_shopping.adding_new_product('Juice')
customer_shopping.adding_new_product('Chocolate')

customer_shopping.total_products()

customer_shopping.emptying_list()

customer = Customer('Rosy')
print(customer.name)

