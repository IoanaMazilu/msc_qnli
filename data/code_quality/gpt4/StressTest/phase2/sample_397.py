series_premise = 7
series_hypothesis = 4

# the hypothesis refers to a series problem mentioned in the premise
if series_hypothesis >= series_premise:
    # check if the first number in the series in the hypothesis contradicts the first number in the series in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the first number in the series
    # any number less than 'series_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
