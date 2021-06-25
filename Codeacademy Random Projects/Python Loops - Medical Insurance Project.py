names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# goal is to calculate the average insurance cost that each person paid

# For Loop
#1: create the variable total_cost and set it to 0
total_cost = 0

#2: Use a for loop to iterate through actual_insurance_costs and add each insurance cost to the variable total_cost.

for cost in actual_insurance_costs:
  total_cost += cost

print(total_cost) # prints out 30800.0

#3: After the for loop, create a variable called average_cost that stores the total_cost divided by the length of the actual_insurance_costs list.
average_cost = total_cost/len(actual_insurance_costs)
print(average_cost) #print 4400.0

#4: Print average_cost with the following message:
print("Average Insurance Cost: " + str(average_cost) + " dollars.")

# Using Range in Loops
#5: For each individual in names, we want to determine whether their insurance cost is above or below average. Write a for loop with variable i that goes from 0 to len(names).

#for i in range(len(names)):

#6: Inside the loop Print out the insurance cost for each individual, with a message saying the <cost> for <name>
for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + "is " + str(insurance_cost) + " dollars.")

# Conditions Inside a Loop
for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + "is " + str(insurance_cost) + " dollars.")
#condition inside to check if cost is above average
  if insurance_cost > average_cost:
    print("The insurance cost for " + name + " is above average.")
#condition inside to check if cost is below average
  elif insurance_cost < average_cost:
    print("The insurance cost for " + name + " is below average.")
#if it is equal we can just set this to be the else statement
  else: 
    print("The insurance cost for " + name + " is equal to the average.")

# Creating a List Comprehension
# Using a list comprehension, create a new list called updated_estimated_costs, which has each element in estimated_insurance_costs multiplied by 11/10.

updated_estimated_costs = [cost * 11/10 for cost in estimated_insurance_costs]

print(updated_estimated_costs)