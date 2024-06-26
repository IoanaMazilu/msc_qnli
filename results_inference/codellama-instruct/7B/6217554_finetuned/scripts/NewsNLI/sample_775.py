funding_premise = 1000000
funding_hypothesis = 1000000

# the hypothesis mentions the funding for the USDA investigation, which is also mentioned in the premise
if funding_hypothesis!= funding_premise:
    # check if the funding in the hypothesis contradicts the funding reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)