he_age_ratio_premise = 5/3
he_age_ratio_hypothesis = 1

# the hypothesis refers to the age ratio mentioned in the premise
if he_age_ratio_premise <= he_age_ratio_hypothesis:
    # check if the estimate of 'he_age_ratio_hypothesis' contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
