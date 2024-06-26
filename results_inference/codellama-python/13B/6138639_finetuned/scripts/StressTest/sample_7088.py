dan_hours_premise = 6
dan_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works alone, which is also mentioned in the premise
if dan_hours_hypothesis >= dan_hours_premise:
    # check if the hypothesis value contradicts the premise estimate of 'dan_hours_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of hours Dan works alone
    # any number of hours less than 'dan_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
