# # Functions inputs/functionality/output
#
# # Add
# def add(n1, n2):
#     return n1 + n2
#
#
# # Subtract
# def subtract(n1, n2):
#     return n1 - n2
#
#
# # Multiply
# def multiply(n1, n2):
#     return n1 * n2
#
#
# # Divide
# def divide(n1, n2):
#     return n1 / n2
#
#
# # Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
#
# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# results = calculate(add, 2, 3)
# print(results)

# Nested Functions
# def outer_function():
#     print("I'm outer")
#
#     def inner_function():
#         print("I'm inner")
#
#     inner_function()
#
# outer_function()

# Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def inner_function():
#         print("I'm inner")
#
#     return inner_function
#
# nested_function = outer_function()
# nested_function()

## Python Decorator Function
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    time.sleep(2)
    print("Bye")


def say_greeting():
    print("How are you?")


decorated_function = delay_decorator(say_greeting)
decorated_function()
