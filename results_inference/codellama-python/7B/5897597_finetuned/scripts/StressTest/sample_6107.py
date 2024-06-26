jane_age_premise = 32
jane_age_hypothesis = 32
jane_stop_babysitting_premise = 12
jane_stop_babysitting_hypothesis = 12

# the hypothesis refers to Jane's age and when she stopped baby-sitting, both mentioned in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the exact age of Jane in the premise
    label = "contradiction"
elif jane_stop_babysitting_hypothesis!= jane_stop_babysitting_premise:
    # check if the hypothesis value contradicts the time Jane stopped baby-sitting in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
