travel_time_premise = 7
travel_time_hypothesis = 8

# the hypothesis talks about the travel time from A to B and back to A, referenced also in the premise
if travel_time_hypothesis <= travel_time_premise:
    # check if the travel time in the hypothesis contradicts the travel time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
