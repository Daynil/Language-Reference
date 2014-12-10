class Fruit(object): # Can omit object if no inheritance
    """ A class that makes various tasty fruits. """
    is_alive = True # Member (of class) variable
    def __init__(self, name, color, flavor, poisonous):
        # Instance variables
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print("I'm a {0} {1} and I taste {2}.".format(self.color, self.name,
        self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible.")
        else:
            print("Don't eat me! I'm super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
lemon.is_edible()
print("Is {0} alive? {1}".format(lemon.name, Fruit.is_alive))

# Looping
for each in range(1, 5):
    print(each)

aList = [1, 2, 5, 9, 12]
for item in aList:
    if item in [2, 4, 6, 8, 10, 12]:
        print(item)

# List comprehension
""" Read: add (x+1) to the list for each value in the range of 5
if the item is evenly divisible by 2 (even number) """
bigList = [x+1 for x in range(5, 9) if x%2 == 0]
print(bigList)

# Dictionary aka hash/hashmap
newDict = {
        "key" : 6,
        "name" : "Danny"
    }

# Lambdas (anonymous functions)
my_list = range(16) #range is a function that generates a list (array)
"""Filter takes an anonymous function (block/lambda) as the argument -
tells it how to filter the list, which is the second argument"""
print(filter(lambda x: x % 3 == 0, my_list))
