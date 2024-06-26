travel_hours_premise = 12
travel_hours_hypothesis = 82

# the hypothesis refers to the travel time of Rajan mentioned in the premise
if travel_hours_hypothesis != travel_hours_premise:
    # check if the travel time in the hypothesis contradicts the travel time reported in the premise
    label = "contradiction"
else:
    # if the travel hours in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
