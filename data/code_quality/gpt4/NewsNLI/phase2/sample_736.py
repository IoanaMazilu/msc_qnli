reporters_premise = 2
journalists_hypothesis = 1

# the hypothesis mentions the number of journalists accused of being an Israeli spy, which is also referenced in the premise
if reporters_premise != journalists_hypothesis:
    # check if the number of reporters in the premise contradicts the number of journalists in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "neutral"

print(label)
