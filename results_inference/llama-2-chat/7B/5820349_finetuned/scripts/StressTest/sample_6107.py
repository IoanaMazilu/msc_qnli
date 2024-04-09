jane_age_premise = 32
jane_age_hypothesis = 32
babysitting_stop_years_premise = 12
babysitting_stop_years_hypothesis = 12

# the hypothesis refers to Jane's age and the years she stopped baby-sitting, both mentioned in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the premise value of 'jane_age_premise'
    label = "contradiction"
elif babysitting_stop_years_hypothesis!= babysitting_stop_years_premise:
    # check if the years she stopped baby-sitting in the hypothesis contradicts the years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
