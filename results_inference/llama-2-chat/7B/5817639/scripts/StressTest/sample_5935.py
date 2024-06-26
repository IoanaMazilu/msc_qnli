fuel_tank_premise = 20
fuel_tank_hypothesis = 60

# the hypothesis refers to a larger fuel tank than the one mentioned in the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the estimate of 'fuel_tank_hypothesis' contradicts the number of fuel tank in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fuel tank
    # any number of fuel tank greater than 'fuel_tank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
