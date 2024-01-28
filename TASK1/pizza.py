def price(tuesday: bool, pizzas: int, delivery: bool, via_app: bool) -> float:
   
    pizza_price = 12
    delivery_cost = 2.5 if pizzas < 5 and delivery else 0
    
    total_price = pizzas * pizza_price
   
    if tuesday:
        total_price *= 0.5

    if via_app:
        total_price *= 0.75
    
    total_price = total_price + delivery_cost
    return total_price

print("BPP Pizza Price Calculator")
print("==========================")

#number of pizzas
pizzas = -1
while pizzas <= 0:
    try:
        pizzas = int(input("How many pizzas would you like to order? "))
        if pizzas < 0:
            print("Please enter a positive integer!")
    except ValueError:
            print("Please enter a number!")

#if its tuesday
while True:
    tuesday = input("Is it Tuesday? ")
    if tuesday.lower() == "y":
        break
    elif tuesday.lower() == "n":
                break
    else:
        print('Please answer "y" or "n".')
                
#if delivery is needed              
while True:
    delivery = input("Is delivery required? ")
    if delivery.lower() == "y":
        break
    elif delivery.lower() == "n":
        break
    else:
        print('Please answer "y" or "n".')
                
                
while True:
    via_app = input("Did the customer use the app? ")
    if via_app.lower() == "y":
        break
    elif via_app.lower() == "n":
        break
    else:
        print('Please answer "y" or "n".')

# Calculate and display the total price
total_price = price(tuesday.lower() == "y", pizzas, delivery.lower() == "y", via_app.lower() == "y")
print(f"\n{f'Total Price: £{total_price:.2f}':}")
