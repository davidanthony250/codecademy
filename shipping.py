weight = 4.8
print("The package weighs " + str(weight) + " pounds.")

# Ground Shipping
cost = 0.0
if weight <= 0:
  print("Error: Weight must be greater than zero.")
elif weight <= 2:
  cost = weight * 1.5 + 20
elif weight <= 6:
  cost = weight * 3 + 20
elif weight <= 10:
  cost = weight * 4 + 20
elif weight > 10:
  cost = weight * 4.75 + 20
else:
  print("Unknown error.")
rounded_cost = format(cost, ".2f")
print("The cost for ground shipping is $" + str(rounded_cost) + "." )

# Premium Ground Shipping
premium_Ground = 125.00
print("The cost for premium ground shipping is $" + str(format(premium_Ground, ".2f")) +".")

# Drone Shipping
if weight <= 0:
  print("Error: Weight must be greater than zero.")
elif weight <= 2:
  cost = weight * 4.5
elif weight <= 6:
  cost = weight * 9
elif weight <= 10:
  cost = weight * 12
elif weight > 10:
  cost = weight * 14.25
else:
  print("Unknown error.")
rounded_cost = format(cost, ".2f")
print("The cost for drone shipping is $" + str(rounded_cost) + "." )
