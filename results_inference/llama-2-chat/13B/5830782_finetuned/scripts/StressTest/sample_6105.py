jane_age_premise = 32
jane_age_hypothesis = 82
jane_babysitting_stop_premise = 12
jane_babysitting_stop_hypothesis = 12

# the hypothesis refers to Jane's age and the years she stopped babysitting, both mentioned in the premise
if jane_age_premise > jane_age_hypothesis:
    # check if Jane's age in the premise contradicts the hypothesis' maximum age
    label = "contradiction"
elif jane_babysitting_stop_hypothesis!= jane_babysitting_stop_premise:
    # check if the years Jane stopped babysitting in the hypothesis contradicts the years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
