class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes a {self.sound} sound."

    def eat(self):
        return f"{self.name} is eating."

    def sleep(self):
        return f"{self.name} is sleeping."


class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "moo")

    def produce_milk(self):
        return f"{self.name} is producing milk."


class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "cluck")

    def lay_egg(self):
        return f"{self.name} has laid an egg."


class Pig(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "oink")

    def roll_in_mud(self):
        return f"{self.name} is rolling in the mud."


# Example usage
cow = Cow("Bessie", 5)
chicken = Chicken("Clucky", 2)
pig = Pig("Porky", 3)

print(cow.make_sound())
print(cow.eat())
print(cow.produce_milk())

print(chicken.make_sound())
print(chicken.sleep())
print(chicken.lay_egg())

print(pig.make_sound())
print(pig.eat())
print(pig.roll_in_mud())
