travel_time_premise = 7
travel_time_hypothesis = 1

# the hypothesis refers to the travel time from A to B and back, mentioned in the premise
if travel_time_hypothesis!= travel_time_premise:
    # check if the travel time in the hypothesis contradicts the travel time reported in the premise
    label = "contradiction"
else:
    # if the travel time in the hypothesis does not contradict the travel time in the premise, we can infer entailment
    label = "entailment"

print(label)
