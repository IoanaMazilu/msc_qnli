commute_diff_premise = 2
commute_diff_hypothesis = 5

# the hypothesis refers to the same difference in commuting time mentioned in the premise
if commute_diff_hypothesis <= commute_diff_premise:
    # check if the hypothesis value contradicts the estimate of more than 'commute_diff_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference in commuting time
    # any difference in commuting time greater than 'commute_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
