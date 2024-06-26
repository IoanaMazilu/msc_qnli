trip_home_longer_premise = 1/2
trip_home_longer_hypothesis = 4/2

# the hypothesis refers to the longer time of the trip home compared to the beach trip
if trip_home_longer_hypothesis!= trip_home_longer_premise:
    # check if the longer time of the trip home in the hypothesis contradicts the longer time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
