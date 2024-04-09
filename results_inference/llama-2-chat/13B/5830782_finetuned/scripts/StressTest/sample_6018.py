jane_age_premise = 32
jane_age_hypothesis = 42
babysitting_stop_premise = 10
babysitting_stop_hypothesis = 10

# the hypothesis refers to Jane's age and when she stopped babysitting, both mentioned in the premise
if jane_age_premise > jane_age_hypothesis:
    # check if Jane's age in the premise contradicts the hypothesis that she is less than 'jane_age_hypothesis'
    label = "contradiction"
elif babysitting_stop_premise!= babysitting_stop_hypothesis:
    # check if the hypothesis contradicts the premise regarding when Jane stopped babysitting
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
