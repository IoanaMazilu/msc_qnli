indu_loss_premise = 2 * 4 * (2 / 100) ** 2
indu_loss_hypothesis = 2 * 4 * (less_than_2 / 100) ** 2

# the hypothesis refers to the length of time Indu lent the money to Bindu
if indu_loss_hypothesis <= indu_loss_premise:
    # check if the hypothesis value contradicts the estimate of the loss after 2 years
    label = "contradiction"
elif indu_loss_hypothesis > indu_loss_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # the hypothesis value is less than the premise value, but the premise value is not explicitly entailed from the hypothesis
    label = "neutral"

print(label)
