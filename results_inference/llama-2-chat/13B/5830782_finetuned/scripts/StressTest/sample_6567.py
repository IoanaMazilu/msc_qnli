trip_home_premise = 1/2
trip_home_hypothesis = 7/2

# the hypothesis refers to the duration of the trip home mentioned in the premise
if trip_home_hypothesis <= trip_home_premise:
    # check if the estimate of 'trip_home_hypothesis' contradicts the duration of the trip home in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
