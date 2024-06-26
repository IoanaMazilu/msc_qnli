jane_age_premise = 32
jane_age_hypothesis = 32
babysitting_stop_years_premise = 10
babysitting_stop_years_hypothesis = 10

# the hypothesis refers to Jane's age and when she stopped babysitting, both mentioned in the premise
if jane_age_hypothesis <= jane_age_premise:
    # check if the hypothesis value contradicts the premise value of 'jane_age_premise'
    label = "contradiction"
elif babysitting_stop_years_hypothesis!= babysitting_stop_years_premise:
    # check if the number of years since Jane stopped babysitting in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
