
products = []
while True:
    name = input('please enter the name of product: ')
    if name == 'q': #quit
        break
    price = input('please enter the price: ')
    p = (name , price)
    products.append(p)
print(products) 

for p in products:
    print(p[0], '$', p[1])

with open('products.txt', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
