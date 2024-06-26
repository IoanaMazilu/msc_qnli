years_future_premise = 18
years_future_hypothesis = 88
years_past = 7

# the hypothesis refers to the same situation as the premise, but with different time frames
if years_future_hypothesis < years_future_premise:
    # check if the time frame in the future in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # the premise does not provide any information about Molly's age in the future
    # any time frame in the future that is not explicitly contradicted by the premise is consistent with it, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
