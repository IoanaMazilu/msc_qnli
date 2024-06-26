# Define variables for the numerical entities in the premise and hypothesis
fuel_tank_premise = 60
distance_premise = 480

# Define variables for the numerical entities in the hypothesis
fuel_tank_hypothesis = 60

# Check if the hypothesis value contradicts the estimate of more than 'fuel_tank_premise'
if fuel_tank_hypothesis <= fuel_tank_premise:
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of gallons in the fuel tank
    # Any number of gallons greater than 'fuel_tank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
