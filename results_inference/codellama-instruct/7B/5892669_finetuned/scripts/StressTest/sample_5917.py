average_raise_premise = 7
average_raise_hypothesis = 2

# the hypothesis refers to the average raise Jerry wants to achieve, which is also mentioned in the premise
if average_raise_hypothesis >= average_raise_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_raise_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average raise
    # any average raise less than 'average_raise_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)