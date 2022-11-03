#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculater")
total = input("What was the total bill?\n")
people = input("How many people have we here?\n")
tip= input("What percentage tip would you like to give 10,12,15?\n")

num_total= float(total)
num_people= int(people)
num_tip= float(tip)
amount= ((num_total * (num_tip/100)) + num_total)/num_people

print(f"For each person is {amount}")