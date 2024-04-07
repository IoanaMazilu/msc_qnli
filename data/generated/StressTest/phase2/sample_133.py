# Premise: John will be less than 6 times as old as Tom in 4 years.
# Hypothesis: John will be 2 times as old as Tom in 4 years.
# Golden Label: neutral

john_future_age_ratio_premise = 6
john_future_age_ratio_hypothesis = 2

# the hypothesis talks about the ratio of John's future age to Tom's future age, which is also referenced in the premise
if john_future_age_ratio_hypothesis >= john_future_age_ratio_premise:
    # check if the hypothesis value contradicts the estimate of less than 'john_future_age_ratio_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of John's future age to Tom's
    # any ratio less than 'john_future_age_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

