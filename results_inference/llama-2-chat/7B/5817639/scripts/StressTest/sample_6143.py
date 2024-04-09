average_premise = 18
average_hypothesis = 38

# the hypothesis talks about the average golf score, which is also referred to in the premise
if average_hypothesis <= average_premise:
    # check if the hypothesis value contradicts the estimate of the average golf score in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average golf score
    # any average golf score greater than 'average_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
