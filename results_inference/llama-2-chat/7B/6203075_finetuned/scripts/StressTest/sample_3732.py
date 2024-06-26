travel_time_premise = 7
travel_time_hypothesis = 8

# the hypothesis refers to the travel time from A to B and back, mentioned in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise, it contradicts the premise
    label = "contradiction"

print(label)
