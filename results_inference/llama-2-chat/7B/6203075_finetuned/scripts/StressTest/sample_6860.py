miles_walked_premise = 4
miles_walked_hypothesis = 4
time_walked_premise = 1.25
time_walked_hypothesis = 1.25

# the hypothesis refers to the distance walked and time walked, both mentioned in the premise
if miles_walked_hypothesis <= miles_walked_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif time_walked_hypothesis!= time_walked_premise:
    # check if the time walked in the hypothesis contradicts the time walked in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
