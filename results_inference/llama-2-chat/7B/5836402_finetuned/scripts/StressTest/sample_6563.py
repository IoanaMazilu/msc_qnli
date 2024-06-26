average_increase_premise = 2
average_increase_hypothesis = 2

# the hypothesis refers to the same average increase as in the premise
if average_increase_hypothesis <= average_increase_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_increase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average increase
    # any average increase greater than 'average_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
