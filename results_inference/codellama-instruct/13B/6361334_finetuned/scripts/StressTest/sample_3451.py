joined_premise = 8
joined_hypothesis = 2

# the hypothesis refers to the number of months since Jose joined, which is also mentioned in the premise
if joined_hypothesis >= joined_premise:
    # check if the estimate of 'joined_hypothesis' contradicts the number of months in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of months
    # any number of months less than 'joined_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
