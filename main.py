# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# convert age to int
age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaininig = years_remaining * 52
months_remaining = years_remaining * 12

# print(months_remaining)

message = (f"You have {days_remaining} days, {weeks_remaininig} weeks, and {months_remaining} months left.")

print(message)
