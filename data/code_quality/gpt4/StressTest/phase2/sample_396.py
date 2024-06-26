series_begin_premise = 4
series_begin_hypothesis = 7

# the hypothesis refers to the start value of the series mentioned in the premise
if series_begin_premise >= series_begin_hypothesis:
    # check if the start value in the hypothesis contradicts the start value in the premise
    label = "contradiction"
else:
    # the premise gives a specific start value for the series
    # a start value greater than 'series_begin_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
