# Defines cars variable as 100
cars = 100
# Defines space in a car as 4.0 people
space_in_a_car = 4.0
# Defines number of drivers
drivers = 30
# Defines number of passengers
passengers = 90
# Defines number of cars not used by subtracting cars from drivers
cars_not_driven = cars - drivers
# Defines number od driven cars by using the number of drivers
cars_driven = drivers
# Defines the capacity of a carpool car as the cars driven multiplied by
# the space in a car
carpool_capacity = cars_driven * space_in_a_car
# Defines the passengers in a car by dividing the total passengers by the total
# cars driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We can tranport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
