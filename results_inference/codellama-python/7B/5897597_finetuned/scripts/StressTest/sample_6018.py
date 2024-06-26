jane_age_premise = 32
jane_age_hypothesis = 42
babysitting_stop_premise = 10
babysitting_stop_hypothesis = 10

# the hypothesis refers to Jane's age and when she stopped baby-sitting, both mentioned in the premise
if jane_age_premise >= jane_age_hypothesis:
    # check if the hypothesis value contradicts the age mentioned in the premise
    label = "contradiction"
elif babysitting_stop_hypothesis!= babysitting_stop_premise:
    # check if the hypothesis value contradicts the time when Jane stopped baby-sitting
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
