age_premise = 6
age_hypothesis = 2

# the hypothesis talks about Sandy's age after a specific time frame, referenced also in the premise
if age_hypothesis <= age_premise:
    # check if the hypothesis value contradicts the estimate of Sandy's age in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for Sandy's age after 6 years, and the hypothesis gives an estimate for Sandy's age after more than 2 years
    # any age greater than 30 years after more than 2 years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
