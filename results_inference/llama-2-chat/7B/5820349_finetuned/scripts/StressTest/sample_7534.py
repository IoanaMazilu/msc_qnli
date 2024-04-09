weight_gain_premise = 50
weight_gain_hypothesis = 10

# the hypothesis refers to the weight gain of Leo mentioned in the premise
if weight_gain_hypothesis >= weight_gain_premise:
    # check if the weight gain in the hypothesis contradicts the premise
    label = "contradiction"
elif weight_gain_hypothesis < weight_gain_premise:
    # if the weight gain in the hypothesis is less than the premise, it is consistent with the premise
    # but we cannot explicitly entail it from the premise
    label = "neutral"

print(label)
