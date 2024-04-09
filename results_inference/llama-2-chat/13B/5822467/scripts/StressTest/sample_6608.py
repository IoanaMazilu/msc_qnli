loss_premise = 2 * 4 * (2 / 100) ** 2
loss_hypothesis = 6 * 4 * (6 / 100) ** 2

# the hypothesis refers to the amount of loss after 6 years, while the premise refers to the amount of loss after 2 years
if loss_hypothesis <= loss_premise:
    # check if the estimate of 'loss_hypothesis' contradicts the amount of loss reported in the premise
    label = "contradiction"
elif loss_hypothesis > loss_premise:
    # check if the amount of loss in the hypothesis exceeds the amount of loss in the premise
    label = "entailment"
else:
    # if the hypothesis value and the premise value are the same, or the hypothesis value is less than the premise value, we can infer neutrality
    label = "neutral"

print(label)
