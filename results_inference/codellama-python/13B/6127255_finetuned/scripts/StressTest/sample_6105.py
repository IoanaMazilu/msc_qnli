jane_age_premise = 32
jane_age_hypothesis = 82
babysitting_stop_years_premise = 12
babysitting_stop_years_hypothesis = 12

# the hypothesis refers to Jane's age and the years since she stopped babysitting, both mentioned in the premise
if jane_age_premise > jane_age_hypothesis:
    # check if Jane's age in the premise contradicts the hypothesis that she is less than 82 years old
    label = "contradiction"
elif babysitting_stop_years_premise!= babysitting_stop_years_hypothesis:
    # check if the years since Jane stopped babysitting in the premise contradict the same value in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
# 