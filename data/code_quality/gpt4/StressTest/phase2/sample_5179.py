average_premise = 35
average_hypothesis = 95

# the hypothesis refers to Joe's average on his first 5 tests, which is also mentioned in the premise
if average_hypothesis <= average_premise:
    # check if the hypothesis average contradicts the estimate of more than 'average_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average
    # any average greater than 'average_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
