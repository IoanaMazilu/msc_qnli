fuel_tank_premise = 20
fuel_tank_hypothesis = 60
distance_premise = 480

# the hypothesis refers to the fuel tank capacity and the distance to be traveled
if fuel_tank_hypothesis > fuel_tank_premise:
    # the hypothesis explicitly entails the premise
    label = "entailment"
elif distance_premise > fuel_tank_hypothesis:
    # the hypothesis value is consistent with the premise, but the premise does not explicitly entail the hypothesis
    label = "neutral"
else:
    # the hypothesis value contradicts the premise
    label = "contradiction"

print(label)
