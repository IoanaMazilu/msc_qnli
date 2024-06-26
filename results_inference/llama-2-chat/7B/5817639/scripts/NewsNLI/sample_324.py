dead_premise = 21
injured_premise = 35

# the hypothesis mentions the number of dead and injured, which are also referenced in the premise
if dead_hypothesis!= dead_premise:
    # check if the number of dead in the hypothesis contradicts the number of dead in the premise
    label = "contradiction"
elif injured_hypothesis!= injured_premise:
    # check if the number of injured in the hypothesis contradicts the number of injured in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
