average_premise = 78
average_hypothesis = 78

# the hypothesis talks about the average score on the first 3 tests, which is consistent with the premise
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of the average score in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the average score on the first 4 tests, and the hypothesis value is consistent with that estimate
    label = "entailment"

print(label)
