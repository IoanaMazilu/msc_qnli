average_premise = 78
average_hypothesis = 78

# the hypothesis talks about the average score of 6 tests, while the premise refers to the first 3 tests
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of the average score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average score of the first 3 tests
    # any average score consistent with the premise is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
