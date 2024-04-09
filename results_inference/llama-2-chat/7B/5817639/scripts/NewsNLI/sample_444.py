differential_premise = 0
differential_hypothesis = 0

# the hypothesis mentions Wales' position relative to France, which is also mentioned in the premise
if differential_hypothesis!= differential_premise:
    # check if the position of Wales in the hypothesis contradicts its position in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
