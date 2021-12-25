# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost

# Store calculated insurance costs estimation values in a list
insurance_cost_estimations = []

# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)
insurance_cost_estimations.append(maria_insurance_cost)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)
insurance_cost_estimations.append(rohan_insurance_cost)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)
insurance_cost_estimations.append(valentina_insurance_cost)

# Estimate Akira's insurance cost
akira_insurance_cost = estimate_insurance_cost(name = "Akira", age = 19, sex = 1, bmi = 27.1, num_of_children = 0, smoker = 0)
insurance_cost_estimations.append(akira_insurance_cost)

# List of names and paid amounts by each person
names = ["Maria", "Rohan", "Valentina", "Akira"]
paid_insurance_costs = [4150.0,5320.0,35210.0,2930.0]

# Combine name list and paid_insurances_costs list
actual_insurance_data = list(zip(names, paid_insurance_costs))
print("\nHere is the actual insurance cost data:\n\n{}".format(actual_insurance_data))
# Create a list and print the estimations with names and values
estimated_insurance_data = []
def fill_estimated_insurance_data():
  i = 0
  for insurance in insurance_cost_estimations:
    estimated_insurance_data.append([names[i], insurance])
    i += 1

fill_estimated_insurance_data()
print("\nHere is the estimated insurance cost data:\n\n{}".format(estimated_insurance_data))

#Calculate differences between real insurance price and estimation price

insurance_cost_difference = []

for index in range(len(estimated_insurance_data)):
  difference = estimated_insurance_data[index][1] - paid_insurance_costs[index]
  insurance_cost_difference.append([names[index],difference])
  print("\nThe margin between the price paid by {name} and our estimations is: {diff}$".format(name=names[index],diff=difference))
  if (difference < 0):
    print("Looks like {name} should change the insurance model.\n".format(name=names[index]))
