fuel_tank_premise = 20
fuel_tank_hypothesis = 60
distance_premise = 480

# the hypothesis refers to the fuel tank capacity and the distance to be flown
if fuel_tank_hypothesis > fuel_tank_premise:
    # check if the estimate of 'fuel_tank_hypothesis' contradicts the fuel tank capacity reported in the premise
    label = "contradiction"
elif fuel_tank_hypothesis == fuel_tank_premise:
    # check if the fuel tank capacity in the hypothesis is consistent with the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the fuel tank capacity
    # any fuel tank capacity greater than 'fuel_tank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

# the hypothesis also refers to the distance to be flown, which is the same in both premise and hypothesis
if distance_premise == distance_hypothesis:
    # check if the hypothesis value contradicts the distance reported in the premise
    label = "contradiction"
else:
    # the premise and hypothesis have different distances, so no conclusion can be drawn
    label = "neutral"

print(label)
