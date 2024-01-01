# Create a list to contain four menu items for the Cafe
menu = ["Tea", "Scone", "Panini", "Cake"]

# Create a dictionary to manage stock levels and one for prices
stock = {'Tea': 10, 'Scone': 12, 'Panini': 15, 'Cake': 8}
price = {'Tea': 1.75, 'Scone': 2.25, 'Panini': 3.50, 'Cake': 2.50}


# Calculate the total stock value within the cafe
stock_value = 0

for i in menu:
    item_value = stock[i] * price[i]
    stock_value += item_value

print(stock_value)