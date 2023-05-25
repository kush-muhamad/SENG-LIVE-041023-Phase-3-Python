#!/usr/bin/env python3
# Demonstrate classes 
# 1. ✅ Create a Pet class
# 2. ✅ Instantiate a few pet instance 
    # Compare the pet instances to demonstrate they are not the same object
    # Note: add 'pass' to the pet class 

import ipdb

#1. define a pet class
#class keyword
# class Pet: #UpperCamelCase #PascalCase

#     pass

# ipdb.set_trace()

# baboi = Pet()  # instantiate a new instance 
# fiona = Pet()
# beau = Pet()
# winnie = Pet()
# chloe = Pet()
# moseph = Pet()
# beau            # calling the instance  
# <__main__.Pet object at 0x106c61160> #instance detail 

# ipdb> winnie == chloe
# False

# winnie and chloe are not the same. They are different objects in memory 
# they are coming the same source, Pet class


# 3. ✅ Demonstrate __init__ 
    # Add arguments to instances  
    # use dot notation to access their attributes 
    # update attributes with new values 

#Attributes :
    # name
    # age
    # breed
    # temperament


class Pet:
    # initialization method/ init method
    def __init__(self, name, age, breed, temperament): #parameters: self, all the attributes
        # __init__ to provide objects(instances) with unique attributes upon the instantiation
        
        # Attached incoming parameters to the self's attributes
        self.name = name #self is always the instance
        self.age = age
        self.breed = breed
        self.temperament = temperament

        print(name, age, breed)


#instantiate a new instance
# baboi = Pet("Baboi", 8, "Chihuahua", "Tranquil") 


# what is self? 
    # self => instance of Pet class
    # <__main__.Pet object at 0x100e17910>
    # we know that the self is `baboi`, exactly same as the instance, `baboi``  


# 4.✅ Demonstrate instance methods by creating a print_pet_details function that will print the pet attributes
#     Review the self keyword 
#     Invoke the print_pet_details on an instance 
#           -> 
            # name:rose
            # age:11
            # breed:domestic longhair
            # temperament:sweet
            # image_url:rose.jpg

    def print_pet_details(self): #self is the instance

        #f string, multiline with Triple Single Quotes
        print (f''' 
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
            temperament:{self.temperament}
        ''')
        pass



#ipdb.set_trace()


# Instance / Object Properties => Attributes that are controlled by methods

    # Create an Owner class with two instance methods:

        #get_name => Retrieve Owner's name


        #set_name => Set Owner's name

            #Ensure that Owner's name is a string


            #If not, issue warning of "Name must be a string"

    #Use property() to compile get_name / set_name and invoke them

    #Whenever we access an Owner instance's name