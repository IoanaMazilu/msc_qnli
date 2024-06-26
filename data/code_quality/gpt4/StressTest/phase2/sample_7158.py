future_years_premise = 6
future_years_hypothesis = 4
future_age_premise = 38
future_age_hypothesis = 38

# the hypothesis talks about Sandy's age after a certain number of years, referenced also in the premise
if future_age_hypothesis != future_age_premise:
    # check if the future age in the hypothesis contradicts the future age in the premise
    label = "contradiction"
elif future_years_hypothesis >= future_years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise gives an exact timeline for Sandy's age
    # any timeline less than 'future_years_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
