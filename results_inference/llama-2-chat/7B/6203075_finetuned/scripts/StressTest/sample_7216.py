fuel_tank_premise = 20
fuel_tank_hypothesis = 60
distance_cleveland = 480

# the hypothesis refers to the fuel tank size and distance to Cleveland mentioned in the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the hypothesis value contradicts the estimate of more than 'fuel_tank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the fuel tank size
    # any fuel tank size greater than 'fuel_tank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
