scott_avg_premise = 38
scott_avg_hypothesis = 48

# the hypothesis refers to the average golf score on the first four rounds
if scott_avg_hypothesis <= scott_avg_premise:
    # check if the hypothesis value contradicts the estimate of the premise
    label = "contradiction"
elif scott_avg_hypothesis > scott_avg_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the average golf score
    # any value less than 48 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
