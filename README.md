Fuel Cost Calculator This script was created to calculate the fuel cost for commuting between my house, my friend's house, and our university.

How it works: The script requires the following inputs:

fuel_price – Price of fuel in R$ (Brazilian currency)

distance – Distance in kilometers (from my house to my friend's house)

car_consume – Car fuel consumption in km/l (kilometers per liter)

days – Number of days the route will be taken

These initial inputs are used to calculate the fuel cost for the route between my house and my friend's house.

After that, you input another:

distance – Distance in kilometers from my friend's house to the university

This second distance is divided by 2, since this part of the trip is shared between the two of us — we both contribute equally to this portion of the fuel cost:

total_cost_route_two = total_cost_route_two / 2

Finally, the script sums the two parts to calculate the amount my friend will pay me.