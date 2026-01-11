city_flight = input("enter your depature city (A/B?C): ").lower()
num_nights = float(input("enter number of night in hotel: "))
rental_days = float(input("enter days of rental car: "))

def hotel_cost(num_nights):
    total_cost = num_nights * 100
    return total_cost


def plane_cost(city_flight):
    if city_flight == "a":
        return 100
    elif city_flight == "b":
        return 200
    elif city_flight == "c":
        return 300
    else:
        return 400

def car_rental(rental_days):
    total_car_cost = rental_days * 50
    return total_car_cost
    

def holiday_cost(num_nights, city_flight, rental_days):
    hotel = hotel_cost(num_nights)
    flight = plane_cost(city_flight)
    car = car_rental(rental_days)
    total_cost = hotel + flight + car
    return total_cost

# call out the function:
hotel = hotel_cost(num_nights)
car = car_rental(rental_days)
flight = plane_cost(city_flight)
total_cost = holiday_cost(num_nights, city_flight, rental_days)

print("Your holiday total cost breakdown is: ")
print (f"Your flight cost: ${flight}")
print (f"Your car rental cost: ${car}")
print (f"Your hotel cost: ${hotel}")
print (f"total trip cost: ${total_cost}")
