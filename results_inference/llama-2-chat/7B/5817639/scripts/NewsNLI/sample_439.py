dead_premise = 3
injured_premise = 52

# the hypothesis mentions the number of people killed and injured, which are also referenced in the premise
if dead_hypothesis!= dead_premise:
    # check if the number of people killed in the hypothesis contradicts the number of people killed in the premise
    label = "contradiction"
elif injured_hypothesis!= injured_premise:
    # check if the number of people injured in the hypothesis contradicts the number of people injured in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
