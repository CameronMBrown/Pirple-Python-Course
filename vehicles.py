# Pirple Assignment 9 - Classes

import random

class Vehicle:
  def __init__(self, make, model, year, weight):
    self.make = make
    self.model = model
    self.year = year
    self.weight = weight
    self.needsMaintenance = False
    self.tripsSinceMaintenance = 0

  def repair(self):
    self.needsMaintenance = False
    self.tripsSinceMaintenance = 0

  def __str__(self):
    return "Make: " + self.make + ", Model: " + self.model + ", Year: " + str(self.year) + ", Weight: " + str(self.weight) + "lbs, Needs Maintenance: " + str(self.needsMaintenance) + ", Trips Since Maintenance: " + str(self.tripsSinceMaintenance)

class Car(Vehicle):
  def __init__(self, make, model, year, weight):
    Vehicle.__init__(self, make, model, year, weight)
    self.isDriving = False

  def drive(self):
    self.isDriving = True

  def stop(self):
    self.isDriving = False
    self.tripsSinceMaintenance += 1
    if(self.tripsSinceMaintenance > 100):
      self.needsMaintenance = True


class Plane(Vehicle):
  def __init__(self, make, model, year, weight):
    Vehicle.__init__(self, make, model, year, weight)
    self.isFlying = False

  def fly(self):
    if self.needsMaintenance:
      print(self.model + " cannot fly until it is repaired.")
      return False
    else:
      self.isFlying = True

  def land(self):
    self.isFlying = False
    self.tripsSinceMaintenance += 1
    if self.tripsSinceMaintenance > 100:
      self.needsMaintenance = True



lambo = Car("Lamborghini", "Huracan", 2021, 3618)
subi = Car("Subaru", "Outback", 2016, 3937)
iceCreamTruck = Car("Ford", "e-350", 2015, 4773)
cars = [lambo, subi, iceCreamTruck]

cessna = Plane("Cessna", "172 Skyhawk", 1960, 2220)
blackHawk = Plane("Sikorsky", "UH-60 Black Hawk", 1985, 12511)
dreamLiner = Plane("Boing", "787 Dreamliner", 2013, 500000)
planes = [cessna, blackHawk, dreamLiner]

def drivingSimulator(trips):
  print("Start your engines!")
  for _ in range(trips):
    car = random.choice(cars)
    car.drive()
    # some time passes
    car.stop()
  for c in cars:
    print(str(c))

def flyingSimulator(trips):
  print("ready for take-off!")
  for _ in range(trips):
    plane = random.choice(planes)
    plane.fly()
    # some time passes
    if plane.isFlying:
      plane.land()
    else:
      print("repairing " + plane.model)
      plane.repair()
  for p in planes:
    print(str(p))

drivingSimulator(300)
flyingSimulator(300)