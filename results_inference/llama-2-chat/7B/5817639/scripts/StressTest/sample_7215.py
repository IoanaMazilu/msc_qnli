fuel_tank_premise = 60
fuel_tank_hypothesis = 20

# the hypothesis refers to the fuel tank capacity in the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the hypothesis value contradicts the estimate of 'fuel_tank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the fuel tank capacity
    # any fuel tank capacity greater than 'fuel_tank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
