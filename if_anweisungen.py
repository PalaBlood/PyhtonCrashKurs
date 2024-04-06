available_toppings = ["mushrooms", "cheese", "green peppers", 
                      "pepperoni", "pineapple"]

requested_toppings = ["mushrooms", "salami", "pepperoni"]

for request_topping in requested_toppings:
    if request_topping in available_toppings:
        print(f"Adding {request_topping} :)")
    else:
        print(f"Sorry we dont have {request_topping} in our house today")
        



