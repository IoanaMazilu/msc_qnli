jane_age_premise = 32
jane_age_hypothesis = 42
babysitting_stop_year_premise = 10
babysitting_stop_year_hypothesis = 10

# the hypothesis refers to Jane's age and when she stopped babysitting, both mentioned in the premise
if jane_age_premise > jane_age_hypothesis:
    # check if Jane's age in the premise contradicts the hypothesis that Jane is less than 42 years old
    label = "contradiction"
elif babysitting_stop_year_premise!= babysitting_stop_year_hypothesis:
    # check if the year Jane stopped babysitting contradicts the year mentioned in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
