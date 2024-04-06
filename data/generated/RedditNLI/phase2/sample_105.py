# Premise: U.S. housing starts rise to 549,000 rate in March.
# Hypothesis: Housing Starts in U.S. Increased 7.2% in March to 549,000 Pace.
# Golden Label: neutral

housing_starts_rate_premise = 549000
housing_starts_rate_hypothesis = 549000
increase_percentage_hypothesis = 7.2

# the hypothesis and premise mention the rate of housing starts in the U.S. for March
if housing_starts_rate_premise != housing_starts_rate_hypothesis:
    # check if the rate of housing starts in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # the premise does not give any information about the increase percentage, so the increase percentage in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

