years_future_premise = 18
years_future_hypothesis = 18

# the hypothesis refers to the same situation as the premise but with a different time estimate
if years_future_hypothesis <= years_future_premise:
    # check if the time estimate in the hypothesis contradicts the time estimate in the premise
    label = "contradiction"
else:
    # the premise gives only a specific time point for Molly's age
    # any time point greater than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
