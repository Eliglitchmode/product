import os # operating system
# Read File
products = []
if os.path.isfile('products.csv'): #Check if the file is existing
	print('yeah! I found it!')
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if 'Product, Price' in line:
				continue #Jump to next loop and skip the current one 
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)

else:
	print('Not found....')

#Two-dimensional list
#Let user input the price & product
while True:
	name = input('Please enter the name of the product: ')
	if name == 'q':  #exit
		break
	price = input('Please enter the price: ')
	price = int(price)
#	p = []
#	p.append(name)
#	p.append(price)
# 	can be written as follows:
#	p = [name, price]
	products.append([name, price])
print(products)

#Print all purchases
for p in products:
	print('The price of ',p[0],'is ', p[1])

#Write into the file
# Use encoding='utf-8' can prevent language not showing properly
with open('products.csv', 'w', encoding='utf-8') as f:   #with --> help auto-close the file after written
	f.write('Product, Price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')