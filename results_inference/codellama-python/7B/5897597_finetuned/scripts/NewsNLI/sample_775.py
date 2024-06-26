funding_premise = 1000000
funding_hypothesis = 1000000

# the hypothesis mentions the amount of funding for the USDA investigation, which is also mentioned in the premise
if funding_hypothesis!= funding_premise:
    # check if the funding amount in the hypothesis contradicts the funding amount reported in the premise
    label = "contradiction"
else:
    # if the funding amount in the hypothesis does not contradict the funding amount in the premise, we can infer entailment
    label = "entailment"

print(label)
