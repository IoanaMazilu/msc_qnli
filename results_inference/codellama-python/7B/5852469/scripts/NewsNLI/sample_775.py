funding_premise = 1000000
funding_hypothesis = 1000000

# the hypothesis mentions the amount of money allocated for the USDA investigation, which is also mentioned in the premise
if funding_hypothesis!= funding_premise:
    # check if the amount of funding from the hypothesis contradicts the amount of funding in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
