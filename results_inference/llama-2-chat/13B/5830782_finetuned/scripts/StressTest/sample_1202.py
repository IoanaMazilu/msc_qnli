travel_time_premise = 7
travel_time_hypothesis = 1

# the hypothesis talks about the time of travel from A to B and back, referenced also in the premise
if travel_time_hypothesis!= travel_time_premise:
    # check if the time of travel in the hypothesis contradicts the time of travel mentioned in the premise
    label = "contradiction"
else:
    # if the time of travel in the hypothesis does not contradict the time of travel in the premise, we can infer entailment
    label = "entailment"

print(label)
