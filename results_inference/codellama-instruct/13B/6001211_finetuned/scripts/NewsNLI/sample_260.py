seized_meth_premise = 2000000
seized_meth_hypothesis = 2000000

# the hypothesis mentions the amount of methamphetamine seized by authorities, which is also mentioned in the premise
if seized_meth_hypothesis!= seized_meth_premise:
    # check if the amount of methamphetamine seized in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
