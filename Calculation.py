# Calculation for route one -> to friend's house:

fuel_price = float(input("Enter the fuel price: "))
distance = float(input("Enter the distance: ")) # km
car_consume = float(input("Enter the car consumme: ")) # km/l
days = int(input("Enter the number of days: ")) 

liters_consumed_per_day = distance / car_consume

liters_consumed_in_x_days = liters_consumed_per_day * days

total_cost_route_one = liters_consumed_in_x_days * fuel_price

# Calculation for route two -> to Puc-GO:

distance = float(input("Enter the distance: ")) # km

liters_consumed_per_day = distance / car_consume

liters_consumed_in_x_days = liters_consumed_per_day * days

total_cost_route_two = liters_consumed_in_x_days * fuel_price

total_cost_route_two = total_cost_route_two / 2

total_cost = total_cost_route_one + total_cost_route_two

print(f"the total expense in {days} days will be: {total_cost:.2f}")