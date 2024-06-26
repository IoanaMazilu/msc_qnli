total_age_premise = 45
total_age_hypothesis = 35

# the hypothesis refers to the total ages of Amar, Akbar and Anthony mentioned in the premise
if total_age_premise < total_age_hypothesis:
    # check if the estimate of 'total_age_hypothesis' contradicts the total age in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
