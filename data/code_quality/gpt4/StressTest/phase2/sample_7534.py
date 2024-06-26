weight_gain_premise = 50
weight_gain_hypothesis = 10

# the hypothesis refers to a possible weight gain for Leo, mentioned also in the premise
if weight_gain_hypothesis >= weight_gain_premise:
    # check if the weight gain in the hypothesis contradicts the estimate of less than 'weight_gain_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight gain
    # any weight gain less than 'weight_gain_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
