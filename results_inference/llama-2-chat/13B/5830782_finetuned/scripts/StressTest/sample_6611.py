years_in_future_premise = 18
years_in_future_hypothesis = 18

# the hypothesis refers to the same situation as the premise, but with a different time estimate
if years_in_future_hypothesis <= years_in_future_premise:
    # check if the hypothesis estimate contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific number of years in the future
    # any number of years greater than 'years_in_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
