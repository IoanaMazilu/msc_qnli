sreenivas_profit_premise = 50
sreenivas_profit_hypothesis = 10
shiva_loss_premise = 10
shiva_loss_hypothesis = 10

# the hypothesis refers to the profit percent of Sreenivas and loss percent of Shiva mentioned in the premise
if sreenivas_profit_premise < sreenivas_profit_hypothesis:
    # check if the profit percent of 'sreenivas_profit_hypothesis' contradicts the profit percent in the premise
    label = "contradiction"
elif shiva_loss_hypothesis != shiva_loss_premise:
    # check if the loss percent of Shiva in the hypothesis contradicts the loss percent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
