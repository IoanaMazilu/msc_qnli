fuel_tank_premise = 40
fuel_tank_hypothesis = 50

# the hypothesis refers to the size of the fuel tank, which is not mentioned in the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the hypothesis value contradicts the estimate of 'fuel_tank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the fuel tank
    # any size of fuel tank greater than 'fuel_tank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
