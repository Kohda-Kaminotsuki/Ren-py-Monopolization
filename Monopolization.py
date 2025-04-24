# imports random for rng
import random
import math
# Test line to make sure renpy script is importing this file correctly.
testme = "yup"

# Configurations for the game:
utility_cost = 5 # Cost per die number for utility.
ratio_rent = 10 # Rent is Cost / ratio_rent default is Rent = Cost/10
ratio_mortgage = 2 # Ratio of how much a player recieves with a mortgage versus the cost of the property. Mortgage = Cost/ratio_mortgage default is Mortgage = Cost/2
building_cost_house = 50 # Cost of house in units of currency per house based on side of board property is on.
building_cost_hotel = 100 # Cost of hotel in units of currency per hotel
hotel_count = 12 # Number of hotels available in the game. This is a hard cap on the number of hotels that can be built.
spaces = 36 # Number of spaces on the board, check used for preventing script from going above this number. 

# This is a 2 d6 roll function. It gives higher weights to middle numbers instead of equal chances for all numbers 2-12.
def roll():
    return random.randint(1, 6) +random.randint(1, 6)

class BOARDSPACE:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.playerlist = []


class REALESTATE(BOARDSPACE):
    
    def._init__(self, name, cost, location, section):
        super().__init__(name, location)
        self.name = name
        self.cost = cost
        self.buildings = 0 # 0 is no buildings, 1-4 is number of houses, 5 is hotel.
        self.mortgaged = False
        self.location = location # 0 is start, 1-{spaces-1} can be used for anything
        self.owner = None
        self.rent = cost / ratio_rent
        self.mortgage = cost / ratio_mortgage
        self.building_cost = (math.ceil(location/(spaces/4))) * building_cost_house 
        self.hotel_cost = (math.ceil(location/(spaces/4))) * building_cost_hotel
    def rent(self):
        pass
class UTILITY(BOARDSPACE):

    def.__init__(self, name, cost, location):
        super().__init__(name, location)
        self.name = name
        self.cost = cost
        self.location = location
        self.mortgaged = False
        self.owner = None
        self.mortgage = cost / ratio_mortgage
    def rent(self, roll):
        return roll * utility_cost
