weight_difference_premise = 50
weight_difference_hypothesis = 10

# the hypothesis refers to the weight difference between Leo and his sister Kendra, also mentioned in the premise
if weight_difference_hypothesis >= weight_difference_premise:
    # check if the estimate of 'weight_difference_hypothesis' contradicts the weight difference in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight difference
    # any weight difference less than 'weight_difference_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
