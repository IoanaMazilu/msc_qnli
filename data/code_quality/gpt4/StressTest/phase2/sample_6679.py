sum_age_premise = 43
sum_age_hypothesis = 93

# the hypothesis refers to the sum of ages of Aswin, Sachin and Sumesh mentioned in the premise
if sum_age_hypothesis <= sum_age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'sum_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the sum of ages
    # any sum of ages greater than 'sum_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
