# requested_topping = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_topping:
# 	if requested_topping == 'green peppers':
# 		print("Sorry, we are out of green peppers right now.")
# 	else:
# 		print(f"Adding {requested_topping}.")	
# if 'mushrooms' in requested_topping:
# 	print("Adding mushrooms.")
# elif 'pepperoni' in requested_topping:
# 	print("Adding pepperoni.")
# elif 'extra cheese' in requested_topping:
# 	print("Adding extra cheese.")

# print("\nFinished making your pizza!")		

available_toppings = ['mushrooms', 'olives', 'green peppers',
					  'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")		

print("\nFinished making your pizza!")