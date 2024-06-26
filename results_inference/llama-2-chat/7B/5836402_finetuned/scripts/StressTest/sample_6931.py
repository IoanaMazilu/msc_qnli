future_years_premise = 2
future_years_hypothesis = 6

# the hypothesis refers to the number of years in the future, mentioned in the premise
if future_years_hypothesis <= future_years_premise:
    # check if the hypothesis value contradicts the estimate of more than 'future_years_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'future_years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
