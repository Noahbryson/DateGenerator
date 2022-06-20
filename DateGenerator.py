from ExcelReader import getSheet
import pandas as pd
import numpy as np
import os
import random

class DateGenerator():
    def __init__(self,
        filePath: str):
        self.eat = False
        self.drink = False
        self.act = False
        self.place = False
        self.filename = filePath
        self.data = 'No Data Yet'

    def eatFlagT(self):
        self.eat = True
    def drinkFlagT(self):
        self.drink = True
    def actFlagT(self):
        self.act = True
    def placeFlagT(self):
        self.place = True

    def eatFlagF(self):
        self.eat = False
    def drinkFlagF(self):
        self.drink = False
    def actFlagF(self):
        self.act = False
    def placeFlagF(self):
        self.place = False

    def randEat(self):
        data = self.data[self.keys[0]]
        rand = random.randrange(len(data))
        return data[rand]
    def randDrink(self):
        data = self.data[self.keys[1]]
        rand = random.randrange(len(data))
        return data[rand]
    def randActivitiy(self):
        data = self.data[self.keys[2]]
        rand = random.randrange(len(data))
        return data[rand]
    def randPlace(self):
        data = self.data[self.keys[3]]
        rand = random.randrange(len(data))
        return data[rand]
    def getData(self):
        self.data, self.keys = getSheet(self.filename)
    def generate(self):
        dateNight = []
        if self.eat:
            event = self.randEat()
            dateNight.append("Restaurant: %s" % event)
        if self.drink:
            event = self.randDrink()
            dateNight.append("Bar: %s" % event)
        if self.act:
            event = self.randActivitiy()
            dateNight.append("What to do: %s" % event)
        if self.place:
            event = self.randPlace()
            dateNight.append("Where to go: %s" % event)
        return dateNight


