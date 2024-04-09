jane_age_premise = 32
jane_age_hypothesis = 35

# the hypothesis refers to Jane's current age and the time she stopped baby-sitting
if jane_age_premise <= jane_age_hypothesis:
    # check if the estimate of 'jane_age_hypothesis' contradicts the premise
    label = "contradiction"
elif jane_age_hypothesis - jane_age_premise > 10:
    # check if the time elapsed since Jane stopped baby-sitting contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
