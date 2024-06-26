weight_gain_premise = 10
weight_gain_hypothesis = 50

# the hypothesis refers to the weight gain of Leo, which is also mentioned in the premise
if weight_gain_hypothesis < weight_gain_premise:
    # check if the hypothesis value contradicts the weight gain in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the weight gain of Leo
    # any weight gain greater than 'weight_gain_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
