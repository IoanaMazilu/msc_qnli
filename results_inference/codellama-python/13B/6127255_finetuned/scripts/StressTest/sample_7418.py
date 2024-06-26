age_future_premise = 18
age_future_hypothesis = 18

# the hypothesis refers to the same situation as the premise, but with a different time estimate
if age_future_hypothesis <= age_future_premise:
    # check if the hypothesis time estimate contradicts the premise one
    label = "contradiction"
else:
    # the premise gives only a specific time point for Molly's age
    # any time point greater than 'age_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
