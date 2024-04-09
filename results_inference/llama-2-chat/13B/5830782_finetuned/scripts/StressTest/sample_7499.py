jane_age_premise = 34
jane_age_hypothesis = 44
babysitting_stop_year_premise = 10
babysitting_stop_year_hypothesis = 10

# the hypothesis talks about Jane's age and when she stopped babysitting, both mentioned in the premise
if jane_age_premise!= jane_age_hypothesis:
    # check if the hypothesis value contradicts the premise value for Jane's current age
    label = "contradiction"
elif babysitting_stop_year_premise!= babysitting_stop_year_hypothesis:
    # check if the hypothesis value contradicts the premise value for when Jane stopped babysitting
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
