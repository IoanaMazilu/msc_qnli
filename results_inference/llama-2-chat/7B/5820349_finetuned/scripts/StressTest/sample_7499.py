jane_age_premise = 34
jane_age_hypothesis = 44
babysitting_stop_years_premise = 10
babysitting_stop_years_hypothesis = 10

# the hypothesis refers to Jane's age and the years she stopped baby-sitting, both mentioned in the premise
if jane_age_premise!= jane_age_hypothesis:
    # check if the age of Jane in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif babysitting_stop_years_hypothesis!= babysitting_stop_years_premise:
    # check if the years Jane stopped baby-sitting in the hypothesis contradicts the years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
