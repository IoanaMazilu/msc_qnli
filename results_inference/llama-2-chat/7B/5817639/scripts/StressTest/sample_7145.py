average_premise = 38
average_hypothesis = 36

# the hypothesis refers to a lower value than the premise's average
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of 'average_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the average, and the hypothesis provides a lower value, which is consistent with the premise
    label = "entailment"

print(label)
