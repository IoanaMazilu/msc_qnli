average_premise = 38
average_hypothesis = 48

# the hypothesis talks about Scott's average golf score, which is also referred to in the premise
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the average golf score, and the hypothesis value is consistent with that estimate
    label = "entailment"

print(label)
