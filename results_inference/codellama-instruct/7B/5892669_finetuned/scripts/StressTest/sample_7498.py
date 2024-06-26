jane_age_premise = 54
jane_age_hypothesis = 34
babysitting_stop_years_premise = 10
babysitting_stop_years_hypothesis = 10

# the hypothesis refers to Jane's age and the year she stopped babysitting, both mentioned in the premise
if jane_age_hypothesis >= jane_age_premise:
    # check if the age in the hypothesis contradicts the premise of Jane being less than 54 years old
    label = "contradiction"
elif babysitting_stop_years_hypothesis!= babysitting_stop_years_premise:
    # check if the year when Jane stopped babysitting in the hypothesis contradicts the year reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Jane's age
    # any age less than 'jane_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
