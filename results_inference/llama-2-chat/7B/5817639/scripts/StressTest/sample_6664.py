chiefs_premise = 6
chiefs_hypothesis = 7

# the hypothesis refers to a higher number of Joint Chiefs of Staff than the premise
if chiefs_hypothesis <= chiefs_premise:
    # check if the hypothesis value contradicts the estimate of 'chiefs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Joint Chiefs of Staff
    # any number of Joint Chiefs of Staff greater than 'chiefs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
