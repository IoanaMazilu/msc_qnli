debenture_period_premise = 18
debenture_period_hypothesis = 58

# the hypothesis refers to the period of debenture mentioned in the premise
if debenture_period_hypothesis != debenture_period_premise:
    # check if the period of the debenture in the hypothesis contradicts the period of the debenture reported in the premise
    label = "contradiction"
else:
    # if the period of debenture in the hypothesis does not contradict the period of debenture in the premise, we can infer entailment
    label = "entailment"

print(label)
