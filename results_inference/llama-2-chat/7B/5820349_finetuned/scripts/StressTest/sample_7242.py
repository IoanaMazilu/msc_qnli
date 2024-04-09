father_age_after_years_premise = 10
father_age_after_years_hypothesis = 80

# the hypothesis refers to the number of years mentioned in the premise
if father_age_after_years_premise >= father_age_after_years_hypothesis:
    # check if the number of years in the premise contradicts the estimate of less than 'father_age_after_years_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
