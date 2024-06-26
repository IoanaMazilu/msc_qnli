jane_age_premise = 54
jane_age_hypothesis = 34
babysitting_stop_year_premise = 10
babysitting_stop_year_hypothesis = 10

# the hypothesis refers to Jane's age and the year she stopped baby-sitting, both mentioned in the premise
if jane_age_hypothesis >= jane_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jane_age_premise'
    label = "contradiction"
elif babysitting_stop_year_hypothesis!= babysitting_stop_year_premise:
    # check if the year Jane stopped baby-sitting in the hypothesis contradicts the year reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Jane's age
    # any age less than 'jane_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
