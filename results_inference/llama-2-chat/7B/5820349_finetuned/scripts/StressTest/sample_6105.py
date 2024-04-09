jane_age_premise = 32
jane_age_hypothesis = 82
babysitting_stop_years_premise = 12
babysitting_stop_years_hypothesis = 12

# the hypothesis refers to Jane's age and the time when she stopped babysitting, both mentioned in the premise
if jane_age_premise >= jane_age_hypothesis:
    # check if Jane's current age contradicts the hypothesis that she is less than 'jane_age_hypothesis' years old
    label = "contradiction"
elif babysitting_stop_years_premise!= babysitting_stop_years_hypothesis:
    # check if the time when Jane stopped babysitting contradicts the time reported in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
