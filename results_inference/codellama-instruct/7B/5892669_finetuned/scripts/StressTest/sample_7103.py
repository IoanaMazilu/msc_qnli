distance_driven_at_60mph_premise = 240
distance_driven_at_60mph_hypothesis = 140
distance_driven_at_40mph_premise = 120
distance_driven_at_40mph_hypothesis = 120

# the hypothesis refers to the distance driven at 60mph and 40mph mentioned in the premise
if distance_driven_at_60mph_premise!= distance_driven_at_60mph_hypothesis:
    # check if the distance driven at 60mph in the hypothesis contradicts the distance driven at 60mph reported in the premise
    label = "contradiction"
elif distance_driven_at_40mph_premise!= distance_driven_at_40mph_hypothesis:
    # check if the distance driven at 40mph in the hypothesis contradicts the distance driven at 40mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
