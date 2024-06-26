epicenter_premise = "Negros"
epicenter_hypothesis = "Negros"
distance_premise = 360
distance_hypothesis = 360

# the hypothesis mentions the epicenter and the distance from Manila, which are also mentioned in the premise
if epicenter_hypothesis!= epicenter_premise:
    # check if the epicenter in the hypothesis contradicts the epicenter reported in the premise
    label = "contradiction"
elif distance_hypothesis!= distance_premise:
    # check if the distance from Manila in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
