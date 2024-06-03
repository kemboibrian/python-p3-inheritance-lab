#!/usr/bin/env python

from user import User

class Student(User):
     def __init__(self, first_name, last_name, knowledge = []):
        self.first_name = first_name
        self.last_name = last_name
        self.knowledge = knowledge

     def learn(self, string):
        self.string = string
        return self.knowledge.append(self.string)