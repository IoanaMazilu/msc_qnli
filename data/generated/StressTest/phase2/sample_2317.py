# Premise: If in less than 64 years, John will be one year younger than twice the age of Mark on that day, how old is John today?
# Hypothesis: If in 14 years, John will be one year younger than twice the age of Mark on that day, how old is John today?
# Golden Label: neutral

years_future_premise = 64
years_future_hypothesis = 14

# the hypothesis refers to the same event as the premise, but in a different future year
if years_future_hypothesis >= years_future_premise:
    # check if the future year in the hypothesis contradicts the future year in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the future year
    # any future year less than 'years_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

