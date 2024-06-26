walk_distance_premise = 7
walk_distance_hypothesis = 2
walk_time_premise = 1.5
walk_time_hypothesis = 1.5

# the hypothesis refers to the distance Jack walked and the time he took to walk it
if walk_distance_premise < walk_distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif walk_time_premise!= walk_time_hypothesis:
    # check if the time in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
