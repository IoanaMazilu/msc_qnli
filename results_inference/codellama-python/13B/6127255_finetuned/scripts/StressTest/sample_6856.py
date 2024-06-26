lower_limit_premise = 5
lower_limit_hypothesis = 1
upper_limit = 35

# the hypothesis refers to the same range of coin sums as the premise, but with a different lower limit
if lower_limit_hypothesis < lower_limit_premise:
    # check if the lower limit in the hypothesis contradicts the lower limit in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the lower limit of the coin sums
    # any lower limit greater than 'lower_limit_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
