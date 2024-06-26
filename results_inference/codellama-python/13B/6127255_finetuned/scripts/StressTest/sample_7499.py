jane_age_premise = 34
jane_age_hypothesis = 44
jane_stop_babysitting_premise = 10
jane_stop_babysitting_hypothesis = 10

# the hypothesis refers to Jane's age and when she stopped babysitting, both mentioned in the premise
if jane_age_premise!= jane_age_hypothesis:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
elif jane_stop_babysitting_premise!= jane_stop_babysitting_hypothesis:
    # check if the time when Jane stopped babysitting in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
