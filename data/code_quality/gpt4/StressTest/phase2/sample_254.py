sum_ages_future_premise = 51
sum_ages_future_hypothesis = 51

# the hypothesis refers to the sum of the ages from the premise
if sum_ages_future_hypothesis >= sum_ages_future_premise:
    # check if the hypothesis value contradicts the exact sum of ages from the premise
    label = "contradiction"
else:
    # the hypothesis value does not exceed the premise value, but it does not explicitly entail it either
    label = "neutral"

print(label)
