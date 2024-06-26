walking_distance_premise = 7
walking_distance_hypothesis = 3
walking_time_premise = 1 + 15
walking_time_hypothesis = 1 + 15

# the hypothesis refers to the distance and time Jack walked, also mentioned in the premise
if walking_distance_hypothesis!= walking_distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif walking_time_hypothesis!= walking_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
