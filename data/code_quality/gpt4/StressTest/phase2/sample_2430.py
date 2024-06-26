travel_time_premise = 15
travel_time_hypothesis = 65

# the hypothesis refers to the travel time of Sravan mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif travel_time_hypothesis > travel_time_premise:
    # the hypothesis value is greater than the premise value
    # any value less than 'travel_time_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
