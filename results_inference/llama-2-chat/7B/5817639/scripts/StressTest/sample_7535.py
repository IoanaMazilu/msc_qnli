weight_premise = 10
weight_hypothesis = 80

# the hypothesis talks about the weight of Leo and Kendra, referenced also in the premise
if weight_hypothesis <= weight_premise:
    # check if the hypothesis value contradicts the estimate of weight in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the weight of Leo, and any weight greater than that estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
