travel_time_premise = 10
travel_time_hypothesis = 10

# the hypothesis refers to the travel time of Raman mentioned in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif travel_time_hypothesis < travel_time_premise:
    # if the hypothesis value is less than the premise, it is consistent with the premise
    # but it cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise, it is consistent with the premise
    # and can be explicitly entailed from the premise
    label = "entailment"

print(label)
