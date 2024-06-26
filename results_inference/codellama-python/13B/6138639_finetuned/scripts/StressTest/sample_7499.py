jane_age_premise = 34
jane_age_hypothesis = 44
babysitting_stop_age_premise = 10
babysitting_stop_age_hypothesis = 10

# the hypothesis talks about Jane's age and the time she stopped baby-sitting, both referenced in the premise
if jane_age_hypothesis!= jane_age_premise:
    # check if the age in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif babysitting_stop_age_hypothesis!= babysitting_stop_age_premise:
    # check if the time when Jane stopped baby-sitting in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
