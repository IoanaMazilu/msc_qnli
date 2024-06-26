jane_age_premise = 42
jane_age_hypothesis = 32
baby_sitting_stop_year_premise = 10
baby_sitting_stop_year_hypothesis = 10

# the hypothesis refers to Jane's age and the year she stopped babysitting, both mentioned in the premise
if jane_age_hypothesis >= jane_age_premise:
    # check if the hypothesis value contradicts the estimate of less than 'jane_age_premise'
    label = "contradiction"
elif baby_sitting_stop_year_hypothesis != baby_sitting_stop_year_premise:
     # check if the hypothesis value contradicts the information of 'baby_sitting_stop_year_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Jane's age
    # exact age of 32 years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
