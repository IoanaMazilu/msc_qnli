scott_avg_premise = 18
scott_avg_hypothesis = 38

# the hypothesis refers to the average golf score on the first four rounds
if scott_avg_hypothesis <= scott_avg_premise:
    # check if the hypothesis value contradicts the estimate of the premise
    label = "contradiction"
elif scott_avg_hypothesis > scott_avg_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the average golf score
    # any value greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
