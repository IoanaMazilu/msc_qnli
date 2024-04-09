jane_age_premise = 82
jane_age_hypothesis = 32
years_since_babysitting_premise = 12

# the hypothesis refers to Jane's current age and the number of years since she stopped baby-sitting
if jane_age_hypothesis <= jane_age_premise:
    # check if the estimate of 'jane_age_hypothesis' contradicts the premise
    label = "contradiction"
elif years_since_babysitting_premise!= years_since_babysitting_hypothesis:
    # check if the number of years since Jane stopped baby-sitting in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
