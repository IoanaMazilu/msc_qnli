epicenter_distance_premise = 360
epicenter_distance_hypothesis = 360

# the hypothesis mentions the distance of the epicenter from Manila, which is also mentioned in the premise
if epicenter_distance_hypothesis!= epicenter_distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
