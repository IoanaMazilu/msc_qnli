ambulances_premise = 12
helicopters_premise = 7
ambulances_hypothesis = 12
helicopters_hypothesis = 7

# the hypothesis mentions the number of ambulances and helicopters dispatched to the scene, which are also mentioned in the premise
if ambulances_hypothesis != ambulances_premise:
    # check if the number of ambulances in the hypothesis contradicts the number of ambulances reported in the premise
    label = "contradiction"
elif helicopters_hypothesis != helicopters_premise:
    # check if the number of helicopters from the hypothesis contradicts the number of helicopters in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
