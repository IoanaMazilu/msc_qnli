travel_time_premise = 15
travel_time_hypothesis = 75

# the hypothesis refers to the same travel time mentioned in the premise
if travel_time_hypothesis != travel_time_premise:
    # check if the travel time in the hypothesis contradicts the travel time reported in the premise
    label = "contradiction"
else:
    # if the travel time in the hypothesis does not contradict the travel time in the premise
    label = "entailment"

print(label)
