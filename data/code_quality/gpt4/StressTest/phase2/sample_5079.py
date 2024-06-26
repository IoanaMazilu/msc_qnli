years_future_premise = 6
years_future_hypothesis = 8
future_age_premise = 42
future_age_hypothesis = 42

# the hypothesis talks about the time it takes for Sandy to be 42 years old, referenced also in the premise
if future_age_premise != future_age_hypothesis:
    # check if the future age in the hypothesis contradicts the future age mentioned in the premise
    label = "contradiction"
elif years_future_hypothesis < years_future_premise:
    # check if the number of years in the future in the hypothesis contradicts the number of years in the future mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific time for when Sandy will be 42
    # any time less than 'years_future_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
