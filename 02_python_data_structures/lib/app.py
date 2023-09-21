# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.
 
#in JS we have  => arrays and objects
#in python we have => lists and dictionaries


# Creating Lists
#1. ✅ Create a list of 10 pet names
#Mutable -> values can be changed (lists are mutable)
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']
banana = ['b', 'a','n', 'a', 'n', 'a']
# ----------------------------------Reading Information From Lists
#2. ✅ Return the first pet name 
print(pet_names[0])#should print Rose
print(pet_names[-1])# to get the last value



#3. ✅ Return all pet names beginning from the 3rd index
print(pet_names[3:5]) # Its exculsive does not include the last index in this case 5
print(pet_names[:5]) # it will start from the beginning till index 5 which wont be shown
print(pet_names[5:])# starts from fifth index till the end


#4. ✅ Return all pet names before the 3rd index
print(pet_names[:3])


#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
print(pet_names[3:7])


#6. ✅ Find the index of a given element
print(pet_names.index("Lea")) # .index is used to get the index of an element


#7. ✅ Reverse the original list
print(pet_names.reverse())# this mutatest and changes the original List
print(pet_names , "reversed")


#8. ✅ Return the frequency of a given element - how many times it appears
print(banana.count("n"))


# -------------------------Updating Lists
#9. ✅ Change the first element to all uppercase 
pet_names[0] = pet_names[0].upper()
print(pet_names)


#10. ✅ Append a new name to the list
pet_names.append("Blu")# muatates the list and adds the element at the end
print(pet_names)


#11. ✅ Add a new name at a specific index
pet_names.insert(0, "Coco")
print(pet_names)


#12. ✅ Add two lists together 
added_list = [1,2,3] + [4,5,6]
print(added_list)


#13. ✅ Remove the final element from the list
print(pet_names.pop())
print(pet_names)


#14. ✅ Remove element by specific index
print(pet_names.pop(7))
print(pet_names)


#15. ✅ Remove a specific element 
pet_names.append("Rose")
print(pet_names)
pet_names.remove('Rose') #only first Rose is removed
print(pet_names)


#16. ✅ Remove all pet names from the list
print(pet_names.clear())
print(pet_names)


#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable

#17. ✅ Create a Tuple of pet 10 ages -> ⛔️ cannot be changed
pet_ages = (3, 2 ,6 ,1 ,7 ,2 ,5, 6)


#18. ✅ Print the first pet age
# print(pet_ages[0])

# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
 #AttributeError: 'tuple' object has no attribute 'pop'


#20. ✅ Attempt to change the first element (should error)
# pet_ages[0] = 'shshs' 
# print(pet_ages)


# Tuple Methods
#21. ✅ Return the frequency of a given element
# print(pet_ages.count(6))


#22. ✅ Return the index of a given element 
# print(pet_ages.index(6))


#23. ✅ Create a Range  default start value is 0 and step value is 1
#Note:  Ranges are primarily used in loops
# range_1 = range(0, 10 ,1)#wont include the 10 the last digit added (2) means it will skip by two
# for i in range_1:
#     print(i)

# range_2 = range(5 , 2, -1 )
# for i in range_2:
#     print(i)
    
#with a while loop
i = 1
while(i < 10) :
   
    print(i)
    i += 1





# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods


# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {'name':'rose',
                 'age':11,
                 'breed':'domestic long '} #unlike js ur keys have to be a string 


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_spot = dict(name='Spot', age=25, breed='boxer')
empty_dict = dict()
print(empty_dict)


# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
print(pet_info_rose['name'])


#28. ✅ Print the pet attribute of "age" using ".get"
print(pet_info_rose.get('name'))


#Note: 🔴 ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error


# Updating 
#29. ✅ Update the pets age to 12
pet_info_rose['age'] =12
print(pet_info_rose)
#if you add something that doest exist it will add a new key value

pet_info_rose['goals'] = 'none'
print(pet_info_rose)


#30. ✅ Update the other pets age to 26
pet_info_spot ["age"] = 26
print(pet_info_spot)


# Deleting
#30. ✅ Delete a pets age using the "del" keyword 
del pet_info_rose['goals']
print(pet_info_rose)


#31. ✅ Delete the other pets age using ".pop"
 
print(pet_info_spot.pop('age'))# will return the value
print(pet_info_spot) # will return the new dict


#32. ✅ Delete the last item in the pet dictionary using "popitem()"
pet_info_spot.popitem()
print(pet_info_spot)


# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]



#33. ✅ Loop through a range of 10 and print every number within the range
# range_10 = range(0,10)
# for i in range_10:
#     print(i)



#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
range_50 = range(50, 60 , 2)
for i in range_50:
    print(i)


#35. ✅ Loop through the "pet_info" list and print every dictionary 
for pet in pet_info:
    print(pet.get('name'))


#36. ✅ Create a function that takes a list as an argument 
def print_info(list = pet_info):
    for pet in pet_info:
        print(pet)
print_info()


    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument


#37. ✅ Create a function that takes a list as an argument. (simple example) 
def counter(lst = pet_info):
    counter = 0
    while(counter < len(lst)):
        counter += 1
    return counter
print(counter())
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 


#38. ✅ Create a function that updates the age of a given pet and # The function should take a list of "dict"s, "name" and "age" as parameters 
def update_age( info, name, age) :
    # Create am index variable and set it to 0
    current_index = 0
       # Create a while loop 
    while(current_index < len(info) and info[current_index].get('name') != name):
        current_index += 1
    if(current_index >= len(info)):
        print("error")
    else:
        info[current_index]['age'] = age
update_age(pet_info,'rose', 2)
print(pet_info)

   
        
     
            # The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'


# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
pet_upper_case = [pet.get('name').upper() for pet in pet_info]
print(pet_upper_case)

# find like
#40. ✅ Use list comprehension to find a pet named spot
pet_named_spot = [pet for pet in pet_info if pet.get('name') == 'spot'] # first pet is the return value


# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old
pet_under_three = [pet for pet in pet_info if pet.get('age') < 25]
print(pet_under_three)


#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 

