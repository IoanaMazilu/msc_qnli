years_future_premise = 18
years_future_hypothesis = 18

# the hypothesis refers to the time period referenced in the premise
if years_future_hypothesis <= years_future_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific time period
    # any time period greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
