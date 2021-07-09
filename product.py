import os # operating sysytem

products = []
if os.path.isfile('products.csv'):
    print('yeah! found the file!')
    #read files
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if 'name, price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
else:
    print('no files...')

#input
while True:
    name = input('please enter the name of product: ')
    if name == 'q': #quit
        break
    price = input('please enter the price: ')
    price = int(price)
    p = (name , price)
    products.append([name, price])
print(products) 

for p in products:
    print(p[0], 'is $', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('Name, Price\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')





