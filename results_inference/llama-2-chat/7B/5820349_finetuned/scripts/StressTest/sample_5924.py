trip_home_premise = 1/2
trip_home_hypothesis = 4/2

# the hypothesis refers to the duration of the trip home compared to the trip to the beach mentioned in the premise
if trip_home_hypothesis!= trip_home_premise:
    # check if the duration of the trip home in the hypothesis contradicts the duration reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
