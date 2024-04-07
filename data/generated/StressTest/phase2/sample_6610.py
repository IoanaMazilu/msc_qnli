# Premise: Molly's age in less than 88 years will be six times her age seven years ago.
# Hypothesis: Molly's age in 18 years will be six times her age seven years ago.
# Golden Label: neutral

years_future_premise = 88
years_future_hypothesis = 18
years_past = 7
multiplier = 6

# the hypothesis talks about Molly's age in the future and past, referenced also in the premise
if years_future_hypothesis >= years_future_premise:
    # check if the estimation of 'years_future_hypothesis' contradicts the estimation of 'years_future_premise'
    label = "contradiction"
elif years_future_hypothesis * multiplier <= years_past:
    # check if the calculation in the hypothesis contradicts the calculation in the premise
    label = "contradiction"
else:
    # the premise only gives an estimation for Molly's age in the future and past
    # any age calculation less than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

