debenture_period_premise = 38
debenture_period_hypothesis = 18

# the hypothesis refers to the agreed period of the debenture mentioned in the premise
if debenture_period_hypothesis >= debenture_period_premise:
    # check if the 'debenture_period_hypothesis' contradicts the period of less than 'debenture_period_premise' in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
