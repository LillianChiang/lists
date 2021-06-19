
products = []
while True:
    name = input('please enter the name of product: ')
    if name == 'q': #quit
        break
    price = input('please enter the price: ')
    p = [name, price]
    products.append(p)
print(products)

products[0][0]


