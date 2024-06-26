debenture_period_premise = 78
debenture_period_hypothesis = 18

# the hypothesis refers to the agreed period of debenture mentioned in the premise
if debenture_period_hypothesis >= debenture_period_premise:
    # check if the value of 'debenture_period_hypothesis' contradicts the statement in the premise
    label = "contradiction"
elif debenture_period_hypothesis > debenture_period_premise:
    # check if the value of 'debenture_period_hypothesis' contradicts the statement in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
