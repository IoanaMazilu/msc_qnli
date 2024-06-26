debenture_period_premise = 18
debenture_period_hypothesis = 18

# the hypothesis refers to the period of the debenture mentioned in the premise
if debenture_period_hypothesis >= debenture_period_premise:
    # check if the hypothesis contradicts the estimate of 'debenture_period_hypothesis' being less than the debenture period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
