fed_speed_premise = 2
sam_speed_premise = 5
meet_distance_hypothesis = 5

# the hypothesis refers to the speed of Fred and Sam mentioned in the premise
if meet_distance_hypothesis <= fed_speed_premise:
    # check if the hypothesis estimate contradicts the speed of Fred in the premise
    label = "contradiction"
elif sam_speed_premise!= 5:
    # check if the speed of Sam in the hypothesis contradicts the speed of Sam reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
