interest_premise = 4
years_premise = 6

interest_hypothesis = 2
years_hypothesis = 2

loss_premise = (years_premise * interest_premise) / 100
loss_hypothesis = (years_hypothesis * interest_hypothesis) / 100

# check if the hypothesis value contradicts the estimate of loss in the premise
if loss_hypothesis > loss_premise:
    label = "contradiction"
elif loss_hypothesis < loss_premise:
    label = "entailment"
else:
    # the premise gives only an estimate for the loss
    # any loss value consistent with the premise is neutral
    label = "neutral"

print(label)
