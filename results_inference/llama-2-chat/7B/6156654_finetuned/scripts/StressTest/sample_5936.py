fuel_tank_premise = 60
fuel_tank_hypothesis = 60
distance_premise = 480
distance_hypothesis = 480

# The hypothesis mentions the fuel tank size, which is also mentioned in the premise
if fuel_tank_hypothesis <= fuel_tank_premise:
    # Check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # Check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
