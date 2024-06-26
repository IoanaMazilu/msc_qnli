trip_home_premise = 1/2
trip_home_hypothesis = 4/2

# the hypothesis refers to the duration of the trip home in comparison to the trip to the beach
if trip_home_premise!= trip_home_hypothesis:
    # check if the duration of the trip home in the hypothesis contradicts the duration of the trip home in the premise
    label = "contradiction"
else:
    # if the duration of the trip home in the hypothesis does not contradict the duration of the trip home in the premise, we can infer entailment
    label = "entailment"

print(label)
