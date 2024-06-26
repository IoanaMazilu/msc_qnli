weight_gain_premise = 10
weight_gain_hypothesis = 80

# the hypothesis talks about the weight gain of Leo, referenced also in the premise
if weight_gain_hypothesis!= weight_gain_premise:
    # check if the weight gain in the hypothesis contradicts the weight gain mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight gain
    # any weight gain equal to 'weight_gain_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
