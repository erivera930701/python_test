class Cake:
    recipe_type = "Basic Cake"
    baking_temperature = 180
    baking_time = 30

    def __init__(self, flour, sugar, milk, eggs):
        self.cake_flour = flour
        self.cake_sugar = sugar
        self.cake_milk = milk
        self.cake_eggs = eggs

    def mix_ingredients(self):
        print(
            f"Mixing {self.cake_flour} grams of flour, {self.cake_sugar} grams of sugar, {self.cake_milk} ml of milk, and {self.cake_eggs} eggs.")

    def bake(self):
        print(f"Baking the cake at {self.baking_temperature}°C for {self.baking_time} minutes.")

    def serve(self):
        print("Serving the cake with decoration.")


class Bakery:
    def __init__(self, name):
        self.bakery_name = name

    def prepare_cake(self, cake):
        print(f"Preparing a cake at {self.bakery_name}.")
        cake.mix_ingredients()
        cake.bake()
        cake.serve()


# Create instances of Cake with specific ingredients: flour, sugar, milk, eggs in order
cake_1 = Cake(200, 200, 240, 2)
cake_2 = Cake(200, 150, 220, 2)

# Create an instance of a Bakery named 'TripleTen Bakery'
bakery_1 = Bakery("TripleTen Bakery")

# Use the Bakery instance to prepare the cake_1
bakery_1.prepare_cake(cake_1)