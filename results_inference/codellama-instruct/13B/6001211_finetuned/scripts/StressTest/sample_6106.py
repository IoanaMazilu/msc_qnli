jane_age_premise = 82
jane_age_hypothesis = 32
babysitting_stop_years_premise = 12
babysitting_stop_years_hypothesis = 12

# the hypothesis refers to Jane's age and the years since she stopped baby-sitting, both mentioned in the premise
if jane_age_hypothesis >= jane_age_premise:
    # check if the age of Jane in the hypothesis contradicts the premise's estimate of less than 'jane_age_premise'
    label = "contradiction"
elif babysitting_stop_years_hypothesis!= babysitting_stop_years_premise:
    # check if the number of years since Jane stopped baby-sitting in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Jane's age
    # any age less than 'jane_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
