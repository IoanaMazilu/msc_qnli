hours_dan_premise = 6
hours_dan_hypothesis = 6

# the hypothesis refers to the number of hours Dan works alone, which is also mentioned in the premise
if hours_dan_hypothesis >= hours_dan_premise:
    # check if the hypothesis value contradicts the number of hours Dan works alone in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of hours Dan works alone
    # any number of hours less than 'hours_dan_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
