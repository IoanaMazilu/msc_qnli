# Premise: Molly's age in less than 88 years will be seven times her age six years ago.
# Hypothesis: Molly's age in 18 years will be seven times her age six years ago.
# Golden Label: neutral

future_age_premise = 88
future_age_hypothesis = 18
multiplication_factor = 7
past_age = 6

# the hypothesis talks about Molly's future and past age, referenced also in the premise
if future_age_hypothesis >= future_age_premise:
    # check if the estimate of 'future_age_hypothesis' contradicts the premise's estimate of Molly's future age
    label = "contradiction"
else:
    # the premise gives only an estimate for the Molly's future age
    # any age less than 'future_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

