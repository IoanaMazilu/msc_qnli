trip_home_premise = 0.5
trip_home_hypothesis = 0.5

# the hypothesis refers to the duration of the trip home in relation to the trip to the beach, also mentioned in the premise
if trip_home_hypothesis > trip_home_premise:
    # check if the hypothesis value contradicts the duration of the trip home in the premise
    label = "contradiction"
elif trip_home_hypothesis < trip_home_premise:
    # check if the hypothesis value contradicts the duration of the trip home in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
