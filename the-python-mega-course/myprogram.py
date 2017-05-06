import os
os.system('cls')

def currency_converter(rate, euros):
    dollars = euros*rate
    return dollars

print (currency_converter(100, 1000))

def age_foo(age):
    new_age = float(age) + 50
    return new_age

age = input("Enter your age: ")
print(age_foo(age))
