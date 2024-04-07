# Premise: Jaclyn buys $10 000 worth of debentures in a company.
# Hypothesis: Jaclyn buys $40 000 worth of debentures in a company.
# Golden Label: contradiction

debenture_premise = 10000
debenture_hypothesis = 40000

# the hypothesis refers to the amount of debentures Jaclyn bought, which is also mentioned in the premise
if debenture_hypothesis != debenture_premise:
    # check if the amount of debentures bought in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the amount of debentures bought in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)

