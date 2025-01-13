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

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['cheese', 'mango', 'chocolate']
    
    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

ice_cream_stand = IceCreamStand('Ice Cream House', 'Dessert')
ice_cream_stand.display_flavors()
