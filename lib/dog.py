#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    name = ""
    breed = ""
    def getName(self):
        return self.name
    def setName(self, name):
        if (type(name) == str and len(name) >= 1 and len(name) <= 25):
            self.name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    def getBreed(self):
        return self.breed
    def setBreed(self, breed):
        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    def __init__(self, name="Dog", breed="Pointer"):
        self.setName(name)
        self.setBreed(breed)


fido = Dog(name="Fido")
print(fido.getName())