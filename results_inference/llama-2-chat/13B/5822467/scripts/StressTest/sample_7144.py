scott_avg_premise = 48
scott_avg_hypothesis = 38

# the hypothesis refers to the average golf score of Scott on his first four rounds
if scott_avg_hypothesis <= scott_avg_premise:
    # check if the hypothesis value contradicts the estimate of less than 48 in the premise
    label = "contradiction"
elif scott_avg_hypothesis > scott_avg_premise:
    # check if the hypothesis value entails the estimate of less than 48 in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the average golf score
    # any value of the average golf score less than 48 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
