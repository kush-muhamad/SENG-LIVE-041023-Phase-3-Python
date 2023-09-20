#!/usr/bin/env python3

# 📚 Review With Students:
# Python environment set up
# Python debugging tools
# Python datatypes

# 🚨 To enable ipdb debugging, first import "ipdb"

# import ipdb
# before_ipdb = "before_ipdb"

# ipdb.set_trace() # pauses the excution of code
# after_ipdb = "after_ipdb"

# when declaring variables we dont need let , const unlike js
# we HAVE to assign a value to a variable when its created
pet_mood = "Hungry!"
pet_name = "Tiger"


# 1. ✅ Create a condition to check a pet's mood
# If "pet_mood" is "Hungry!", "Rose needs to be fed."
# If "pet_mood" is "Rowdy!", "Rose needs a walk."
# In all other cases, "Rose is all good."

# if pet_mood == "Hungry!": #triple equals doesnt exit in python unlike js
#     print(f"{pet_name}  needs to be feed") #interpolation is f{then word to be added}
# elif pet_mood == "Rowdy":
#     print("Rose needs a walk")
# else:
#     print("Rose is all good")

# Note => Feel free to set your own values for "pet_mood" to view various outputs.


# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
# If pet_food is "Hungry!" => "Rose needs to be fed."
# In all other cases => "Rose is all good."

# in JS we had contidition ? true :else
# in Python  true if condition else false ie:

print(f"{pet_name}  needs to be feed") if pet_mood == "Hungry!" else print(
    f"{pet_name} is all good")


# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
# Test invocation of "say_hello" in ipdb using "say_hello()"
# say_hello() => "Hello, world!"

def say_hello(name):
    return f"hello, {name}!"


print(say_hello("Kush"))  # calling the function
# print(say_hello()) this wont work unlike in JS (TypeError: say_hello() missing 1 required positional argument: 'name')
# have to pass in value unless ur paremeter is a default


def default_hello(name="Muha"):
    return f"hello {name}!"


print(default_hello())  # ⛔️works cause the set paremeter has a default value

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
# Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
# pet_greeting("Rose") => "Rose says hello!"
# pet_greeting("Spot") => "Spot says hello!"


def pet_greeting(name):
    return f"hello pet {pet_name}"


print(pet_greeting("momo"))

# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
# Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
# pet_status("Rose", "Hungry!") => "Rose needs to be fed."
# pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
# pet_greeting("Bud", "Relaxed") => "Bud is all good."


def pet_status(pet_mood, pet_name):
    if pet_mood == "Hungry!":  # triple equals doesnt exit in python unlike js
        # interpolation is f{then word to be added}
        print(f"{pet_name}  needs to be fed")
    elif pet_mood == "Rowdy!":
        print(f"{pet_name} needs a walk")
    else:
        print(f"{pet_name} is all good")
pet_status('Rowdy!', 'phantom')


    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.

# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors.
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

def pet_birthday(age):
    try: #make sure user is passing an integer
       new_age = age + 1
       print(f"Happy Birthday , You are {new_age}!")
    except TypeError:
        print("age must be an integer")

pet_birthday('hey')

    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()
