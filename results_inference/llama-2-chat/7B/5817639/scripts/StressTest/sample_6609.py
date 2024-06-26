age_premise = 18
age_hypothesis = 88

# the hypothesis talks about Molly's age in the future, while the premise refers to her age 7 years ago
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of Molly's age in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for Molly's age 7 years ago, and the hypothesis talks about her age in the future
    # any age greater than the estimate in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
