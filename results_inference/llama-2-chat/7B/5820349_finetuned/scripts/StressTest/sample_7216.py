fuel_tank_premise = 20
fuel_tank_hypothesis = 60
distance_premise = 480
distance_hypothesis = 480

# the hypothesis refers to the fuel tank capacity and distance to Cleveland mentioned in the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # check if the fuel tank capacity in the hypothesis contradicts the premise estimate of more than 'fuel_tank_premise'
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance to Cleveland in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fuel tank capacity
    # any fuel tank capacity greater than 'fuel_tank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
