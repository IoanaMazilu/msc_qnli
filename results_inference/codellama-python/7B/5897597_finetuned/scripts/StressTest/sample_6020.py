jane_age_premise = 32
jane_age_hypothesis = 32
babysitting_stop_premise = 10
babysitting_stop_hypothesis = 10

# the hypothesis refers to Jane's age and the time she stopped baby-sitting, both mentioned in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the exact age of Jane in the premise
    label = "contradiction"
elif babysitting_stop_hypothesis!= babysitting_stop_premise:
    # check if the time Jane stopped baby-sitting in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
