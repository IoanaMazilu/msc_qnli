fuel_tank_size_premise = 20
fuel_tank_size_hypothesis = 60
distance_to_Cleveland = 480

# the hypothesis talks about the size of the fuel tank and the distance to Cleveland, which are also mentioned in the premise
if fuel_tank_size_hypothesis <= fuel_tank_size_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fuel tank size
    # any fuel tank size greater than 'fuel_tank_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
