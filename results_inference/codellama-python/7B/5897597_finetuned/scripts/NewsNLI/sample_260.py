meth_seized_premise = 2000000
meth_seized_hypothesis = 2000000

# the hypothesis mentions the seizure of $2 million worth of methamphetamine, which is also mentioned in the premise
if meth_seized_hypothesis!= meth_seized_premise:
    # check if the amount of methamphetamine seized in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
