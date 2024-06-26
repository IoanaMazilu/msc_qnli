trip_home_premise = 1/2
trip_home_hypothesis = 7/2

# the hypothesis refers to the duration of the trip home, which is also mentioned in the premise
if trip_home_hypothesis <= trip_home_premise:
    # check if the hypothesis value contradicts the duration of the trip home in the premise
    label = "contradiction"
elif trip_home_hypothesis > trip_home_premise:
    # any duration of the trip home greater than 'trip_home_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
