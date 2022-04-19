#Two-dimensional list

products = []
while True:
	name = input('Please enter the name of the product: ')
	if name == 'q':  #exit
		break
	price = input('Please enter the price: ')
#	p = []
#	p.append(name)
#	p.append(price)
# 	can be written as follows:
#	p = [name, price]
	products.append([name, price])
print(products)

print(products[0][0])