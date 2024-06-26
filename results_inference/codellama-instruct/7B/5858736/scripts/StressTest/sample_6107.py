jane_age_premise = 32
jane_age_hypothesis = 32
jane_babysitting_premise = 12
jane_babysitting_hypothesis = 12

# the hypothesis refers to the age and the time when Jane stopped baby-sitting
if jane_age_hypothesis <= jane_age_premise:
    # check if the estimate of 'jane_age_hypothesis' contradicts the age reported in the premise
    label = "contradiction"
elif jane_babysitting_hypothesis!= jane_babysitting_premise:
    # check if the time when Jane stopped baby-sitting in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
