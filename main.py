from shop.cart import Cart
from shop.order import Order


# ------ CUSTOMER ------ 
# create cart
adam = Cart("Adam")

# customer add item
adam.add("apple")
adam.add("orange")
adam.add("pineapple")
adam.add("durian")

# get cart status
print(adam)

# get dictionary
print(adam.cart)

# change customer
adam.name ="Adrain"

# access dictionary
print(adam.cart["name"])
print(adam.cart["basket"][0])

# update dict value by key
# adam.cart["name"] = "Adele" # readable but not changeable
adam.cart["basket"][0] = "kiwi"
adam.cart["basket"].pop(1)

# get item by index
print(adam[2])

# update item by index
adam[2] = "guava"

# get dictionary after modification
print(adam.cart)


# ------ SHOP ------
# create order list
daily_order = Order()

# add customes to order list
customers = [
    {"name": "Elle", "basket": ["carrot", "spinach", "tomato"]},
    {"name": "Francis", "basket": ["detergent", "toothbrush"]},
    {"name": "Gale", "basket": ["bread", "milk", "cereal", "juice"]},
            ]
for customer in customers:
    new_customer = Cart(customer["name"])
    for item in customer["basket"]:
        new_customer.add(item)
    daily_order.add_order(new_customer)
    # print(new_customer.cart)

# show order list
daily_order.output_list()

# delete order list
daily_order.cancel_order(2)
daily_order.output_list()