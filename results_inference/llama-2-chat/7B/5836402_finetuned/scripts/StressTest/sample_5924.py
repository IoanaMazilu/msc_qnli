trip_home_longer_premise = 1/2
trip_home_longer_hypothesis = 4/2

# the hypothesis refers to the time difference between the trip to the beach and the trip home mentioned in the premise
if trip_home_longer_hypothesis!= trip_home_longer_premise:
    # check if the time difference in the hypothesis contradicts the time difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
