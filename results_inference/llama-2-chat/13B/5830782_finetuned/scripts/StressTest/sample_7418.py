years_future_premise = 18
years_future_hypothesis = 18

# the hypothesis refers to the same situation as the premise but estimates a different time period
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis time period contradicts the premise time period
    label = "contradiction"
else:
    # the premise gives an exact number of years in the future
    # any number of years greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
