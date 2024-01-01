# Gather users holiday details and store to variables
city_flight = input("Which city will you be visiting? Please enter a,b or c:\n(a) Barcelona\n(b) Berlin\n(c) Paris\n ").lower()
num_nights = int(input("How many nights will you be staying? "))
rental_days = int(input("How many days car rental are required? "))

# Defining functions to calculate costs
def hotel_cost(num_nights):
    cost_night = 0
    if city_flight == 'a':
        cost_night = 120.00
    elif city_flight == 'b':
        cost_night = 99.00
    else:
        cost_night = 110.00
    
    return num_nights * cost_night

def plane_cost(city_flight):
    cost = 0
    if city_flight == 'a':
        cost = 75.00
    elif city_flight == 'b':
        cost = 65.00
    else:
        cost = 55.00

    return cost

def car_rental(rental_days):
    rent = 35.00
    return rental_days * rent

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost, plane_cost, car_rental, (hotel_cost + plane_cost + car_rental)

# Create variables to store our individual costs for displaying breakdown
h_cost, p_cost, c_rental, total_cost = holiday_cost(hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))

# Output our holiday costs neatly for user
print("=========================================")
print("Here is the cost breakdown for your trip:")
print("Hotel Cost: " + str(h_cost))
print("Flight Cost: " + str(p_cost))
print("Car rental: " + str(c_rental))
print("--------------------------")
print("Total Cost: " + str(total_cost))
print("--------------------------")