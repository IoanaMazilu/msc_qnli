average_premise = 90
average_hypothesis = 90

# the hypothesis talks about the average score of more than 3 tests, while the premise refers to the first 3 tests
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of the average score in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average score of the first 3 tests, while the hypothesis talks about a larger number of tests
    # any average score greater than 90 for more than 3 tests is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
