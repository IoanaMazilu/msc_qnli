distance_premise = 360
distance_hypothesis = 360

# the hypothesis mentions the distance from the epicenter to Manila, which is also referenced in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance from the epicenter to Manila in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
