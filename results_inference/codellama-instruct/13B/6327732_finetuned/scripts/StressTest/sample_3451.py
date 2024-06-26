joined_premise = 8
joined_hypothesis = 2

# the hypothesis refers to the number of months since Jose joined, which is less than the estimate in the premise
if joined_hypothesis >= joined_premise:
    # check if the hypothesis value contradicts the estimate of less than 'joined_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of months since Jose joined
    # any number of months less than 'joined_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
