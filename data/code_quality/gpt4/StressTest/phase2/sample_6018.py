jane_age_premise = 32
jane_age_hypothesis = 42
babysitting_stop_premise = 10
babysitting_stop_hypothesis = 10

# the hypothesis refers to Jane's age and the years since she stopped babysitting mentioned in the premise
if jane_age_premise >= jane_age_hypothesis:
    # check if the estimate of 'jane_age_hypothesis' contradicts the age in the premise
    label = "contradiction"
elif babysitting_stop_hypothesis != babysitting_stop_premise:
    # check if the number of years since Jane stopped babysitting in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
