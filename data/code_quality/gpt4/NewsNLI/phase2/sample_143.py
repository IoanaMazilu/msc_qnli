funding_premise = 225000000
funding_hypothesis = 225000000

# the hypothesis mentions the amount of funding received by Pinterest, which is also mentioned in the premise
if funding_hypothesis != funding_premise:
    # check if the funding amount in the hypothesis contradicts the funding amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
