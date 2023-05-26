# 1. ✅ Demonstrate First Class Functions
    # Create functions to be used as callbacks 
    
def dance(music):
    print(f'We dance to {music}!')

def listen(music):
    print(f'We listen to {music} and love {music}!')

    # Create a higher-order function that will take a callback as an argument

def activate_fun(callbackfunc):
    return callbackfunc("Prince")

# activate_fun(dance)
# activate_fun(listen)

# 2. ✅ Create a higher-order function that returns a function

#def activate_fun(dance)
def activate_fun(): #instead of setting it as a parameter
    def dance(music): #let's define the same callback we wrote earlier
        return f'We dance to {music}!'
    
    return dance #return the inner function

#print(activate_fun()) # => feed function reference <function activate_fun.<locals>.dance at 0x1045da8c0>

#print(activate_fun()("Prince"))

# dance = activate_fun()
# print(dance("Prince"))

# 3. ✅ Demonstrate a decorator
    # 3-1. Create a function that takes a function as an argument 
    # 3-2. has an inner function
    # 3-3. returns the inner function

#1. decorator - outer function
def coupon_calculator(callbackfunc): #7 func as a parameter

    #2. inner function
    def report_price():
        print('Initial Price = $35.00') #3. print initial price
        final_price = callbackfunc(35.00) #4. calculate the final price w a new func #8. whatever func is passed in, it's going to be invoked
        print(f'Newly Discounted Price = ${final_price}') #5. interpolate the value print the final price

    return report_price #6. return the report_price function

#tools 
    #.format()
    # returns double decimal point
    #https://www.geeksforgeeks.org/python-string-format-method/

    #.round()
    #https://www.geeksforgeeks.org/round-function-python/


# Demo examples of the decorator with and without pie syntax '@'

    # Without pie syntax 
#12. 

#9. Build a callback func to calculate new price
def calculate_price(price):
    return '{:.2f}'.format(round(price / 2, 2)) #10. with two decimal point floating number, using format method
    #11. Divide price in half and round up w 2 decimal nums
    #this is how we want our string to be formatted

#coupon_calculator(calculate_price)()

#option2
xyz = coupon_calculator(calculate_price)
xyz()

    # With pie syntax
#13. decorator - it fires off and we can use the decorator function 
@coupon_calculator

def calculate_price(price):
    return '{:.2f}'.format(round(price / 2, 2)) 
calculate_price()


# @coupon_calculator
# def some_other_function():
#     return "something"
# some_other_function()

# @coupon_calculator
# def some_other_function2():
#     return "something else"
# some_other_function2()