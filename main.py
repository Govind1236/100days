# print("print('What to print')")
# string manupulation
# print("Hello" + " " + "Govind") # String concatenate
# print("Day 1 - string manipulation")
# print("String cocatenation is done with "+" sign")
# print("hello" + input("Enter Your Name: "))
# calculates the length of a string with PYTHON VARIAABLES
# name = input("Enter A Name: ")
# print("The length of character is" ,len(name))
# a = input("a:")
# b = input("b:")
# c = a
# a = b
# b = c
# print("a = ", a)
# print("b = ", b)
# Brand Name Generator
# print("Hello User welcome to brand name generator ")
# city_name = input("Which city you were born?\n")
# pet_name = input("What is the name of your pet?\n")
# # generator = city_name + pet_name
# print("The Brand You are looking for is " + city_name + " " + pet_name) #concatenation 
# print(pet_name[2]) #printing the index of pet_name 
# length  =len(input("Enter your name: "))
# new_length =  str(length)
# print("The length of your name is " + new_length + " character")
# two_digit_number = input("Enter a number: ")
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]

# result = int(first_digit )+ int(second_digit)
# print(result)
# print(3 * (3 + 3) / 3 - 3)
# name = input("Enter Your Name To Measure BMI: ")
# height = input("Enter Your Height In M: ")
# weight = input("Enter Your Weight In Kg: ")
# new_height = float(height)
# new_weight = float(weight)
# body_measure_index = new_weight / (new_height ** 2)
# print(f"{name} Your Body Measure Index Is: ", body_measure_index)
# print(round(34 / 3 ))
# Your Life In Weeks
# age = input("What is your current age? ")
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days_remaining  = years_remaining * 365
# weeks_remaining = years_remaining * 52  
# month_remaining = round(days_remaining / 30)
# print(f"You have {years_remaining} years, you have {days_remaining} days, you have {weeks_remaining} weeks, you have {month_remaining} months remaining")
# Tip Calculator
bill = float(input("What was the total bill? \n "))
# percentage = {0.12, .15, 0.1 }
percentage = float(input("What percentage tip would you like to give 10, 12 , 15 ? \n "))
if percentage == 10:
    Pay = bill * 0.1
elif percentage == 12:
    Pay = bill * 0.12
else:
  Pay = bill * .15 

total_bill = Pay + bill
num_people = int(input("How many people to split the bill? "))
pay_per_person = round(total_bill / num_people, 2)
print(f"Each should pay $ {pay_per_person}")
