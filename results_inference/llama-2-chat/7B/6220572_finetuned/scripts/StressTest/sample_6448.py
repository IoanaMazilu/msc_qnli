years_future_premise = 8
years_future_hypothesis = 5

# the hypothesis refers to the number of years until John is twice as old as Frank, also mentioned in the premise
if years_future_hypothesis >= years_future_premise:
    # check if the estimate of 'years_future_hypothesis' contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
