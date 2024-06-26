debenture_period_premise = 18
debenture_period_hypothesis = 18

# the hypothesis also talks about the period of the debenture, mentioned in the premise
if debenture_period_hypothesis > debenture_period_premise:
    # check if the hypothesis estimate contradicts the exact period mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
