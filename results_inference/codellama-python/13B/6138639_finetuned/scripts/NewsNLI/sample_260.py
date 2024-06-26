methamphetamine_seized_premise = 2000000
methamphetamine_seized_hypothesis = 2000000

# the hypothesis mentions the amount of methamphetamine seized, which is also mentioned in the premise
if methamphetamine_seized_hypothesis!= methamphetamine_seized_premise:
    # check if the amount of methamphetamine seized in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
