weight_premise = 10
weight_hypothesis = 50

# the hypothesis talks about the weight of Leo and Kendra, referenced also in the premise
if weight_hypothesis <= weight_premise:
    # check if the hypothesis value contradicts the estimate of less than 'weight_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of Leo and Kendra
    # any weight greater than 'weight_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
