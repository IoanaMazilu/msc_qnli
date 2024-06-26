jane_age_start_babysitting_premise = 20
jane_age_start_babysitting_hypothesis = 40

# the hypothesis refers to the age Jane started babysitting, which is also mentioned in the premise
if jane_age_start_babysitting_hypothesis!= jane_age_start_babysitting_premise:
    # check if the age in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the age in the hypothesis does not contradict the age in the premise, we can infer entailment
    label = "entailment"

print(label)
