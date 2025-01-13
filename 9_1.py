class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0    

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type}")
    
    def open_restaurant(self):
        print("The restaurant is open")
    
    def display_number_served(self):
        print(f"Number served: {self.number_served}")

    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant('Chitos', 'fastfood')
restaurant2 = Restaurant('Buddys', 'fastfood')
restaurant3 = Restaurant('Yellow Lane', 'Italian')

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant.number_served = 100
restaurant.display_number_served()

restaurant.set_number_served(500)
restaurant.display_number_served()

restaurant.increment_number_served(200)
restaurant.display_number_served()
