debenture_period_premise = 18
debenture_period_hypothesis = 78

# the hypothesis refers to the period of the debenture mentioned in the premise
if debenture_period_hypothesis <= debenture_period_premise:
    # check if the hypothesis value contradicts the period of debenture in the premise
    label = "contradiction"
elif debenture_period_premise >= debenture_period_hypothesis:
    # check if the period of debenture in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
