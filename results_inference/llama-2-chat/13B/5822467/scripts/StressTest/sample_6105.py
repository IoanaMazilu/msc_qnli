jane_age_premise = 32
jane_age_hypothesis = 82

# the hypothesis refers to Jane's current age and the time she stopped baby-sitting
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif jane_age_premise <= 12:
    # check if the premise value contradicts the time mentioned in the hypothesis
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
