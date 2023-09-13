#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    name = ""
    job = ""

    def getName(self):
        return self.name
    def setName(self, name):
        if (type(name) == str and len(name) >= 1 and len(name) <= 25):
            titleCasingName = name.split()
            titleCasingName = (word.capitalize() for word in titleCasingName)
            titleCasingName = ' '.join(titleCasingName)
            self.name = titleCasingName
        else:
            print("Name must be string between 1 and 25 characters.")

    def getJob(self):
        return self.job
    def setJob(self, job):
        if job in APPROVED_JOBS:
            self.job = job
        else:
            print("Job must be in list of approved jobs.")

    def __init__(self, name="Person", job="Admin"):
        self.setName(name)
        self.setJob(job)