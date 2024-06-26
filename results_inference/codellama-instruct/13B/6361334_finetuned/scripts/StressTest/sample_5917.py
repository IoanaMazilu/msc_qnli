premise_average_raise = 7
hypothesis_average_raise = 2

# the hypothesis refers to the number of points Jerry wants to raise his average by
if hypothesis_average_raise < premise_average_raise:
    # check if the hypothesis value contradicts the estimate of less than 'premise_average_raise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of points Jerry wants to raise his average by
    # any number of points greater than 'premise_average_raise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
