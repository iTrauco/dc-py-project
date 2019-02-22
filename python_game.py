# establish hero/goblin class
# Added 'Hero' and 'Goblin' classes
class Goblin():
    def __init__(self, name, power, health): # defines function values of goblin class # respawn baseline stats 
        self.name = name #just name until defined later, called with ()
        self.power = power
        self.health = health

    def defend(self):
        return "%s defends itself." % (self.name)

    def health_status(self):
        return "You have %s power and %s health remaining." % (self.power, self.health)

class Hero(Goblin):    
    def __init__(self, name, power, health):  # defines function values of hero class
        self.name = name
        self.power = power #applies to all instances
        self.health = health #pass health and power top left

    def attack(self):
        return "%s, attacks  !" % (self.name)

    def hero_status(self):
        return super().health_status()

        ##make character
        
        
        #super().health_status() imports super class parameters + health status of goblin

# class Goblin():
#     def __init__(self, name, power, health): # defines function values of goblin class # respawn baseline stats 
#         self.name = name
#         self.power = power
#         self.health = health

    # def attack(self):


    #     #function belongs to goblin to do some kind of work

    # def attack(self):
    #     self.attack = Hero


        





# Extract code from hero into method hero.attack(goblin)<---feeds in goblin as parameter



# Extract code from hero into method hero.attack(goblin)<---feeds in goblin as parameter


# extract code from goblin into method goblin.attach(hero)<--- feeds in goblin as paramter